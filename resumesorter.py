from feature import jdparser 
from feature import resumeparser 
from feature import textutil
from comparator import textcomparator

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
        textcomparator.fetchSimilarity(score_df, rdf, jdf)
        return score_df
        
        
    


"""
resumedir="D:\deep\SPAN\Shikhsa\AI\ML\kaggle\Data Science_Final project\Resumes\Business Analyst"
jdfile = "D:\deep\SPAN\Shikhsa\AI\ML\kaggle\Data Science_Final project\JD_One.xlsx"

jdf=jdparser.parsejd(jdfile)
file_list = resumeparser.getfiles(resumedir)
text_dic = resumeparser.extracttext(file_list)



rdf = resumeparser.extractfeatures(text_dic)

rdf =textutil.texttokenize('Resume_text','text_tok',rdf)
    
score_df = pd.DataFrame()
score_df["ResumeName"] = rdf["ResumeName"]
textcomparator.fetchSimilarity(score_df, rdf, jdf)


"""

#featureConverter = textToFeatureConverter()
#featureConverter.getFeaturesFromText(file_list, text_list)


