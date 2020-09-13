# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 19:10:41 2020

@author: Anusha
"""
from flask import Flask , render_template ,request
import pickle
app  = Flask(__name__)
model = pickle.load(open('forest.pkl','rb'))
@app.route('/')
def hello_world():
    return render_template('Forestfire.html')

@app.route('/login', methods = ["POST"])
def login():
    temp = request.form["temp"]
    oxy = request.form["oxy"]
    humi= request.form["humi"]
    
    total = [[int(temp),int(oxy),int(humi)]]
    p=model.predict(total)
    p=p[0]
    
    if p==0:
        return render_template('Forestfire.html',label ="The probability of fire occurance is = "+ str(p)+" " +"(No Fire)")
    else:
        return render_template('Forestfire.html',label ="The probability of fire occurance is = "+ str(p)+" "+"(Will Cause Fire)")
        
if __name__=='__main__':
    app.run(debug = True,port = 5000)
