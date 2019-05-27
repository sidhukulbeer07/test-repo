#!/usr/bin/env bash

echo "ArrDelay,Dest" > first3sfo.csv | cut -d',' -f15,17 flightdelays.csv | grep 'SFO' | head -3 >> first3sfo.csv

cat first3sfo.csv | csvlook
