from flask import Flask, render_template, request
import numpy as np
import pickle
app=Flask (__name_ # our flask app
@app.route('/') # rendering the html template
def home():
return render_template('home.html')
@app.route('/predict') # rendering the html template
def index() :
return render_template("index.html")
@app.route('/data_predict', methods=['POST']) # route for our prediction def predict():
age = request.form['age'] # requesting for age data
gender = request.form['gender'] # requesting for gender data
tb = request.form['tb'] # requesting for Total Bilirubin data
db = request.form['db'] # requesting for Direct Bilirubin data
ap = request.form['ap'] # requesting for Alkaline Phosphotose data
aal = request.form['aal'] # requesting for Alamine Aminotransferase data
aa2 = request.form['aa2'] # requesting for Aspartate Aminotransferase data tp = request.form['tp'] # requesting for Total_Protiens data
a = request.form['a'] # requesting for Albumin data
agr = request.form['agr'] # requesting for Albumin and Globulin Ratio data
#coverting data into float format
data = [[float(age), float (gender), float(tb), float(db), float (ap), float (aal), float (aa2), float(tp),
# Loading model which we saved
model = pickle.load(open('liver_analysis.pkl', 'rb'))
prediction= model.predict(data)[0]
if (prediction == 1):
return render_template('noChance.html', prediction='You have a liver desease problem, You must and)
else:
return render_template('chance.html', prediction='You dont have a liver desease problem')
if __name__ == '__main__':
app.run()
