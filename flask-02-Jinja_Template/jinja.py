from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html", number1=1981, number2=1453)

@app.route("/cohort18")
def number():
    num1 = 12
    num2 = 11
    return render_template("body.html", value1=num1, value2=num2, sum=num1+num2)



if __name__== "__main__":
    app.run(debug=True, port=30000)
    # app.run(host= '0.0.0.0', port=8081)

    #soruce kodlar templates klasorunde icinde bulunur ve render_template ile cagrilir.
    # sudo dnf install tree -- dosyalari agac seklinde gorebilmek icin

    #BU ISLEMLERI EC2 YA BAGLANIP YAPARKEN ASAGIDAKI ISLEMLERI IZLE
    # ec2 ya terminalden baglandigimizda flask yuklu olmuyor pip3 list ile 
    #olmadigini gorebilirsin. 
    #sudo yum install python3-pip -y   --flaski yukler. pip3 list ile bak Flask formuyorsan indirmemis. pip3 install flask le indir.
    # # python3 --version la yuklu geldigini gorursun.
    #vim  hello.py  
    # from flask import Flask 

    #vim hello.py
 # app = Flask(__name__)

 # @app.route("/")
 # def head():
   #   return "hello word clarusway-18"

 # @app.route("/second")
 # def head2():
     # return "second page"

 # @app.route("/third")
 # def head3():
    #  return "buda 3 ncü sayfa"

 # @app.route('/forth/<string:id>')
 # def forth(id):
     # return f'Id of this page is {id}'

 # if __name__ == '__main__':

     # app.run(debug=True, port=30000)
    # app.run(host= '0.0.0.0', port=8081)

    #  python3 hello.py --python dosyasini calistirir.

    # KILL ETME
    #ps -ef | grep python
    #sudo kill -9

    # VIM DEN CIKMA  :wq

    # ** WEB SERVERDAN EC2 YI GORUTELEMEK ICIN PYTHON KODUNU CALISTIRDIKTAN SONRA
    # ** EC2 KENDI IP4 VEYA DNS ADRESI SONUNA :8081 YAZARAK WEB SERVERDA GOREBILIRSIN.