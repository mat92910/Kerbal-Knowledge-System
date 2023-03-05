import networkx as nx
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