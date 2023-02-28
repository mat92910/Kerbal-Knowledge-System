#find the node that can be accesses with the given start node and delta v as either a single value or list of delta v of stages
def FindAvailableNodeFromDeltaV(Start, DeltaV, RoundTrip, Aerobreaking):
    AvailableNodes = [Start]