import numpy as np
import pandas as pd
import lib4 as lb

print("skriv in ett namn på csv fil som ska laddas")
tempname=input()
tempname="data.csv"
df =pd.read_csv(tempname)
df.fillna(0, inplace = True)
z=0
k=0
for k in range(k,len(df.loc[0])):
    if isinstance(df.iloc[0, k], str)== True:           #data kan inte och skall inte röras
        print("Not used")
    else:                                               #datan kan normaliseras och skall normaliseras

        for z in range(z,len(df.iloc[:,0])):
            df.iloc[z,k]= lb.minmaxnorm(df.iloc[z,k], df.iloc[:,k].min(), df.iloc[:,k].max())


        z=0

print("Vad skall den nya filen heta?")
tempname=input()

df.to_csv(tempname,index=False)