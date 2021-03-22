#!/usr/bin/env bash
# set -x
today="day$(date +'%d')"

echo "Making directory for $today"
mkdir "$today"
# cd "$today"

cp templates/day.py "${today}/${today}.py"
cp templates/test_day.py "${today}/test_${today}.py"

echo "Making new script ${today}.py"

chmod +x ${today}/*.py
