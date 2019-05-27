#!/usr/bin/env bash

cut -d',' -f18 flightdelays.csv | sort | uniq -c | sort -r -n | head -3 |  tee -a Top_3_dest.csv

cat Top_3_dest.csv | csvlook
Kulbeer Singh
