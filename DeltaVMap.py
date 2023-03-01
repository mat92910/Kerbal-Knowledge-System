import json
from pathlib import Path

#Add link between parent node and child with delta-v, plane change Delta-v and arebreaking as sub dictionary
#returns true if added, false if not
def AddLinkToDeltaVMap(DeltaVMap, node, link, deltaV, planeChangeDeltaV, aerobreaking):
    #check if node is in dictionary if yes continue else create
    if(node in DeltaVMap.keys()):
        #check if link is in sub dictioanry if yes return false else create fill sub dictionary with delta-v, plane change Delta-v and arebreaking as sub dictionary
        if(link in DeltaVMap[node].keys()):
            return False
        else:
            DeltaVMap[node][link] = [deltaV, planeChangeDeltaV, aerobreaking]
            return True
    else:
        DeltaVMap[node] = {link:[deltaV, planeChangeDeltaV, aerobreaking]}
        return True

#get the links associated with parent node
#returns links or false if none
def GetLinksFromDeltaVMap(DeltaVMap, node):
    if(node in DeltaVMap.keys()):
        return DeltaVMap[node].keys()
    else:
        return False

#get delta-v, plane change Delta-v and arebreaking
#return dictionary with delta-v, plane change Delta-v and arebreaking or false if none
def GetValuesFromDeltaVMap(DeltaVMap, node, link):
    if(node in DeltaVMap.keys()):
        if(link in DeltaVMap[node].keys()):
            return DeltaVMap[node][link]
        else:
            return False
    else:
        return False

#Populates DeltaVMap with values with given file
def PopulateDeltaVMap(file):
    DeltaVMap = {}
    filePath = Path(file)
    if(filePath.is_file()):
        with open(file) as DeltaVMapFile:
            DeltaVMapContents = json.load(DeltaVMapFile)
    
    #go throught the DeltaVMapContents and add the links to the DeltaVMap
    for Nodes in DeltaVMapContents:
        for Links in Nodes["Links"]:
            AddLinkToDeltaVMap(DeltaVMap, Nodes["Id"], Links["Id"], Links["DeltaV"], Links["MaxPlaneChangeDeltaV"], Links["Aerobreaking"])

    return DeltaVMap

#Populates NameList with values with given file
def PopulateNameList(file):
    NameList = {}
    filePath = Path(file)
    if(filePath.is_file()):
        with open(file) as DeltaVMapFile:
            DeltaVMapContents = json.load(DeltaVMapFile)
    
    #go throught the DeltaVMapContents and add the Name to the NameList
    for Nodes in DeltaVMapContents:
        NameList[Nodes["Id"]] = Nodes["Name"]

    return NameList

#print the DeltaVMap to console
def PrintDeltaVMap(DeltaVMap, NameList):
    for key,subDict in DeltaVMap.items():
        print(key, NameList[key])
        for value in subDict.items():
            print("  : " + str(value[0]) + " " + NameList[value[0]])
            print("         Delta-V: \t\t" + str(value[1][0]))
            print("         Plane Change Delta-V: \t" + str(value[1][1]))
            print("         Aerobreaking: \t\t" + str(value[1][2]))

#Populates the DeltaVMap with the file
#returns a Copy of the Populated DeltaVMap
def GetDeltaVMap():
    return PopulateDeltaVMap("./KnowledgeBase/DeltaVMap.json")

#Populates the NameList with the file
#returns a Copy of the Populated NameList
def GetNameList():
    return PopulateNameList("./KnowledgeBase/DeltaVMap.json")