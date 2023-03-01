import DeltaVMap

#find the node that can be accesses with the given start node and delta v as either a single value or list of delta v of stages
def FindAvailableNodeFromDeltaV(Nodes, Start, DeltaV, RoundTrip, Aerobreaking, PlaneChange):
    deltaVmap = DeltaVMap.GetDeltaVMap()
   
    Nodes.append(Start)

    links = DeltaVMap.GetLinksFromDeltaVMap(deltaVmap, Start)
    for i in links:
        if(i in Nodes):
            continue
        v = 0
        temp = DeltaVMap.GetValuesFromDeltaVMap(deltaVmap, Start, i)
        if(Aerobreaking):
            if(temp[2] & (not RoundTrip)):
                v = v + temp[0]*0.10
            elif(RoundTrip & (not temp[2])):
                v = v + temp[0]*2
            elif(temp[2] & RoundTrip):
                v = v + temp[0]*0.10 + temp[0]
            else:
                v = v + temp[0]
        else:
            if(RoundTrip):
                v = v + temp[0]*2
            else:
                v = v + temp[0]
        if(PlaneChange):
            v = v + temp[1]

        v = (DeltaV - v)
        if(v > 0):
           Nodes = FindAvailableNodeFromDeltaV(Nodes, i, v, RoundTrip, Aerobreaking, PlaneChange)

    return Nodes


AvailableNodes = []
AvailableNodes = FindAvailableNodeFromDeltaV(AvailableNodes, 300, 5500, 0, 0, 0)
NameList = DeltaVMap.GetNameList()
for Nodes in AvailableNodes:
    print(NameList[Nodes])
#print(AvailableNodes)