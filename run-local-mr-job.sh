#!/usr/bin/env bash

START_TIME=$(date -u +%s)

python ./map_reduce.py -r local --database=./db/GeoLite2-Country.mmdb ./data/log_$1.csv

DURATION="$(($(date -u +%s)-$START_TIME))"
echo "Total of $DURATION seconds elapsed for process"