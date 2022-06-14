from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secrect"

# some code for the routes andd endpoints
list_todos = [{
    "todo": "learn Templates in flask",
    "status": "in progres",
},
    {
    "todo": "learn Objests Orientation Programing",
    "status": "complete"
},
    {
    "todo": "learn Deployment",
    "status": "cancel"
}]

app.route("/")


@app.route("/todos")
def get_all_todos():
    if "NUMBER_OF_VISITS" in session:
        session["NUMBER_OF_VISITS"] += 1
    else:
        session["NUMBER_OF_VISITS"] = 1
    return render_template("index.html", first_name="Lenddy", list_todos=list_todos)


@app.route("/todo/new")
def display_create_todo():
    if "NUMBER_OF_VISITS" in session:
        session["NUMBER_OF_VISITS"] += 1
    else:
        session["NUMBER_OF_VISITS"] = 1
    return render_template("todoForm.html")

# you have link the routt on the first html file that you created  with an a tag        and the tag needs to be at the very bottom'

''' your need to create another routeto be able to display the new form (/todo/new)
you can create 2 routes with the same URL BUT the funtions name need to be different 
you dont have to specify the get method because that is the defaut method  the othe method need to be specify method = [' method type ']
'''

@app.route("/todo/new", methods=['POST'])
def create_todo():
    # here we need one of the form that we imported  (request) requeste is an objet and it has an atribute that is form  this atribute is unmutable dictionary       so to see it we need to put request.form
    print(request.form)
    # we need to target the list_todos and do an append()
    new_todo = {
        "todo":request.form["todo"],
        "status": request.form["status"]
    }
    list_todos.appen(new_todo) 
    # here we need to use the  redirect funtion that we imported 
    return redirect("/")
    print("trigering this todo methooooooooooood")

'''
we need to create a new tamplate 
in our templait folder'''


# display routes
# Action routes
if __name__ == "__main__":
    app.run(debug=True)

# standar ways to do get, post,put,and delet 
# 
# they all have to be on caps when you rigth them    
'''
Get = read and display
URL of the route to display all: the name of the list or dictionary that we are about to diaply 
example: "/ todos"
example: "/ users"


funtion: get_all_todos()

URL of the route display one: the name of teh list in singular  that we are sbout to display follow by the id
example: "/todo/<int:id>"
example: "/users/<int:id> "

untion:get_todo_by_id(id)


post = create
funtion: create_todo()

URL of the route to create something new the name of the list in singular the we about to create follow by the keyword new
example: "/todo/new"
example: "/user/new"


put = update
the URL of the route to update someting existing: the name of the list in singular that we are about to update, follow by the id followed by the keyword /update or edit

funtion: funtion: update_todo_user_by_id

example : "/todo/<int:id/update>"
example: "/usere <int:id>/update"

funtion: update_todo_by_id(id)

delete = remove

the URL of the route to delete someting existing: the name of the list in singular that we are about to delete, follow by the id followed by the keyword /delete or remove

example : "/todo/<int:id/delete>"
example: "/usere <int:id>/remove"


funtion: delete_todo_by_id(id)

'''


"http://127.0.0.1:5000/hello"
'''@app.route("/hello")
def hello_from_flask():
    return "hello this message is coming from your first server in flask "
@app.route("/bye")
def bye_from_flask():
    return "<h1> bye classssss <h1/> "
@app.route("/number/<int:num>")
def print_number(num):
    print("number sent from URL:", num)
    return "your number is " + str(num)'''
