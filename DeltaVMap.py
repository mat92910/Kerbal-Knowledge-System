import json
from pathlib import Path

#DeltaVMap Dictionary key: id; value: {links with [deltaV value, MaxPlaneChangeDeltaV value, Aerobreaking]}
#DeltaVMap = {101:{100:[870,0,False], 103:[2400,0,False]}}
DeltaVMap = {}
NameList = {}

def AddLinkToDeltaVMap(node, link, deltaV, planeChangeDeltaV, aerobreaking):
    global DeltaVMap
    if(node in DeltaVMap.keys()):
        if(link in DeltaVMap[node].keys()):
            return False
        else:
            DeltaVMap[node][link] = [deltaV, planeChangeDeltaV, aerobreaking]
            return True
    else:
        DeltaVMap[node] = {link:[deltaV, planeChangeDeltaV, aerobreaking]}
        return True

def GetLinksFromDeltaVMap(DeltaVMap, node):
    if(node in DeltaVMap.keys()):
        return DeltaVMap[node].keys()
    else:
        return False

def GetValuesFromDeltaVMap(DeltaVMap, node, link):
    if(node in DeltaVMap.keys()):
        if(link in DeltaVMap[node].keys()):
            return DeltaVMap[node][link]
        else:
            return False
    else:
        return False

def PopulateDeltaVMap(file):
    global DeltaVMap
    global NameList
    filePath = Path(file)
    if(filePath.is_file()):
        with open(file) as DeltaVMapFile:
            DeltaVMapContents = json.load(DeltaVMapFile)
    
    for Nodes in DeltaVMapContents:
        NameList[Nodes["Id"]] = Nodes["Name"]
        for Links in Nodes["Links"]:
            AddLinkToDeltaVMap(Nodes["Id"], Links["Id"], Links["DeltaV"], Links["MaxPlaneChangeDeltaV"], Links["Aerobreaking"])

def PrintDeltaVMap(DeltaVMap, NameList):
    for key,subDict in DeltaVMap.items():
        print(key, NameList[key])
        for value in subDict.items():
            print("  : " + str(value[0]) + " " + NameList[value[0]])
            print("         Delta-V: \t\t" + str(value[1][0]))
            print("         Plane Change Delta-V: \t" + str(value[1][1]))
            print("         Aerobreaking: \t\t" + str(value[1][2]))


def GetDeltaVMap():
    global DeltaVMap
    PopulateDeltaVMap("./KnowledgeBase/DeltaVMap.json")
    return DeltaVMap.copy()

def GetDeltaVMap():
    global NameList
    PopulateDeltaVMap("./KnowledgeBase/DeltaVMap.json")
    return NameList.copy()