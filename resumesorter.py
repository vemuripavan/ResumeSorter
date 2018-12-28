from feature import jdparser 
from feature import resumeparser 
from feature import textutil
from comparator import textcomparator, skillscomparator, expcomparator

import pandas as pd


class ResumeSorter():

    ## Create three variables for weightage to 
    """
    Experience: 60%
    Skills : 25%
    Job Description: 15%

    """


    def sortResumes(self, jdfile,resumedir):
        #resumedir="D:\deep\SPAN\Shikhsa\AI\ML\kaggle\Data Science_Final project\Resumes\Business Analyst"
        #jdfile = "D:\deep\SPAN\Shikhsa\AI\ML\kaggle\Data Science_Final project\JD_One.xlsx"

        jdf=jdparser.parsejd(jdfile)
        file_list = resumeparser.getfiles(resumedir)
        text_dic = resumeparser.extracttext(file_list)
        rdf = resumeparser.extractfeatures(text_dic)
        rdf =textutil.texttokenize('Resume_text','text_tok',rdf)
        score_df = pd.DataFrame()
        score_df["ResumeName"] = rdf["ResumeName"]
        score_df["ResmueEXP"] = rdf["Exp"]
        textcomparator.fetchSimilarity(score_df, rdf, jdf)
        skillscomparator.compareSkills(score_df, rdf, jdf)
        expcomparator.compareExp(score_df, rdf, jdf)
        return score_df
        
    

# Code for Unit Testing
"""
resumedir="D:\deep\SPAN\Shikhsa\AI\ML\kaggle\Data Science_Final project\Resumes\Sharepoint"
jdfile = "D:\deep\SPAN\Shikhsa\AI\ML\kaggle\Data Science_Final project\JD_SP.xlsx"

jdf=jdparser.parsejd(jdfile)
file_list = resumeparser.getfiles(resumedir)
text_dic = resumeparser.extracttext(file_list)
rdf = resumeparser.extractfeatures(text_dic)
rdf =textutil.texttokenize('Resume_text','text_tok',rdf)
    
score_df = pd.DataFrame()
score_df["ResumeName"] = rdf["ResumeName"]
textcomparator.fetchSimilarity(score_df, rdf, jdf)
skillscomparator.compareSkills(score_df, rdf, jdf)
expcomparator.compareExp(score_df, rdf, jdf)


jdf['Exp'][0] = clearExp(jdf['Exp'][0])


import numpy as np
jd_exp = jdf.iloc[0]['Exp']
rd_exp = rdf['Exp']


exp_score = []
jdexp = jd_exp
exp_score = []
if isinstance(jdexp,np.int64):
    for rsexp in rd_exp:
        if isinstance(rexp,int):
            exp_score.append(compare_exp(jdexp,rsexp))
        else:
            exp_score.append(0)
elif isinstance(jd_exp,list):
    for rsexp in rd_exp:
        if isinstance(rsexp,int):
            
            exp_score.append(compare_exp_range(jdexp,rsexp))
        else:
            exp_score.append(0)


    

skills_score = []
for resumeText in resumes:
    skillscore={}
    for skill in requiredSkills:
        if skill in resumeText:
            ocurrance_count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(skill), resumeText))
            score = int(ocurrance_count)/max_count
            score = 1 if score>=1 else score
            score = score*(1/skills_count)
            #print(score)
            skillscore[skill]= score
        else:
            skillscore[skill]= 0
    skills_score.append(sum(skillscore.values()))   

score_df['exp_Score'] = exp_score
"""

#featureConverter = textToFeatureConverter()
#featureConverter.getFeaturesFromText(file_list, text_list)


