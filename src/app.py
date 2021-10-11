from flask import Flask, jsonify, request
import json
app = Flask(__name__)

todos = [{"label": "Sample", "done": True}]

@app.route('/todos', methods=['GET'])
def hello_world():
    res = jsonify(todos)
    return res

@app.route('/todos', methods=['POST'])
def add_new_todo():
    new_task = json.loads(request.data)
    todos.append(new_task)
    response = jsonify(todos)
    print("Incoming request with the following body", new_task)
    return response, 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    #position = todos.index(position)
    #todos.remove(position)
    #del todos[position]
    todos.pop(position)
    res = jsonify(todos)
    print('This is the position to delete: ',position)
    return res, 200
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)