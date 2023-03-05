import DeltaVMap

# find the nodes that can be accesses with the given start node and delta v as either a single value or list of delta v of stages
def FindAvailableNodeFromDeltaV(Nodes, Start, DeltaV, RoundTrip, Aerobreaking, PlaneChange):
    deltaVmap = DeltaVMap.GetDeltaVMap()

    
    # start with adding the start node to the return list, if it makes it here it's added
    if Start not in Nodes:
        Nodes.append(Start)
        #print(Start)
        #print("ADDED")

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

        #print("________")
        #print(DeltaV)
        #print(DeltaVLoss)
        #print("-------------        ")
        
        # if the loss is less than the delta v, sent that amount to it's links
        NewDeltaV = (DeltaV[0] - DeltaVLoss)

        
        if(NewDeltaV >= 0):
            NewList = DeltaV
            NewList[0] = NewDeltaV
            #print(NewList)
            Nodes = FindAvailableNodeFromDeltaV(Nodes, point, NewList, RoundTrip, Aerobreaking, PlaneChange)
        else:
            if(len(DeltaV) > 1): 
                #print("    POP    ")
                extra = DeltaV[0]
                NewList = []
                for i in range(1,len(DeltaV)):
                    NewList.append(DeltaV[i])
                NewList[0] += extra
                Nodes = FindAvailableNodeFromDeltaV(Nodes, Start, NewList, RoundTrip, Aerobreaking, PlaneChange)
              
   #loop end     
    
    return Nodes


# veery fancy main \\\(>>w<<)}}}}
AvailableNodes = []
Stages = [32000,200,2000]
StartingPoint = 300
AvailableNodes = FindAvailableNodeFromDeltaV(AvailableNodes, StartingPoint, Stages, 0, 0, 0)
NameList = DeltaVMap.GetNameList()
for Nodes in AvailableNodes:
    print(NameList[Nodes])
#print(AvailableNodes)