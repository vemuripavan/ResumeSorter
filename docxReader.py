from ResumeReader import ResumeReader

from docx import Document

class docxReader(ResumeReader):
    #Method which will parse the docx file and return text
    def readResume(self,file):
        document = Document(file)
        return "\n".join([para.text for para in document.paragraphs])