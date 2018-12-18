# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 12:40:05 2018

@author: surya.k
"""


import pandas as pd




def parsejd(jdfile):
    jddata = pd.read_excel(jdfile)
    jddata.info()
    jd_info = jddata[["Job Title","Yrs Of Exps","Qualification","Primary Skill"]]
    primarySkillSeries = jd_info["Primary Skill"]
    
    
    
    
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
            
    jd_info.drop(['Primary Skill'], inplace = True, axis = 1)
    jd_info.insert(3,'Required Skill',updated_sk_list)
    
    return jd_info

