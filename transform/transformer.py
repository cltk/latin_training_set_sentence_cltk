import os
import re

root = os.path.abspath('./')
orig = os.path.join(root,'original/')
files = os.listdir(orig)
for file in files:
    with open(orig + file) as f:
        r = f.read()
        #readlines
        #lines = f.readlines()
        #lines = lines[:-3]
        #print(str(lines[1:22]))

        n = re.sub(r'([a-z]+)(\.|;|\?)\s([\w]+)', r'\1\2\n\3', r)
        d = re.sub(r'\[.+\]', r'', n)
        print(d)