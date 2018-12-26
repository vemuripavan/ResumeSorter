import pandas as pd
import numpy as np
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import gensim
from gensim import corpora
#import nltk
#nltk.download('stopwords')
from sklearn.metrics.pairwise import cosine_similarity as cs
from sklearn.metrics.pairwise import manhattan_distances as md
from sklearn.metrics.pairwise import euclidean_distances as ed

words = re.compile(r"\w+",re.I)
stopword = stopwords.words('english')
lemmatizer = WordNetLemmatizer()

# Read text from textcol and create tokcol with tokens in given df
def texttokenize(textcol, tokcol, df):   
    df[tokcol] = df[textcol].apply(lambda x: re.sub('[^a-zA-Z0-9]', ' ', x))
    df[tokcol] = df[tokcol].str.lower()            
    df[tokcol] = df[tokcol].apply(lambda x: [lemmatizer.lemmatize(item) for item in words.findall(x) if item not in stopword])
    return df


# Read text_tok from two data frame and create dictonary
def train_dictionary(df1,df2):
    documents = df1.text_tok.tolist() + df2.text_tok.tolist()
    dictionary = corpora.Dictionary(documents)
    #dictionary.filter_extremes(no_below=5, no_above=0.8)
    dictionary.compactify()
    return dictionary


def get_vectors(rdf,jdf, dictionary):
    
    resume_vec = [dictionary.doc2bow(text) for text in rdf.text_tok.tolist()]
    resume_csc = gensim.matutils.corpus2csc(resume_vec, num_terms=len(dictionary.token2id))
    
    jd_vec = [dictionary.doc2bow(text) for text in jdf.text_tok.tolist()]
    jd_csc = gensim.matutils.corpus2csc(jd_vec, num_terms=len(dictionary.token2id))
    
    return resume_csc.transpose(), jd_csc.transpose()

def get_similarity_values(res_csc, jd_csc):
    cosine_sim = []
    manhattan_dis = []
    eucledian_dis = []
    
    j= jd_csc
    for i in res_csc:
        sim = cs(i,j)
        cosine_sim.append(sim[0][0])
        sim = md(i,j)
        manhattan_dis.append(sim[0][0])
        sim = ed(i,j)
        eucledian_dis.append(sim[0][0])
        
    return cosine_sim, manhattan_dis, eucledian_dis  



"""from resumesorter import ResumeSorter
from texttofeatureconverter import textToFeatureConverter


rs = ResumeSorter()
dir_cvs="D:\deep\SPAN\Shikhsa\AI\ML\kaggle\Data Science_Final project\Resumes\Business Analyst"
resumelist = []
#resumelist.append(dir_cvs)
resumelist = rs.getfiles(dir_cvs)
text_dic = rs.extracttext(resumelist)
feature_df = rs.extractfeatures(text_dic)

jdfile = "D:\deep\SPAN\Shikhsa\AI\ML\kaggle\Data Science_Final project\JD_One.xlsx"
jddf = pd.read_excel(jdfile)



rdf = pd.DataFrame()
rdf["text"] = feature_df["Resume_text"]

jdf = pd.DataFrame()
jdf["text"] = jddf["High Level Job Description"]

rdf =texttokenize(rdf)
jdf =texttokenize(jdf)

dictionary = train_dictionary(rdf,jdf)
print ("No of words in the dictionary = %s" %len(dictionary.token2id))

res_csc, jd_csc = get_vectors(rdf,jdf, dictionary)
print(res_csc.shape)
print(jd_csc.shape)
cosine_sim, manhattan_dis, eucledian_dis = get_similarity_values(res_csc, jd_csc)
print(cosine_sim, manhattan_dis, eucledian_dis, jaccard_dis)

mapped=zip(jd_csc,*res_csc)
mapped = set(mapped) 

cosine_sim = []
for i in res_csc:
    sim = cs(i,jd_csc)
    cosine_sim.append(sim[0][0])
"""

