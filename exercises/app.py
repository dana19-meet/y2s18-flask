from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    dancers = ["batseva", "ohad neharin", "maddie"]
    return render_template(
        "index.html" ,
        dancers=dancers,
        likes_same_sport=True)

if __name__ == '__main__':
    app.run(debug = True)