from docxReader import docxReader
from pdfReader import pdfReader
from docReader import docReader
from rtfReader import rtfReader
from txtReader import txtReader
import os

class ReaderFactory:
    @staticmethod
    def createReader(file):
        name, ext = os.path.splitext(file)
        #Todo we need take care of uper/lowe case also
        if ext =='.docx':
            return docxReader()
        elif ext =='.doc':
            return docReader()
        elif ext =='.pdf':
            return pdfReader()
        elif ext =='.rtf':
            return rtfReader()
        elif ext =='.text' or ext =='.txt':
            return txtReader()