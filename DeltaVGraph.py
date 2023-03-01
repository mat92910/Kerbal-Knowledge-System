import networkx as nx
import matplotlib.pyplot as plt
import KerbalKnowledgeSystem
import DeltaVMap

#create graph with given AvailableNodes
#returns nx.DiGraph object
def GraphGivenNodes(AvailableNodes):

    deltaVMap = DeltaVMap.GetDeltaVMap()
    posList = DeltaVMap.GetPositionList()
    nameList = DeltaVMap.GetNameList()

    G = nx.DiGraph()

    #iterate through all node in DeltaVMap
    for key in deltaVMap.keys():
        #only if node is in AvailableNodes add node
        if(key in AvailableNodes):
            G.add_node(key, name=nameList[key], pos=posList[key])
            #iterate through all links
            for link in DeltaVMap.GetLinksFromDeltaVMap(deltaVMap, key):
                #only if link is in AvailableNodes add edge
                if((link in AvailableNodes) and (key in AvailableNodes)):
                    G.add_edge(key, link, weight=DeltaVMap.GetValuesFromDeltaVMap(deltaVMap, key, link)[0])
    
    return G
    
#Temperary Main Function

nameList = DeltaVMap.GetNameList()

nameList = {x: v.replace(' ', '\n')
        for x, v in nameList.items()}

AvailableNodes = []
AvailableNodesNames = {}
AvailableNodes = KerbalKnowledgeSystem.FindAvailableNodeFromDeltaV(AvailableNodes, 300, 91050, 0, 0, 0)

for Nodes in AvailableNodes:
    AvailableNodesNames[Nodes] = nameList[Nodes]

G = GraphGivenNodes(AvailableNodes)

pos = nx.get_node_attributes(G, "pos")
plt.figure(3,figsize=(18,9))
nx.draw(G, pos, with_labels = True, labels=AvailableNodesNames, node_shape="s", font_size=10, arrowstyle="-", bbox=dict(facecolor="skyblue", edgecolor='black', boxstyle='round,pad=0.2'))
plt.show()