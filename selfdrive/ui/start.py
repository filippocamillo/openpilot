#!/usr/bin/env python3
import os

assert os.system("make") == 0
os.environ['LD_LIBRARY_PATH'] = "/system/lib64:"+os.environ['LD_LIBRARY_PATH']
os.execv("./ui", ["ui"])

