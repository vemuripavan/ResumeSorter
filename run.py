from flask import Flask, render_template, request, redirect, flash, make_response
import pandas as pd
import numpy as np
from resumesorter import ResumeSorter
from feature import jdparser 

app = Flask(__name__)

@app.route("/")
def start():
	return render_template("index.html")


#test = jdparser.parsejd("D:\deep\SPAN\Shikhsa\AI\ML\kaggle\Data Science_Final project\JD.xlsx")

@app.route("/upload", methods=['POST'])
def upload_file():
    if request.method=='POST':
        resumedir = request.form['resumedir']
        jdfile = request.files['JD']
        jddata=jdparser.parsejd(jdfile)
        
        rs = ResumeSorter()
        score_df = rs.sortResumes(jdfile,resumedir)
        #score_df.sort_values(by='text_score',ascending=False)
        return render_template("result.html", data=score_df, jddata=jddata)
        #return render_template("result.html")
        

if __name__ == "__main__":
    app.run()