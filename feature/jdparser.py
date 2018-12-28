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
    jd_info = jddata[['Yrs Of Exp ','Primary Skill','High Level Job Description','Technology']]
    
    skillAndTech= jd_info.iloc[0]['Primary Skill'] + ", " +  jd_info.iloc[0]['Technology']
    skillAndTechValues = skillAndTech.lower().split("--")
    jd_info['Skills_Tech'] = prepareSkillTechList(skillAndTechValues)
        
    jd_info =textutil.texttokenize('High Level Job Description','text_tok',jd_info)
    jd_info.rename(columns={'Yrs Of Exp ': 'Exp',
                       'High Level Job Description':'Job_Desc'}, inplace=True)
    
    jd_info['Exp'][0] = clearExp(jd_info['Exp'][0])
    jd_info.drop(['Primary Skill','Technology'], inplace = True, axis = 1)
    return jd_info

def prepareSkillTechList(skilltechvalueslist):
    skilltechvalues = []
    z = ['None' if v is None else v for v in skilltechvalueslist]
    z1 = list(set(z))
    if 'None' in z1:
        z1.remove('None')
    j = ' '.join(z1)
    if "expert" in j:
        j = j.replace("expert",' ')
    if "master" in j:
        j = j.replace("master",' ')
    if "," in j:
        j = j.replace(",",' ')
    if "&" in j:
        j = j.replace("&",' ')        
    j = j.split(" ")
    j1 = list(set(j))
    j1.remove("")
    skilltechvalues.append(j1)
        
    return skilltechvalues

def clearExp(jd_exp):
    if isinstance(jd_exp,str):
        jd_exp = jd_exp.lower()
        jd_exp = jd_exp.strip()
        jd_exp = jd_exp.replace(" ", "")
        if '-' in jd_exp:
            jd_exp = [int(x) for x in jd_exp.split("-")]
        elif 'to' in jd_exp:
            jd_exp = [int(x) for x in jd_exp.split("to")]
    return jd_exp




# Code for Unit Testing
"""jdfile = "D:\deep\SPAN\Shikhsa\AI\ML\kaggle\Data Science_Final project\JD_BA.xlsx"
jddata = pd.read_excel(jdfile)
jddata.info()
jd_info = jddata[['Yrs Of Exp ','Primary Skill','High Level Job Description','Technology']]

skillAndTech= jd_info.iloc[0]['Primary Skill'] + ", " +  jd_info.iloc[0]['Technology']
skillAndTechValues = skillAndTech.lower().split("--")
skillAndTechValuesLIST = prepareSkillTechList(skillAndTechValues)
"""