import abc

class ResumeReader(metaclass=abc.ABCMeta):
    #Method which will parse the file and return text
    @abc.abstractmethod
    def readResume(self,file):
        pass