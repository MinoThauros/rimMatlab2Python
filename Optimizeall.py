from sympy import interpolate
from plots import Data
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import math

nv = 50

def cleaner(data:pd.DataFrame):
    df= data[data['Vds'] != 0]
    return df
    
data=Data()

IdVg1=pd.DataFrame(abs(data.data2Output30V()))
Vg1max= max(IdVg1['Ids'])
Vg1min=min(IdVg1['Ids'])


Vv=pd.DataFrame(columns=['one','two','three','four','five'])
Id=pd.DataFrame(columns=['one','two','three','four','five'])
Vv['one']=np.linspace(Vg1min,Vg1max,nv+1) #add plus one to get 50 elements
Id['one'] = np.log10(np.interp(IdVg1['Ids'],Vv['one'],IdVg1['Vds']))
print(Id)