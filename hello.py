#! /usr/bin/env python

import sys

def path_and_verison():
    print()
    print("Python path and verion: ")
    print(sys.executable)
    print(sys.version)
    print()

def add(x,y):
    return x + y

path_and_verison()
print(add(1,2))
