import DeltaVMap

#find the node that can be accesses with the given start node and delta v as either a single value or list of delta v of stages
def FindAvailableNodeFromDeltaV(Nodes, Start, DeltaV, RoundTrip, Aerobreaking, PlaneChange):
    deltaVmap = DeltaVMap.GetDeltaVMap()
   
    Nodes.append(Start)

    links = DeltaVMap.GetLinksFromDeltaVMap(deltaVmap, Start)
    for point in links:
        if(point in Nodes):
            continue
        DeltaVLoss = 0
        temp = DeltaVMap.GetValuesFromDeltaVMap(deltaVmap, Start, point)
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

        NewDeltaV = (DeltaV - DeltaVLoss)
        if(NewDeltaV >= 0):
           Nodes = FindAvailableNodeFromDeltaV(Nodes, point, NewDeltaV, RoundTrip, Aerobreaking, PlaneChange)

    return Nodes


AvailableNodes = []
AvailableNodes = FindAvailableNodeFromDeltaV(AvailableNodes, 300, 5500, 0, 0, 0)
NameList = DeltaVMap.GetNameList()
for Nodes in AvailableNodes:
    print(NameList[Nodes])
#print(AvailableNodes)