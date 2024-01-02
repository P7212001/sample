from flask import Flask, render_template, request
app = Flask(_name_)

@app.route("/")
def home_page(name=None):
    return render_template("index.html",name=name)


if name == '_main_':
    app.run(host='0.0.0.0',port=5000)
