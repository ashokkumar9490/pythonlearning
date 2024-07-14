from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route('/hello')
def hello():
    return render_template('hello.html', utc_dt=datetime.datetime.utcnow())


@app.route('/comments')
def comments():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('comments.html', comments=comments)


if __name__ == '__main__':
    app.run(debug=True)
