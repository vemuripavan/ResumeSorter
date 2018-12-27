from feature import jdparser 
from feature import resumeparser 
from feature import textutil
from comparator import textcomparator, skillscomparator

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
        return score_df
        
    

# Code for Unit Testing
"""
resumedir="D:\deep\SPAN\Shikhsa\AI\ML\kaggle\Data Science_Final project\Resumes\Business Analyst"
jdfile = "D:\deep\SPAN\Shikhsa\AI\ML\kaggle\Data Science_Final project\JD_BA.xlsx"

jdf=jdparser.parsejd(jdfile)
file_list = resumeparser.getfiles(resumedir)
text_dic = resumeparser.extracttext(file_list)



rdf = resumeparser.extractfeatures(text_dic)

rdf =textutil.texttokenize('Resume_text','text_tok',rdf)
    
score_df = pd.DataFrame()
score_df["ResumeName"] = rdf["ResumeName"]
textcomparator.fetchSimilarity(score_df, rdf, jdf)


requiredSkills = jdf.iloc[0]['Skills_Tech']
resumes = rdf['Resume_text']
skills_count=len(requiredSkills)
max_count = 3 # If occurance of a skill in reume is 3, then give it full score
skillscore={}

import re
skills_score = []
for resumeText,resumeName in zip(rdf['Resume_text'],rdf['ResumeName']):
    skillscore={}
    for skill in requiredSkills:
        if skill in resumeText:
            ocurrance_count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(skill), resumeText))
            #print(ocurrance_count)
            score = int(ocurrance_count)/max_count
            score = 1 if score>=1 else score
            score = score*(1/skills_count)
            #print(score)
            skillscore[skill]= score
        else:
            skillscore[skill]= 0
    print(resumeName,':',sum(skillscore.values()))
    skills_score.append(sum(skillscore.values()))

 
score_df['SkillTech_Score'] = skills_score


"""

#featureConverter = textToFeatureConverter()
#featureConverter.getFeaturesFromText(file_list, text_list)


