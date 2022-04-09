#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template


# In[2]:


app=Flask(__name__)


# In[3]:


import joblib


# In[4]:


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        income = float(request.form.get("income"))
        age = float(request.form.get("age"))
        loan = float(request.form.get("loan"))
        print(income,age,loan)
        
        model1 = joblib.load("Tree")
        pred1 = model1.predict([[income, age, float(loan)]])
        
        model2 = joblib.load("RF")
        pred2 = model2.predict([[income, age, float(loan)]])
        
        model3 = joblib.load("GB")
        pred3 = model3.predict([[income, age, float(loan)]])
        
        return(render_template("index.html",result1=pred1,result2=pred2,result3=pred3))
    else:
        return(render_template("index.html",result1="Please input a value",result2="Please input a value",result3="Please input a value"))


# In[ ]:


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int("2345"))


# In[ ]:




