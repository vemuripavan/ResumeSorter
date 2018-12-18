from reader.readerfactory import ReaderFactory
#from ReaderFactory import ReaderFactory
from os import listdir
from os.path import isfile, join
from texttofeatureconverter import textToFeatureConverter

dir_cvs="D:\deep\SPAN\Shikhsa\AI\ML\kaggle\Data Science_Final project\Resumes\docx"


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
        
    
"""rs = ResumeSorter()
dir_cvs="D:\deep\SPAN\Shikhsa\AI\ML\kaggle\Data Science_Final project\Resumes\docx\Abhishek Kumar Singh_5.10_HCL_Azure_Delhi_N.docx"
file = open(dir_cvs)
resumelist = []
resumelist.append(file)
text_dic = rs.extracttext(resumelist)
"""

#featureConverter = textToFeatureConverter()
#featureConverter.getFeaturesFromText(file_list, text_list)


