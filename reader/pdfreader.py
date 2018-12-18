from .resumereader import ResumeReader
"""from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage"""
import io

class PDFReader(ResumeReader):
    #Method which will parse the docx file and return text
    def readResume(self,file):        
        """pagenums = set()   
        manager = PDFResourceManager() 
        codec = 'utf-8'
        caching = True

        output = io.StringIO()
        converter = TextConverter(manager, output, codec=codec, laparams=LAParams()) 

        interpreter = PDFPageInterpreter(manager, converter)   
        infile = open(file, 'rb')

        for page in PDFPage.get_pages(infile, pagenums,caching=caching, check_extractable=True):
            interpreter.process_page(page)

        convertedPDF = output.getvalue()  
        #print(convertedPDF)
        infile.close(); converter.close(); output.close()"""
        return 'Problem in reading pdf file'