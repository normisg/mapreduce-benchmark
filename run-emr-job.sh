#!/usr/bin/env bash

START_TIME=$(date -u +%s)

python ./map_reduce.py -r emr --instance-type c1.medium --num-core-instances 4 --database=./db/GeoLite2-Country.mmdb ./data/log_$1.csv > results/emr_result.txt

DURATION="$(($(date -u +%s)-$START_TIME))"
echo "Total of $DURATION seconds elapsed for process"