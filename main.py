# Code By Arman Shaikh
import flask
from flask import Flask,render_template
from flask import request
from calculator import calculatio

app=Flask(__name__)
@app.route("/")
def main():
    return render_template("/index.html")

@app.route('/calculation',methods=['GET','POST'])
def calculation():
    if request.method=="POST":
        x=request.form.get('fnumber',default=0,type=float)
        y=request.form.get('snumber',default=0,type=float)
        z=request.form.get('operator')
        result=str(calculatio(x,y,z))
        return render_template("index.html",x=result)
    else:
        x=request.args.get('fnumber',default=0,type=float)
        y=request.args.get('snumber',default=0,type=float)
        z=request.args.get('operator')
        result=str(calculatio(x,y,z))
        return render_template("index.html",x=result)

    


if __name__=="__main__":
    app.run(debug = True)

