#!/usr/bin/env python
#stop the server

import os
import signal
import json
folder = os.path.dirname(os.path.abspath(__file__))
os.chdir("/tmp")

try:
    _file = open("singpath_pids","r")
    content = _file.read()
    _file.close()
    pid = json.loads(_file.read().strip())
except:
    pid = {}

try:
    os.kill(int(pid["java"]),signal.SIGKILL)
    os.kill(int(pid["python"]),signal.SIGKILL)
except:
    pass

os.popen("fuser -k 80/tcp").read()
os.popen("fuser -k 2012/tcp").read()

print " Server closed"
