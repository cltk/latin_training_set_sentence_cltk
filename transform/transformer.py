import os
import re

root = os.path.abspath('./')

orig = os.path.join(root,'original/')

files = os.listdir(orig)

for file in files:
    with open(orig + file) as f:
        r = f.read()
        print(r)