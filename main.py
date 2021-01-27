import wget
import json
import os
#Create Constants and Global Variables
global importedkits
global nodelist
global creatednodelist
creatednodelist = []
importedkits = {}
nodelist = []

global config

config = {
    "ASKFORURL": False,
    "PRESETLINK": "https://api.npoint.io/18d115461b2ab1e22dce",
    "AUTOUPDATE": True
}


#Associate Commands with Functions
def commands():
    command = raw_input("")
    if command == "loadjson":
        if os.path.exists("./JSON/kitsimported.json"):
            os.remove("./JSON/kitsimported.json")
        loadjson(True)
    elif command == "yml":
        loadjson(True)


def loadjson(url):
    if url == True:
        if config.get("ASKFORURL") == True:
            lnk = raw_input("Link to Json: ")
        elif config.get("PRESETLINK") != "" and config.get(
                "ASKFORURL") == False:
            lnk = config.get("PRESETLINK")
        #Download JSON File from URL and put it in ./JSON/kitsimported.json
        if config.get("AUTOUPDATE") == True:
            wget.download(lnk, 'JSON/kitsimported.json')
    with open("./JSON/kitsimported.json", "r") as read_file:
        importedkits = json.load(read_file)
    createyml(nodelist, importedkits)


def createnode(L, kit, ikk):
	#Create Command Placeholder Value
	cmd = "/k_" + ikk.get("kits").get(str(kit)).get("CMDID")
	#Insert Placeholders into String
	finalnode = "\'" + kit + "\'" + ":\n  command: " + cmd + "\n  type: RUN_COMMAND\n  runcmd:"
	#Iterate through commands and add them to final string
	if ikk.get("kits").get(str(kit)).get("CMDTYPE") == "ARMOR":
		for y in ikk.get("kits").get(str(kit)).get("INVSLOTS"):
			finalnode += "\n  - \'/replaceitem entity @s " + y.get("ID") + " " + y.get("ITEM") + " 1\'"
	elif ikk.get("kits").get(str(kit)).get("CMDTYPE") == "ENCHANT":
		for i in ikk.get("kits").get(str(kit)).get("INVSLOTS"):
			finalnode += "\'/execute if entity @s[nbt={Inventory:[{id:\"minecraft:netherite_helmet\",Slot:103b}]}] run /replaceitem entity @s armor.head netherite_helmet 1\'"
	#Print Results Formatted in Unicode
	print(u'\n' + finalnode)


def createyml(l, ik):
    #Iterate through each kit
    for x in ik.get("kits"):
        l.append(createnode(creatednodelist, x, ik))


commands()