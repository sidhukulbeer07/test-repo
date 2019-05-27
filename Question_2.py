#!/usr/bin/env python3

import pandas as pd
import numpy as np

print("Hello")

df = pd.read_csv("flightdelays.csv")

print("data frame loaded")

top3SFO = df[['ArrDelay','Origin']]

top3SFO = top3SFO[top3SFO['Origin']== 'SFO'].head(3)

top3SFO.to_csv('first3SFO.csv',index=false)

print("first3SFO.csv created")

print("============Part2============")

Print("Top 3 Destination")

print(df['Dest'].value_counts().head(3))




