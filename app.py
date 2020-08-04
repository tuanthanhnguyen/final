'''from flask import Flask, render_template,send_file

app = Flask(__name__)





@app.route("/")

def home():

    return render_template('home.html')





if __name__ == '__main__':

    app.run(debug=True)'''
from flask import Flask, render_template 
 
app = Flask(__name__) 
 
@app.route('/')
def home():
    return render_template("index.html")
    return "Hey there,this is Thanh's website"
@app.route('/about-me')
def about():
    return render_template('about.html')
@app.route('/introduction')
def WordSection1():
    return render_template('home.html')
@app.route('/feedback')
def feedback():
    return render_template('feedback.html')
@app.route('/test')
def test():
    return render_template('first embed.html')
@app.route('/myapp')
def myapp():
    return render_template('myapp.html')
@app.route('/downloadtheapp')
def download():
    return send_file("./static/Phần mềm giải toán ngân hàng-(with update) (2).exe", as_attachment=True)
 
if __name__ == '__main__': app.run(debug=True) 
 
