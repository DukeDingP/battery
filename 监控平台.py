from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def login():
    i=1
    return render_template('梯次电池等级评估.html',name1=i)

if __name__ == '__main__':

    app.run(debug=True)