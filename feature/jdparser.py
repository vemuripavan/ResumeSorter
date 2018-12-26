# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 12:40:05 2018

@author: surya.k
"""

import pandas as pd
from feature import textutil

# Read JD file (having only one profile) and provide Exp, Skils_Tech, job_desc
def parsejd(jdfile):
    jddata = pd.read_excel(jdfile)
    jddata.info()
    jd_info = jddata[['Yrs Of Exp ','Primary Skill','High Level Job Description']]
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
    jd_info['Required Skill'] = updated_sk_list
    
    jd_info =textutil.texttokenize('High Level Job Description','text_tok',jd_info)
    
    jd_info.rename(columns={'Yrs Of Exp ': 'Exp', 'Required Skill': 'Skills_Tech',
                       'High Level Job Description':'Job_Desc'}, inplace=True)
    
    return jd_info