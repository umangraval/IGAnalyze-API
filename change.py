#!/usr/bin/python
import fileinput
import os

try:
    with fileinput.FileInput('/app/.heroku/python/lib/python3.7/site-packages/firebase/__init__.py', inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('.async', '.assync'), end='')

    with fileinput.FileInput('/app/.heroku/python/lib/python3.7/site-packages/firebase/firebase.py', inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace('.async', '.assync'), end='')

    os.rename('/app/.heroku/python/lib/python3.7/site-packages/firebase/async.py', '/app/.heroku/python/lib/python3.7/site-packages/firebase/assync.py')
except:
    print('Already Fixed')
