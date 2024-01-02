from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html", name="YourName")  # Provide a default value or fetch the name from somewhere

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
