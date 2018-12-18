from .resumereader import ResumeReader
from docx import Document
import xml.dom.minidom

class DocxReader(ResumeReader):
    #Method which will parse the docx file and return text
    def readResume(self,file):
        document = Document(file)
        content = []
        
        headers = [x.blob.decode() for x in document.part.package.parts if x.partname.find('header')>0]
        for header in headers:        
            content = self.getChildText(xml.dom.minidom.parseString(header))
            
        footers = [x.blob.decode() for x in document.part.package.parts if x.partname.find('footer')>0]
        for footer in footers:        
            content = content + self.getChildText(xml.dom.minidom.parseString(footer))
        
        content = content + [para.text for para in document.paragraphs]
        return "\n".join(content)
    
    def getChildText(self, node):
        items = []
        if node.hasChildNodes:
            for cn in node.childNodes:
                items = items + self.getChildText(cn)
        if node.nodeValue  is not None: 
            items.append(node.nodeValue)
        return items