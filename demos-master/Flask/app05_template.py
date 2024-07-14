import requests
import datetime
from flask import Flask, render_template
import random
app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    year = datetime.datetime.now().year  # current year

    # return "Hello World"
    return render_template("index.html", random_number=random_number, year=year)


@app.route("/guess/<name>")
def guess(name):
    # call api https://api.agify.io/ and https://api.genderize.io/
    age_url = "https://api.agify.io?name=" + name
    gender_url = "https://api.genderize.io?name=" + name

    age_response = requests.get(age_url)
    gender_response = requests.get(gender_url)

    age = age_response.json()["age"]
    gender = gender_response.json()["gender"]

    return render_template("guess.html", name=name, gender=gender, age=age)


@app.route("/blog")
def get_blogs():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    header = {'Accept': 'application/json'}
    response = requests.get(blog_url, headers=header)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
