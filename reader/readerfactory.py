from .docxreader import DocxReader
from .pdfreader import PDFReader
from .docreader import DocReader
from .rtfreader import RTFReader
from .txtreader import TxtReader
import os

class ReaderFactory:
    @staticmethod
    def createReader(file):
        name, ext = os.path.splitext(file)
        #Todo we need take care of uper/lowe case also
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