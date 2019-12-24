import os
import sys

n = sys.argv[1]

for i in range(n):
    if(os.path.isfile('commit_file')):
        os.system('del commit_file')
        os.system('git add .')
        os.system('git commit -m "deleted commit_file')
        os.system('git push')
    else:
        open('commit_file', 'r').close()
        os.system('git add .')
        os.system('git commit -m "added commit_file')
        os.system('git push')
