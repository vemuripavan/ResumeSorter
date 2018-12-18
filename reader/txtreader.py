from .resumereader import ResumeReader

class TxtReader(ResumeReader):
    #Method which will parse the docx file and return text
    def readResume(self,file):
        f = open(file,'r')
        lines = f.readlines()
        #todo : shall we close the file?
        return "\n".join(lines)