from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(100))
    is_completed = db.Column(db.Boolean,default=False)

    def __init__(self,content):
        self.content = content
    





@app.route('/',methods=['GET','POST'])
def home():

    if request.method == 'POST':
        todo_content = request.form.get('todo')
        todo_row = Todo(todo_content)
        db.session.add(todo_row)
        db.session.commit()


    todos = Todo.query.all()

    context = {
        'todos':todos
    }
    return render_template('index.html',context=context)



if __name__=='__main__':
    app.run(debug=True)