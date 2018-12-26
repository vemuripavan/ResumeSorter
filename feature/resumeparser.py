from reader.readerfactory import ReaderFactory
from os import listdir
from os.path import isfile, join, basename
from .featureconverter import FeatureConverter
import pandas as pd


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
def getfiles(resumedir):
    file_list = []
    if isfile(resumedir):
            file_list.append(resumedir)
    else:
        for f in listdir(resumedir):
            if isfile(join(resumedir,f)):
                file_list.append(join(resumedir,f))
    return file_list

# Extract the text from list of files and retun a dictionary
def extracttext(file_list):
    filedic={}
    for path in file_list:
        parser = ReaderFactory.createReader(path)
        filedic[path] =parser.readResume(path)
    return filedic

# Extract the featurs in dataframe object
def extractfeatures(filedic):
    feature_df= pd.DataFrame(columns=('ResumeName', 'Email', 'Phone', 'Exp' ,'Resume_text'))
    for key,value in filedic.items():
        featureConverter = FeatureConverter()
        email, phn, exp  = featureConverter.getFeaturesFromText(value)
        feature_df= feature_df.append({'ResumeName':basename(key), 'Email':email, 'Phone': phn,'Exp':exp,'Resume_text':value},ignore_index=True)
    return feature_df
