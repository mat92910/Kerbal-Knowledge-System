import DeltaVMap

# find the nodes that can be accesses with the given start node and delta v as either a single value or list of delta v of stages
def FindAvailableNodeFromDeltaV(Nodes, Start, DeltaV, RoundTrip, Aerobreaking, PlaneChange):
    deltaVmap = DeltaVMap.GetDeltaVMap()
    

    # start with adding the start node to the return list, if it makes it here it's added
    Nodes.append(Start)

    # get node links to the start node from the map and loop them
    links = DeltaVMap.GetLinksFromDeltaVMap(deltaVmap, Start)
    for point in links:

        # check if in list already to avoid looping 
        if(point in Nodes):
            continue

        # get the value for delta v loss calculations    temp[0]=delta v cost  temp[1]=plane change cost   temp[2]=calculate aero bool
        temp = DeltaVMap.GetValuesFromDeltaVMap(deltaVmap, Start, point)
        DeltaVLoss = 0

        # simple if checks for delta v loss with diffrent checks
        if(Aerobreaking & temp[2]):
            if(RoundTrip):
                DeltaVLoss += (temp[0]*0.10 + temp[0])
            else:
                DeltaVLoss += temp[0]*0.10
        else:
            if(RoundTrip):
                DeltaVLoss += temp[0]*2
            else:
                DeltaVLoss += temp[0]
        if(PlaneChange):
            DeltaVLoss += temp[1]

        # if the loss is less than the delta v, sent that amount to it's links
        NewDeltaV = (DeltaV - DeltaVLoss)
        if(NewDeltaV >= 0):
           Nodes = FindAvailableNodeFromDeltaV(Nodes, point, NewDeltaV, RoundTrip, Aerobreaking, PlaneChange)

    return Nodes

def StagesDeltaV(Stages):
    for i in Stages:
        return sum(Stages)


# veery fancy main \\\(>>w<<)}}}}
AvailableNodes = []
Stages = [1000 ,000]
StartingPoint = 300
AvailableNodes = FindAvailableNodeFromDeltaV(AvailableNodes, StartingPoint, StagesDeltaV(Stages), 0, 0, 0)
NameList = DeltaVMap.GetNameList()
for Nodes in AvailableNodes:
    print(NameList[Nodes])
#print(AvailableNodes)