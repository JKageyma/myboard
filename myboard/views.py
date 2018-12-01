from flask import url_for, request, render_template, redirect
from myboard import app,db
from myboard.models import Content


@app.route("/")

def index():
    contents = Content.query.order_by("id desc").all()
    return render_template("index.html", contents=contents)

@app.route("/add_content", methods=['POST'])
def add_content():
    content = Content(
        name=request.form['name'],
        text=request.form['text'],
    )
    db.session.add(content)
    db.session.commit()

    return redirect(url_for('index'))
