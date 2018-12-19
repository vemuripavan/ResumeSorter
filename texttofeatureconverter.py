import nltk, re
class textToFeatureConverter:
    
    information=[]
    inputString = ''
    tokens = []
    lines = []
    sentences = []
    
    def getFeaturesFromText(self, text):
        self.preprocess(text)
        self.tokenize(text)
        return self.getEmail(text), self.getPhone(text), self.getExperience(text)
            
    def preprocess(self, document):
        '''
        Information Extraction: Preprocess a document with the necessary POS tagging.
        Returns three lists, one with tokens, one with POS tagged lines, one with POS tagged sentences.
        Modules required: nltk
        '''
        try:
            # Try to get rid of special characters
            try:
                document = document.decode('ascii', 'ignore')
            except:
                document = document.encode('ascii', 'ignore')
            # Newlines are one element of structure in the data
            # Helps limit the context and breaks up the data as is intended in resumes - i.e., into points
            lines = [el.strip() for el in document.split("\n") if len(el) > 0]  # Splitting on the basis of newlines 
            lines = [nltk.word_tokenize(el) for el in lines]    # Tokenize the individual lines
            lines = [nltk.pos_tag(el) for el in lines]  # Tag them
            # Below approach is slightly different because it splits sentences not just on the basis of newlines, but also full stops 
            # - (barring abbreviations etc.)
            # But it fails miserably at predicting names, so currently using it only for tokenization of the whole document
            sentences = nltk.sent_tokenize(document)    # Split/Tokenize into sentences (List of strings)
            sentences = [nltk.word_tokenize(sent) for sent in sentences]    # Split/Tokenize sentences into words (List of lists of strings)
            tokens = sentences
            sentences = [nltk.pos_tag(sent) for sent in sentences]    # Tag the tokens - list of lists of tuples - each tuple is (<word>, <tag>)
            # Next 4 lines convert tokens from a list of list of strings to a list of strings; basically stitches them together
            dummy = []
            for el in tokens:
                dummy += el
            tokens = dummy
            # tokens - words extracted from the doc, lines - split only based on newlines (may have more than one sentence)
            # sentences - split on the basis of rules of grammar
            return tokens, lines, sentences
        except Exception as e:
            print(e)
    
    def tokenize(self, inputString):
        try:
            self.tokens, self.lines, self.sentences = self.preprocess(inputString)
            return self.tokens, self.lines, self.sentences
        except Exception as e:
            print(e)
    
    #Given an input string, returns possible matches for emails.
    def getEmail(self, inputString): 
        email = None
        try:
            pattern = re.compile(r'\S*@\S*')
            matches = pattern.findall(inputString) # Gets all email addresses as a list
            email = matches
        except Exception as e:
            print(e)
        return email
    
    #Given an input string, returns possible matches for phone numbers.
    def getPhone(self, inputString):
        number = None
        try:
            pattern = re.compile(r'([+(]?\d+[)\-]?[ \t\r\f\v]*[(]?\d{2,}[()\-]?[ \t\r\f\v]*\d{2,}[()\-]?[ \t\r\f\v]*\d*[ \t\r\f\v]*\d*[ \t\r\f\v]*)')
                # Understanding the above regex
                # +91 or (91) -> [+(]? \d+ -?
                # Metacharacters have to be escaped with \ outside of character classes; inside only hyphen has to be escaped
                # hyphen has to be escaped inside the character class if you're not incidication a range
                # General number formats are 123 456 7890 or 12345 67890 or 1234567890 or 123-456-7890, hence 3 or more digits
                # Amendment to above - some also have (0000) 00 00 00 kind of format
                # \s* is any whitespace character - careful, use [ \t\r\f\v]* instead since newlines are trouble
            match = pattern.findall(inputString)
            # match = [re.sub(r'\s', '', el) for el in match]
                # Get rid of random whitespaces - helps with getting rid of 6 digits or fewer (e.g. pin codes) strings
            # substitute the characters we don't want just for the purpose of checking
            match = [re.sub(r'[,.]', '', el) for el in match if len(re.sub(r'[()\-.,\s+]', '', el))>6]
                # Taking care of years, eg. 2001-2004 etc.
            match = [re.sub(r'\D$', '', el).strip() for el in match]
                # $ matches end of string. This takes care of random trailing non-digit characters. \D is non-digit characters
            match = [el for el in match if len(re.sub(r'\D','',el)) <= 15]
                # Remove number strings that are greater than 15 digits
            try:
                for el in list(match):
                    # Create a copy of the list since you're iterating over it
                    if len(el.split('-')) > 3: continue # Year format YYYY-MM-DD
                    for x in el.split("-"):
                        try:
                            # Error catching is necessary because of possibility of stray non-number characters
                            # if int(re.sub(r'\D', '', x.strip())) in range(1900, 2100):
                            if x.strip()[-4:].isdigit():
                                if int(x.strip()[-4:]) in range(1900, 2100):
                                    # Don't combine the two if statements to avoid a type conversion error
                                    match.remove(el)
                        except:
                            pass
            except:
                pass
            number = match
        except:
            pass
        return number
    
    def getExperience(self,inputString):
        experience=[]
        try:
            for sentence in self.lines:#find the index of the sentence where the degree is find and then analyse that sentence
                    sen=" ".join([words[0].lower() for words in sentence]) #string of words in sentence
                    if re.search('experience',sen):
                        sen_tokenised= nltk.word_tokenize(sen)
                        tagged = nltk.pos_tag(sen_tokenised)
                        entities = nltk.chunk.ne_chunk(tagged)
                        for subtree in entities.subtrees():
                            for leaf in subtree.leaves():
                                if leaf[1]=='CD':
                                    experience=leaf[0]
        except Exception as e:
            print (e)
        return experience
