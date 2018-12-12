from ReaderFactory import ReaderFactory
#from ResumeReader import ResumeReader
from os import listdir
from os.path import isfile, join

dir_cvs="D:\deep\SPAN\Shikhsa\AI\ML\kaggle\Data Science_Final project\Resumes\docx"

file_list=[]
def read_All_CV(dir_cvs,file_list):
    if isfile(dir_cvs):
            #print(f)
            file_list.append(dir_cvs)
    else:
        for f in listdir(dir_cvs):
            if isfile(f):
                #print(f)
                file_list.append(f)
            else:
                read_All_CV(dir_cvs+'\\'+f,file_list)
    return file_list

read_All_CV(dir_cvs,file_list)

text_list=[]
for path in file_list:
    parser = ReaderFactory.createReader(path)
    text_list.append( parser.readResume(path))


