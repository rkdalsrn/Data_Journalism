import pandas as pd
import numpy as np

data1 = pd.read_excel('mingumingu.xlsx',sheet_name = '일반음식점_1')
data2 = pd.read_excel('mingumingu.xlsx',sheet_name = '일반음식점_2')
data3 = pd.read_excel('mingumingu.xlsx',sheet_name = '일반음식점_3')
data4 = pd.read_excel('mingumingu.xlsx',sheet_name = '일반음식점_4')
data5 = pd.read_excel('mingumingu.xlsx',sheet_name = '일반음식점_5')
data6 = pd.read_excel('mingumingu.xlsx',sheet_name = '일반음식점_6')
data7 = pd.read_excel('mingumingu.xlsx',sheet_name = '일반음식점_7')

strdata = ['단수이대왕카스테라', '따거대만카스테라', '정성대왕카스테라', '대만락카스테라', '스린대왕카스테라', '대왕통카스테라', '따호카스테라', '대만원미대왕카스테라']
mingu = []
mingu1 = []
for i in range(0, 47):
    mingu1.append(0)

def compareString(str, i, k):
    for i in range(0, len(str) - len(strdata[k]) + 1):
        mingu = ""
        for j in range(i, i + len(strdata[k])):
            mingu = mingu + str[j]
        if(strdata[k] == mingu):  return 1
        else:   return 0

for j in range(0, len(strdata)):
    for i in range(0, len(data1['사업장명'])):
        verify = compareString(data1['사업장명'][i], i, j)
        if(verify == 1):
            mingu.append(data1['인허가일자'][i])
    for i in range(0, len(data2['사업장명'])):
        verify = compareString(data2['사업장명'][i], i, j)
        if(verify == 1):
            mingu.append(data2['인허가일자'][i])
    for i in range(0, len(data3['사업장명'])):
        verify = compareString(data3['사업장명'][i], i, j)
        if(verify == 1):
            mingu.append(data3['인허가일자'][i])
    for i in range(0, len(data4['사업장명'])):
        verify = compareString(data4['사업장명'][i], i, j)
        if(verify == 1):
            mingu.append(data4['인허가일자'][i])
    for i in range(0, len(data5['사업장명'])):
        verify = compareString(data5['사업장명'][i], i, j)
        if(verify == 1):
            mingu.append(data5['인허가일자'][i])
    for i in range(0, len(data6['사업장명'])):
        verify = compareString(data6['사업장명'][i], i, j)
        if(verify == 1):
            mingu.append(data6['인허가일자'][i])
    for i in range(0, len(data7['사업장명'])):
        verify = compareString(data7['사업장명'][i], i, j)
        if(verify == 1):
            mingu.append(data7['인허가일자'][i])

for k in mingu:
    for i in range(2016, 2020):
        for j in range(1, 13):
            if(i * 10000 + j * 100 <= k <= i * 10000 + j * 100 + 31):
                mingu1[(i-2016)*12 + j - 1] = mingu1[(i-2016)*12 + j - 1] + 1
                
print(mingu1)
