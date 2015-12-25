__author__ = 'malcolmbarnes'
from flask import Flask, render_template, request, redirect
app= Flask(__name__)


todolist= []
@app.route('/', methods=['GET', 'POST'])
def toDo():

    return render_template ('index.html', todolist= todolist)


@app.route('/updates.html')
def updates():
    return render_template('updates.html', blog_updates=blog_updates)

@app.route('/submit', methods= ['POST'])
def submit():
    task= request.form['task']
    priority= request.form['priority']
    email= request.form['email']
    print(task,email,priority)
    return redirect ('/')





if __name__ == "__main__":
    app.run(debug= True)

