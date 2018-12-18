from .resumereader import ResumeReader

from win32com.client import Dispatch
import pythoncom
import os


class DocReader(ResumeReader):
    #Method which will parse the docx file and return text
    def readResume(self,file):
        # You need to call CoInitialize() in order to use win32com.client to use this some other process
        pythoncom.CoInitialize()
        wordapp = Dispatch("Word.Application")
        doc = wordapp.Documents.Open(os.path.normcase(file))
        #doc = app.Documents.Open(fullpath)
        docText = doc.Content.Text
        wordapp.Quit()
        return docText