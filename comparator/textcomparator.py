from feature import textutil


# compare text_col from resume and jd data and add similarity score 
def fetchSimilarity(score_df, rdf, jdf):
    dictionary = textutil.train_dictionary(rdf,jdf)
    print ("No of words in the dictionary = %s" %len(dictionary.token2id))
    res_csc, jd_csc = textutil.get_vectors(rdf,jdf, dictionary)
    #print(res_csc.shape)
    #print(jd_csc.shape)
    cosine_sim, manhattan_dis, eucledian_dis = textutil.get_similarity_values(res_csc, jd_csc)
    score_df['text_score'] = cosine_sim

