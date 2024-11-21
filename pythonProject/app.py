from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    dic = {"Name":"Ajay","Age":"22","Mobile":"2020202020"}
    return render_template('index.html',context=dic)

@app.route('/about-us')
def about_us():
    return render_template('about.html')

@app.route('/contact-us')
def contact_us():
    return render_template('contact.html',)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5005,debug=True)