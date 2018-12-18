from ResumeReader import ResumeReader
from striprtf.striprtf import rtf_to_text
from pathlib import Path

class rtfReader(ResumeReader):
    #Method which will parse the rtf file and return text
    def readResume(self,file):
        rtf_path = Path(file)
        with rtf_path.open() as source:
            return rtf_to_text(source.read()) 