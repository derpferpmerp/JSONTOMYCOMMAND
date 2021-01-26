# JSONTOMYCOMMAND
This Project was created in order for a user to be able to import JSON into the MyCommand Plugin on Spigot.

# Installation:
```bash
Reccomended Method (Installing Through Scripts):
  Download Start Script:
    WINDOWS (.bat): curl https://github.com/derpferpmerp/JSONTOMYCOMMAND/releases/download/v0.0.1/start.bat -O
    MACOSX (.sh): curl https://github.com/derpferpmerp/JSONTOMYCOMMAND/releases/download/v0.0.1/start.sh -O
  Add Permissions:
    WINDOWS: chmod 777 start.bat
    MACOSX: chmod 777 start.sh
  Run Script:
    WINDOWS: ./start.bat
    MACOSX: ./start.sh
  The Python Script Will Proceed to Download and Run

Installing Through Git:
  First Install Git:

  LINUX: $ sudo dnf install git-all 
  WINDOWS: https://git-scm.com/download/win

  Next Clone My Repository:

  git clone https://github.com/derpferpmerp/JSONTOMYCOMMAND.git
  cd JSONTOMYCOMMAND

  Then Run The Python Script:
  python main.py
```
# Documentation
```bash
Commands:
yml - converts JSON/file.json into YAML formatted MyCommand Text, then prints it
loadjson - updates the json from the web

Possible Errors:
Permission Error: 
Navigate to Directory
chmod 777 *
