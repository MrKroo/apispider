#!/bin/bash

if [ -z $1 ]; then
    TIME=3600
else
    TIME=$1
fi

timeout $TIME /usr/bin/python3 apispider.py

sed -e 's/}$/},/' apispider.txt | head --bytes=-2 | sed -e '1s/^/\[/' | sed -e '$a\]' | sponge apispider.txt

/usr/bin/python3 gethighscore.py | grep github > github.gethighscore.txt
