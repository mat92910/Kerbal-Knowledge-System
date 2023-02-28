import json
from pathlib import Path

#DeltaVMap Dictionary key: id; value: {links with [deltaV value, MaxPlaneChangeDeltaV value, Aerobreaking]}
#DeltaVMap = {101:{100:[870,0,False], 103:[2400,0,False]}}
DeltaVMap = {101:{100:[870,0,False], 103:[2400,0,False]}}

def AddLinkToDeltaVMap(node, link, deltaV, planeChangeDeltaV, aerobreaking):
    global DeltaVMap
    if(link in DeltaVMap[node].keys()):
        return False
    else:
        DeltaVMap[node] = {link:[deltaV, planeChangeDeltaV, aerobreaking]}
        return True

def GetLinksFromDeltaVMap(node):
    global DeltaVMap
    if(node in DeltaVMap.keys()):
        return DeltaVMap[node].keys()
    else:
        return False

def GetValuesFromDeltaVMap(node, link):
    global DeltaVMap
    if(node in DeltaVMap.keys()):
        if(link in DeltaVMap[node].keys()):
            return DeltaVMap[node][link]
        else:
            return False
    else:
        return False

def PopulateDeltaVMap(file):
    filePath = Path(file)
    if(filePath.is_file()):
        with open(file) as DeltaVMapFile:
            DeltaVMapContents = json.load(DeltaVMapFile)
    
    print(len(DeltaVMapContents))
    print(DeltaVMapContents[1]["Id"])
    print(DeltaVMapContents[1]["Name"])
    print(len(DeltaVMapContents[1]["Links"]))

def main():
    PopulateDeltaVMap("./KnowledgeBase/DeltaVMap.json")

if __name__ == "__main__":
    main()