"""
+---------------------------------------------------------------------------+
|                      Setup Systemd with Systemctl                         |
|                                                                           |
|                             Chris Achenbach                               |
|                              19 April 2018                                |
+---------------------------------------------------------------------------+                              

Current Features:
- Accepts path location of a file in the command's arguments.
- Copies the file to /etc/systemd/system
- Reports any errors that occur during the attempt to copy the file.

TODO:
- Make a .config file.
- Start and enable the service.
- Infer targetpath based on systemd or systemctl configuration
- Resolve non-absolute paths.

CODE CLEANUP:
- use less variables
- make the object type more clear. (to avoid that Path vs. string problem)

_____________________________________________________________________________
"""

from __future__ import print_function
import argparse
import os
import sys
from pathlib import Path
from platform import system
from subprocess import call
from shutil import copyfile

# -------------------------------------------------------------------------- 
# Variables
# 
VERSION = "0.2"
TARGET_DIR = "/etc/systemd/system/"

# --------------------------------------------------------------------------
# Parse CLI Arguments
#
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file",
                    help="path of the input file.",
                    required="true")

parser.add_argument("-v", "--version",
                    help="displays current version of the program.",
                    action="version",
                    version="%(prog)s version " + VERSION)
args = parser.parse_args()

# --------------------------------------------------------------------------
# Determine Paths and Filenames
#
input_pathObject = Path(args.file).resolve()
input_path = str(input_pathObject)
input_filename = input_path.split('/')[-1]
target_path = TARGET_DIR + input_filename

# --------------------------------------------------------------------------
# Error Print and Exit 
# 
# function err() acts like the print(), but prints to standard error.
# Credits:
# https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
#
def err(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    exit(1)

# --------------------------------------------------------------------------
# Input Confirmation
#
print("Input Path = " + input_path)
if not input_pathObject.exists():
    err("Input Path does not exist.")
if not os.path.isfile(input_path):
    err("Input Path must lead to a file.")
if not os.access(input_path, os.R_OK):
    err("Input File needs to have read permissions.")

# --------------------------------------------------------------------------
# Target Confirmation
# 
print("Output Path = " + target_path)
if not Path(TARGET_DIR).exists():
    err("Target directory does not exist.  Cannot copy file.")

# --------------------------------------------------------------------------
# File Copying
# 
try:
    copyfile(input_path, target_path)
except Exception as e:
    raise e
else:
    print("File successfully copied to", target_path)

# --------------------------------------------------------------------------
# Helper Function
#
# which(program) acts like the Bash command "which", and returns the path
# at which the program is located. If it can't be found, it returns "None".
# 
# Credits:
# https://stackoverflow.com/questions/377017/test-if-executable-exists-in-python 

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
def checkForSystemctl():
    x = which("systemctl")
    if x == None:
        err("Systemctl was not located in the OS path.  Exiting.")
    print("Found systemctl at path:", x)
checkForSystemctl()

# --------------------------------------------------------------------------
# Start & Enable Using Systemctl 
#
# - Start the service.
# - Enable the service.
# - TODO: Check if service is actually enabled correctly.
# 
call(["sudo", "systemctl", "start", "simpleServer"])
call(["sudo", "systemctl", "enable", "simpleServer"])

# --------------------------------------------------------------------------
# Success.
#
print("%(prog)s exits with no errors.")
exit(0)

