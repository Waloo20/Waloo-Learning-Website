from flask import Flask, render_template, send_from_directory
from data import Data
app = Flask(__name__)


@app.route("/")
def home():
  return render_template('home.html',
                        data = Data)

@app.route("/blog")
def blog():
  return render_template('blog.html')
  
@app.route("/credentials")
def credentials():
  return render_template('credentials.html')
  
@app.route("/CardPredictor")
def CardPredictor():
  return render_template('CardPredictor.html')

@app.route("/WebsiteProject")
def WebsiteProject():
  return render_template('WebsiteProject.html')

@app.route("/CactusProject")
def CactusProject():
  return render_template('CactusProject.html')

@app.route("/Aboutme")
def Aboutme():
  return render_template('Aboutme.html')
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
