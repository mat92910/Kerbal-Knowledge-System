import networkx as nx
import Blackboard

#create graph with given AvailableNodes
#returns nx.DiGraph object
def GraphGivenNodes(AvailableNodes):

    deltaVMap = Blackboard.GetDeltaVMap()
    posList = Blackboard.GetPositionList()
    nameList = Blackboard.GetNameList()

    G = nx.DiGraph()

    #iterate through all node in DeltaVMap
    for key in deltaVMap.keys():
        #only if node is in AvailableNodes add node
        if(key in AvailableNodes):
            G.add_node(key, name=nameList[key], pos=posList[key])
            #iterate through all links
            for link in Blackboard.GetLinksFromDeltaVMap(deltaVMap, key):
                #only if link is in AvailableNodes add edge
                if((link in AvailableNodes) and (key in AvailableNodes)):
                    G.add_edge(key, link, weight=Blackboard.GetValuesFromDeltaVMap(deltaVMap, key, link)[0])
    #return graph
    return G