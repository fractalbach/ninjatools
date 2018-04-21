#!/bin/bash
sudo python3 setupSystemd.py -f simpleServer.service
sudo systemctl daemon-reload
systemctl status simpleServer.service