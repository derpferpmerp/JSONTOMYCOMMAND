import wget
import json
import pprint
import os
global importedkits
global nodelist
global creatednodelist
pp = pprint.PrettyPrinter(depth=4)
creatednodelist=[]
importedkits={}
nodelist=[]
def commands():
  command=raw_input("")
  if command=="loadjson":
    if os.path.exists("./JSON/kitsimported.json"):
      os.remove("./JSON/kitsimported.json")
    loadjson(True)
  elif command=="yml":
    loadjson(False)
def loadjson(url):
  if url==True:
    #lnk=raw_input("Link to Json: ")
    lnk="https://api.npoint.io/18d115461b2ab1e22dce"
    wget.download(lnk, 'JSON/kitsimported.json')
  with open("./JSON/kitsimported.json", "r") as read_file:
    importedkits = json.load(read_file)
  createyml(nodelist,importedkits)
def createnode(L,kit,ikk):
  cmd="/k_"+ikk.get("kits").get(str(kit)).get("CMDID")
  finalnode="\'"+kit+"\'"+":\n  command: "+cmd+"\n  type: RUN_COMMAND\n  runcmd:"
  for x in ikk.get("kits").get(str(kit)).get("INVSLOTS"):
    finalnode+="\n  - \'/replaceitem entity @s "+x.get("ID")+" "+x.get("ITEM")+" 1\'"
  print(u'\n'+finalnode)
def createyml(l,ik):
  for x in ik.get("kits"):
    l.append(createnode(creatednodelist,x,ik))
commands()