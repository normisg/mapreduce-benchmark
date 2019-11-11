#!/usr/bin/env bash

START_TIME=$(date -u +%s)

python ./simple.py data/log_$1.csv > results/simple_result.txt

DURATION="$(($(date -u +%s)-$START_TIME))"
echo "Total of $DURATION seconds elapsed for process"