from flask import Flask,render_template,request
import pandas as pd
import os

app=Flask(__name__)
app.config["UPLOAD_FOLDER"]='uploads'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload',methods=['POST'])
def upload_file():
    file=request.files['file']

    if file and file.filename.endswith('.csv'):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)


        df=pd.read_csv(file_path)
        data=df.head().to_html()
        stats=df.describe().to_html()
        return render_template('result.html',data=data, stats=stats)

#app.run()
app.run(host="0.0.0.0", port=5000,debug=True)