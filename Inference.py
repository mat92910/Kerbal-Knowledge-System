import Blackboard

# find the nodes that can be accesses with the given start node and delta v as either a list of delta v of stages or a single value in a list
def FindAvailableNodeFromDeltaV(Nodes, Start, DeltaV, RoundTrip, Aerobreaking, PlaneChange):
    deltaVmap = Blackboard.GetDeltaVMap()
    nameList = Blackboard.GetNameList()
    # start with adding the start node to the return list, if it makes it here it's added
    if Start not in Nodes:
        Nodes.append(Start)

    # get node links to the start node from the map and loop them
    links = Blackboard.GetLinksFromDeltaVMap(deltaVmap, Start)
    for point in links:
        # check if in list already to avoid looping 
        if(point in Nodes):
            continue

        # get the value for delta v loss calculations    temp[0]=delta v cost  temp[1]=plane change cost   temp[2]=calculate aero bool
        temp = Blackboard.GetValuesFromDeltaVMap(deltaVmap, Start, point)
        tempReturn = Blackboard.GetValuesFromDeltaVMap(deltaVmap, point, Start)
        DeltaVLoss = 0

        # calculate Delta-V loss given modifiers 
        if(RoundTrip):
            if(Aerobreaking & (temp[2] or tempReturn[2])):
                if(temp[2]):
                    DeltaVLoss += (temp[0]*0.10 + tempReturn[0])
                elif(tempReturn[2]):
                    DeltaVLoss += (temp[0] + tempReturn[0]*0.10)
            else:
                DeltaVLoss += (temp[0] + tempReturn[0])
        else:
            if(Aerobreaking & temp[2]):
                DeltaVLoss += temp[0]*0.10
            else:
                DeltaVLoss += temp[0]

        # if the loss is less than the delta v, sent that amount to it's links and keeping the array
        NewDeltaV = (DeltaV[0] - DeltaVLoss)
        if(NewDeltaV >= 0):
            NewList = DeltaV.copy() # .copy() IMPORTANT
            NewList[0] = NewDeltaV
            Nodes = FindAvailableNodeFromDeltaV(Nodes, point, NewList, RoundTrip, Aerobreaking, PlaneChange)
        else:
            # check if more stages availble to pass on delta v while staging
            if(len(DeltaV) > 1):

                # save extra and add it to the next stage
                extra = DeltaV[0]
                
                # done this way due to recusive memory problems
                NewList = []
                for i in range(1,len(DeltaV)):
                    NewList.append(DeltaV[i])
                NewList[0] += extra

                Nodes = FindAvailableNodeFromDeltaV(Nodes, Start, NewList, RoundTrip, Aerobreaking, PlaneChange)         
    #loop end     
    
    return Nodes
#
#nodes = []
#Stages = [3800]
#nodes = FindAvailableNodeFromDeltaV(nodes, 300, Stages, 0, 0, 0)
#nameList = DeltaVMap.GetNameList()
#for key in nodes:
#    print(nameList[key])