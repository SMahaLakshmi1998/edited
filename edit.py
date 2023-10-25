from flask import Flask,render_template,request,url_for,redirect
import requests
fund="https://api.mfapi.in/mf/"
list1=[]

app=Flask(__name__)
@app.route('/',methods=["POST","GET"])
def home():
    if request.method=="POST":
        name=request.form.get("name")
        fundcode=request.form.get("fundcode")
        bank=requests.get(fund+str(fundcode))
        found=bank.json()
        fundhouse=found.get("meta").get("fund_house")
        investedamount=request.form.get("investedamount")
        unitheld=request.form.get("unitheld")
        found1=found.get("data")[0].get("nav")
        
        
        dic1={}
        dic1.update({"Name":name})
        dic1.update({"fundhouse":fundhouse})
        dic1.update({"investedamount":investedamount})
        dic1.update({"unitheld":unitheld})
        dic1.update({"found1":found1})
        currentvalue=float(dic1.get("found1"))*int(dic1.get("investedamount"))

        dic1.update({"currentvalue":currentvalue})
        growth=float(dic1.get("currentvalue"))-int(dic1.get("unitheld"))
        dic1.update({"growth":growth})
        list1.append(dic1)
    return render_template("edit1.html",sample=list1)

@app.route('/hello/<int:id>',methods=["POST","GET"])
def hello(id):
    
    if request.method=="POST":
         dic=list1[int(id)-1]
         dic.update({"Name":request.form.get("name")})
         dic.update({"fundhouse":request.form.get("fundhouse")})
         dic.update({"investedamount":request.form.get("investedamount")})
         dic.update({"unitheld":request.form.get("unitheld")})
        
         return redirect(url_for("home"))
    edit_list1=list1[int(id)-1]
    return render_template("fun1.html",s=edit_list1)
@app.route('/hello1/<int:id>')
def hello1(id):
     list1.pop(int(id)-1 )
     return render_template("edit1.html",sample=list1)

        



if __name__=="__main__":
    app.run(debug=True)