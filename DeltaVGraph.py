import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import KerbalKnowledgeSystem
import DeltaVMap

deltaVMap = DeltaVMap.GetDeltaVMap()

def GraphGivenNodes(AvailableNodes):

    posList = DeltaVMap.GetPositionList()
    nameList = DeltaVMap.GetNameList()

    G = nx.DiGraph()

    for key in deltaVMap.keys():
        if(key in AvailableNodes):
            G.add_node(key, name=nameList[key], pos=posList[key])
            #print(key, nameList[key])
            for link in DeltaVMap.GetLinksFromDeltaVMap(deltaVMap, key):
                if((link in AvailableNodes) and (key in AvailableNodes)):
                    print(key, link)
                    G.add_edge(key, link, weight=DeltaVMap.GetValuesFromDeltaVMap(deltaVMap, key, link)[0])
    
    return G
    


nameList = DeltaVMap.GetNameList()

nameList = {x: v.replace(' ', '\n')
        for x, v in nameList.items()}

AvailableNodes = []
AvailableNodesNames = {}
AvailableNodes = KerbalKnowledgeSystem.FindAvailableNodeFromDeltaV(AvailableNodes, 300, 91050, 0, 0, 0)

print(AvailableNodes)

for Nodes in AvailableNodes:
    print(nameList[Nodes])
    AvailableNodesNames[Nodes] = nameList[Nodes]

G = GraphGivenNodes(AvailableNodes)

pos = nx.get_node_attributes(G, "pos")
plt.figure(3,figsize=(18,9))
nx.draw(G, pos, with_labels = True, labels=AvailableNodesNames, node_shape="s", font_size=10, arrowstyle="-", bbox=dict(facecolor="skyblue", edgecolor='black', boxstyle='round,pad=0.2'))
plt.show()