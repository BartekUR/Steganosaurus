#!/bin/bash

[[ $# != 1 ]] && echo "Podaj dokladnie jeden argument!\n"

python2 ~/.claws-mail/python-scripts/tools/unistego.git/unistego-tool --unhide --preset joiners $1

echo
