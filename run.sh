#!/bin/bash
for f in src/*.py; do
    if [ "$f" != "src/main.py" ]; then
        cached_file="cached/$(basename $f)"
        if [ ! -f "$cached_file" ] || [ "$f" -nt "$cached_file" ]; then
            mpremote cp "$f" :
            cp "$f" "$cached_file"
        fi
    fi
done
mpremote run src/main.py