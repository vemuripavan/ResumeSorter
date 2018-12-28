from .docxreader import DocxReader
from .pdfreader import PDFReader
from .docreader import DocReader
from .rtfreader import RTFReader
from .txtreader import TxtReader
import os

class ReaderFactory:
    @staticmethod
    def createReader(file):
        #TODO: What if file extn is not in the given list
        name, ext = os.path.splitext(file)
        ext = ext.lower()
        if ext =='.docx':
            return DocxReader()
        elif ext =='.doc':
            return DocReader()
        elif ext =='.pdf':
            return PDFReader()
        elif ext =='.rtf':
            return RTFReader()
        elif ext =='.text' or ext =='.txt':
            return TxtReader()