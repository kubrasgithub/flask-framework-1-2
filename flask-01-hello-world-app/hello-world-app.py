from flask import Flask 
app = Flask(__name__)


@app.route("/")
def head():
    return "hello word clarusway-18"

@app.route("/second")
def head2():
    return "second page"

@app.route("/third")
def head3():
    return "buda 3 ncü sayfa"

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id of this page is {id}'

if __name__ == '__main__':

    app.run(debug=True, port=30000)
    # app.run(host= '0.0.0.0', port=8081)

   
   
    #python extantion yuklumu diye sol taraftan baktin deilse yukle
    #terminalde python3 --version
    #pip3 install Flask==2.3.3
    #pip3 list
    #python3 hello-world-app.py -- this works python application with manuel