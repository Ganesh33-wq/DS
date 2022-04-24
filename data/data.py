import pandas as pd
data=pd.read_csv(r'C:\Users\Sort\Desktop\data\JEOPARDY_CSV.csv')
from difflib import SequenceMatcher
import itertools
output=[]
def chk(q1):
    k=[]
    for i,j in itertools.product(q1,data['ques']):
        rat=SequenceMatcher(None, i, j).ratio()
        k.append((rat,j))
    k.sort(key = lambda x: x[1])
    output.append(k[-1])
    return k

for k in data['ques']:
    print(k)
    s=chk(k)
    break