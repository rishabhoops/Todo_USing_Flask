from flask import Flask, render_template , request, redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title_name = db.Column(db.String, nullable=False)
    desc = db.Column(db.String,nullable=False)

    def __repr__(self)->str:
        return f"{self.sno} - {self.title_name}"


@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
        title=request.form['title_name']
        desc=request.form['desc']
        todo=Todo(title_name=title,desc=desc)
        db.session.add(todo)
        db.session.commit()
    
    allTodo=Todo.query.all()
    return render_template('index.html',allTodo=allTodo)
    
@app.route('/delete/<int:sno>')
def delete(sno):
    todo=Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")
  
    


if __name__=="__main__":
    # app.run(debug=True)
    with app.app_context():
        db.create_all()
app.run(debug=True)