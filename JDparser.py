# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 12:40:05 2018

@author: surya.k
"""


import pandas as pd
excelsheet = pd.read_excel("D:/ML_Projects/FinalProject/JD.xlsx")
excelsheet.info()
req_info = excelsheet[["Job Title","Yrs Of Exp ","Primary Skill"]]
primarySkillSeries = req_info["Primary Skill"]
x = primarySkillSeries.str.split("--",expand=True)
y = x[0]
skill_list = y.values.tolist()


updated_sk_list = []
for i in skill_list:
    if (',' in i ):
        j = i.split(',')
        updated_sk_list.append(j)
    elif('&' in i):
        j = i.split('&')
        updated_sk_list.append(j)
    elif('-' in i):
        j = i.split('-')
        updated_sk_list.append(j)
    else:
        j = [i]
        updated_sk_list.append(j)

