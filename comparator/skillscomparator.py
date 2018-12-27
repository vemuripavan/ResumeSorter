from feature import textutil
import re


# Check the list of all skills&Tech from JD in the Resume_word_list
def compareSkills(score_df, rdf, jdf):
    
    requiredSkills = jdf.iloc[0]['Skills_Tech']
    resumes = rdf['Resume_text'].str.lower()
    skills_count=len(requiredSkills)
    max_count = 3 # If occurance of a skill in reume is 3, then give it full score

    skills_score = []
    for resumeText in resumes:
        skillscore={}
        for skill in requiredSkills:
            if skill in resumeText:
                ocurrance_count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(skill), resumeText))
                score = int(ocurrance_count)/max_count
                score = 1 if score>=1 else score
                score = score*(1/skills_count)
                #print(score)
                skillscore[skill]= score
            else:
                skillscore[skill]= 0
        skills_score.append(sum(skillscore.values()))    
     
    score_df['SkillTech_Score'] = skills_score
    

