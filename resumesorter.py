from reader.readerfactory import ReaderFactory
from os import listdir
from os.path import isfile, join, basename
from texttofeatureconverter import textToFeatureConverter
import pandas as pd


class ResumeSorter():

    """# Read all files from the given directory and it will check sub-directory also
    def getfiles(self,resumedir):
        file_list = []
        if isfile(resumedir):
                #print(f)
                file_list.append(resumedir)
        else:
            for f in listdir(resumedir):
                if isfile(f):
                    #print(f)
                    file_list.append(f)
                else:
                    file_list.append(self.getfiles(resumedir+'\\'+f))
        return file_list"""
    
    # Read all files from the given directory
    def getfiles(self,resumedir):
        file_list = []
        if isfile(resumedir):
                file_list.append(resumedir)
        else:
            for f in listdir(resumedir):
                if isfile(join(resumedir,f)):
                    file_list.append(join(resumedir,f))
        return file_list
    
    # Extract the text from list of files and retun a dictionary
    def extracttext(self,file_list):
        filedic={}
        for path in file_list:
            parser = ReaderFactory.createReader(path)
            filedic[path] =parser.readResume(path)
        return filedic
    
    # Extract the featurs in dataframe object
    def extractfeatures(self,filedic):
        feature_df= pd.DataFrame(columns=('Resume', 'Email', 'Phone', 'Exp' ,'Resume_text'))
        for key,value in filedic.items():
            textconverter = textToFeatureConverter()
            email, phn, exp  = textconverter.getFeaturesFromText(value)
            feature_df= feature_df.append({'Resume':key, 'Email':email, 'Phone': phn,'Exp':exp,'Resume_text':value},ignore_index=True)
        return feature_df
        
    
"""
rs = ResumeSorter()
dir_cvs="D:\deep\SPAN\Shikhsa\AI\ML\kaggle\Data Science_Final project\Resumes\docx\Abhishek Kumar Singh_5.10_HCL_Azure_Delhi_N.docx"
resumelist = []
resumelist.append(dir_cvs)
text_dic = rs.extracttext(resumelist)
text = text_dic[dir_cvs]
textconverter = textToFeatureConverter()
email, phn, exp  = textconverter.getFeaturesFromText(text)
feature_df= pd.DataFrame(columns=('Resume', 'Email', 'Phone' ,'Resume_text'))
feature_df= feature_df.append({'Resume':dir_cvs, 'Email':email, 'Phone': phn,'Resume_text':text},ignore_index=True)

"""

#featureConverter = textToFeatureConverter()
#featureConverter.getFeaturesFromText(file_list, text_list)


