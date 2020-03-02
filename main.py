import sys
from flask import Flask, render_template, request
from flask_restful import reqparse, abort, Api, Resource
import os


app = Flask(__name__)
api = Api(app)

# TODOS = {
#     'todo1': {'task': 'build an API'},
#     'todo2': {'task': '?????'},
#     'todo3': {'task': 'profit!'},
# }


# def abort_if_todo_doesnt_exist(todo_id):
#     if todo_id not in TODOS:
#         abort(404, message="Todo {} doesn't exist".format(todo_id))

# parser = reqparse.RequestParser()
# parser.add_argument('task')


# # Todo
# # shows a single todo item and lets you delete a todo item
# class Todo(Resource):
#     def get(self, todo_id):
#         abort_if_todo_doesnt_exist(todo_id)
#         return TODOS[todo_id]

#     def delete(self, todo_id):
#         abort_if_todo_doesnt_exist(todo_id)
#         del TODOS[todo_id]
#         return '', 204

#     def put(self, todo_id):
#         args = parser.parse_args()
#         task = {'task': args['task']}
#         TODOS[todo_id] = task
#         return task, 201


# # TodoList
# # shows a list of all todos, and lets you POST to add new tasks
# class TodoList(Resource):
#     def get(self):
#         return TODOS

#     def post(self):
#         args = parser.parse_args()
#         todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
#         todo_id = 'todo%i' % todo_id
#         TODOS[todo_id] = {'task': args['task']}
#         return TODOS[todo_id], 201

# ##
# ## Actually setup the Api resource routing here
# ##
# api.add_resource(TodoList, '/todos')
# api.add_resource(Todo, '/todos/<todo_id>')

@app.route('/') #creates the flask html route
def root():
    return render_template('main.html')
@app.route('/', methods=['POST']) #creates the flask html route
def post():
    text1 = request.form['user1']
    text2 = request.form['user2'] 
    text3 = request.form['user3']
    text4 = request.form['user4'] 
    args = "del *.avi"
    os.system(args)
    args2 = "del *.png"
    os.system(args2)
    args3 = "del *.mp4"
    os.system(args3)
    args3 = "python3 hw3queue.py "+ str(text1) + " " + str(text2) + " " + str(text3) + " " + str(text4)
    os.system(args3)
    processed_text = text1.upper()
    return render_template('videos.html')



if __name__ == '__main__':

    app.run()