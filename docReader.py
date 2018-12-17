from ResumeReader import ResumeReader

from win32com.client import Dispatch
import os


class docReader(ResumeReader):
    #Method which will parse the docx file and return text
    def readResume(self,file):
        wordapp = Dispatch("Word.Application")
        doc = wordapp.Documents.Open(os.path.normcase(file))
        #doc = app.Documents.Open(fullpath)
        docText = doc.Content.Text
        wordapp.Quit()
        return docText