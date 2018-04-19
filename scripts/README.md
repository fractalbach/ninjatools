# Random Scripts

This folder contains various scripts that I've found useful.
Usually to automate either mundane tasks, or tasks that are more safely
handled by a computer than a human.


## GoGetGo.sh and gogetgo.py

Bash
- Downloads and installs [The Go Programming Language](https://golang.org/).
- Very simple, without many features
- Designed for usage on a freshly created linux os.
- BUGGY, path configuration is hacky. 

Python (TODO)
- A better version of the above bash script.
- configures paths correctly.
- Best used on a fresh virtual machine.
- Will try to figure out how to configure environment variables based on the OS.
- Will try to update Go if there is a new version.
- Will try to not have side effects if run on a system where Go is already configured.
- Optionally, will reconfigure environment if Go is installed, but is not configured correctly.



## setupSystemd.py

`setupSystemd.py` makes it easier to automatically place `.service` files in the 
correct directory and to start/stop that service.  The Use-Case in mind is to 
automate the process of configuring a server on a freshly created virtual machine.


Current Features
- Designed for usage with [simpleServer](https://github.com/fractalbach/ninjatools/tree/master/simpleServer).
- Writes a `.service` file to the directory `/etc/systemd/system/`
- Attempts to both start the service, and enable it.


Future Features
- will be designed to work well with updating the same service.
- check the status of the services.
- stops and disables current service of the same name.
- will use a separate `.service` file, which you can specify the location of with a flag.