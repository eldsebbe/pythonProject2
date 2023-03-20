import numpy as np
import pandas as pd



def minmaxnorm(a,mines,maxes):              #tar in alla värden i en collumn av ints och skickar tillbaka V=(x-min)/(max-min)
                                            #först hitta minsta samt största värdet min och max
    b =(a-mines)/(maxes-mines)
    return b