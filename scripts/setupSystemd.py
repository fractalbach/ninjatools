"""
+---------------------------------------------------------------------------+
|                      Setup Systemd with Systemctl                         |
|                                                                           |
|                             Chris Achenbach                               |
|                              18 April 2018                                |
+---------------------------------------------------------------------------+                              

- Creates a service file for systemd
- Overwrites that service file, which should keep it updated.
- Starts system

TODO
- Make a help message

TODO: Error checking
- check if the files were written correctly.
- Check if the service was started correctly.


TODO LATER
- have the service file live somewhere else. (or have a template)
- This program should simply move that file, and 

_____________________________________________________________________________
"""

import os
from pathlib import Path
from platform import system
from subprocess import call



# --------------------------------------------------------------------------
# Helper Functions
#
# Credits ~ Thanks for the Source Code: 
# https://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
# 
# function which acts like the Bash command "which", and returns the path
# at which the program is located. If it can't be found, it returns "None".
# 
def which(program):
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None



# --------------------------------------------------------------------------
# Check for Systemctl
# 
# Without Systemctl, this program is essentially pointless.  It would be
# wise to check for systemctl's existence before writing files everywhere.
#
# Most likely, systemctl is not going to be available on certain systems.
# In particular, windows will not have systemctl.
#
# checkForSystemctl uses the which() function to check for systemctl on
# the current system.  If all goes well, it prints a friendly message.
# If systemctl can't be found, the program can't continue.
#
def checkForSystemctl():
    x = which("systemctl")
    if x == None:
        print("Systemctl was not located in the OS path.  Exiting.")
        exit(1)
        
    print("Found systemctl at path:", x)

checkForSystemctl()

# Since this program is still in the experimental stage, it should warn the
# user that strange things may happen, and give them a chance to run away
# before this program destroys their computer.

ok = input("This is experimental, and may break something. Continue? (y/n)")
if ok == "n":
    print("Exiting program.")
    exit(0)
if ok != "y":
    print("I don't recognize that input... so I'm just going to exit.")
    exit(1)


# --------------------------------------------------------------------------
# Startup
#
# - Define constants/variables.
# - parsing flags. (THERE ARE CURRENTLY NO FLAGS)
# - print helpful messages. (THERE SHOULD BE A HELP MESSSAGE)

print("Starting the setup...")

filename = "simpleServer.service"
filepath = "/etc/systemd/system/"
fullpath = filepath + filename

q = Path(filepath)
print("Checking for the existence of path:",q)
if not q.exist():
    print("Error: path",q, "does not exist.")
    exit(1)



filecontents = """
[Unit]
Description=A Simple File Server
Documentation=https://github.com/fractalbach/ninjatools/
After=networking.target

[Service]
User=user
Type=simple
WorkingDirectory=/home/user/example/
StandardError=journal

[Install]
WantedBy=multi-user.target
"""
print(filecontents)



# --------------------------------------------------------------------------
# File Writing 
#
# - Write the File (it should automatically overwrite an existing file).
# - Opens up the file to check if the file write was successful.
#  
print("Writing to the file:", fullpath)

with open(fullpath, "w") as f:
    f.write(filecontents)

with open(fullpath, "r") as f:
    x = f.read()

if x == filecontents:
    print("File was successfully written.")
else:
    print("Error: The file's contents are different from what we intended to write.")
    exit(1)


# --------------------------------------------------------------------------
# Systemctl 
#
# - Start the service.
# - Enable the service.
# - TODO: Check if service is actually enabled correctly.
#
try:
    call(["sudo", "systemctl", "start", "simpleServer"])
    call(["sudo", "systemctl", "enable", "simpleServer"])
except Exception as e:
    raise e


# --------------------------------------------------------------------------
# Success.
# 
# - Hurray! We reached the end of this program without crashing.
#
print("Setup ended without errors. Hurray!")
exit(0)



