from feature import textutil
import numpy as np

max_var = 1 # maximum variance in experience which we can consider
var_score = 0.9 # Score for the variance in the experience


# Compare the JD experience X with Candidate experience Y
def compareExp(score_df, rdf, jdf):
    
    jdexp = jdf.iloc[0]['Exp']
    r_exp = rdf['Exp']
    exp_score = []
    if isinstance(jdexp,np.int64):
        for rsexp in r_exp:
            if isinstance(rsexp,int):
                exp_score.append(compare_exp(jdexp,rsexp))
            else:
                exp_score.append(0)
    elif isinstance(jdexp,list):
        for rsexp in r_exp:
            if isinstance(rsexp,int):
                
                exp_score.append(compare_exp_range(jdexp,rsexp))
            else:
                exp_score.append(0)
                
    score_df['Exp_Score'] = exp_score

    
    
def compare_exp(jdexp,rsexp):
    if rsexp>jdexp:
        score = var_score if rsexp<=jdexp+max_var else 0
    elif rsexp<jdexp:
        score = var_score if rsexp>=jdexp-max_var else 0
    else:
        score =1
    return score
    
def compare_exp_range(jdexp,rsexp):
    min_jdexp = jdexp[0]
    max_jdexp = jdexp[1]
    if rsexp>max_jdexp:
        score = var_score if rsexp<=max_jdexp+max_var else 0
    elif rsexp<min_jdexp:
        score = var_score if rsexp>=min_jdexp-max_var else 0
    else:
        score =1
    return score