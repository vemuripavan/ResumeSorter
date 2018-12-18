from flask import Flask, render_template, request, redirect, flash, make_response
import pandas as pd
import numpy as np
from resumesorter import ResumeSorter

app = Flask(__name__)

@app.route("/")
def start():
	return render_template("index.html")


@app.route("/upload", methods=['POST'])
def upload_file():
    print("Sample for upload:")
    if request.method=='POST':
        resumedir = request.form['resumedir']
        print(resumedir)
        """resumelist = []
        if type(resumes) is list:
            resumelist = resumes
            for resume in resumes:
                print("file list: "  +resume.filename)
        else :
            print("Single File type :"+str(type(resumes))+": " + resumes.filename)
            resumelist.append(resumes)"""
            
        rs = ResumeSorter()
        #dir_cvs="D:\deep\SPAN\Shikhsa\AI\ML\kaggle\Data Science_Final project\Resumes\docx"
        file_list = rs.getfiles(resumedir)
        text_dic = rs.extracttext(file_list)
        df = pd.DataFrame.from_dict(data=text_dic,orient='index')
        return render_template("result.html", data=df)
        #return render_template("result.html")
        

if __name__ == "__main__":
    app.run()