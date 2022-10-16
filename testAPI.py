import os
from flask import Flask, jsonify, request
from multiprocessing import Value


counter = Value('i', 0)
app = Flask(__name__)

base_path = r'/tmp'
target_path = os.path.join(base_path, 'storage.data')
f = open(target_path)
a = f.read()
 
help_message = """
<html>
<body>
<head style="font-size:30px;">Key-value API prototype:</head>

<p>
- GET all data WEB:  http:/localhost:5000/api/list
</p>
<p>
- GET all data CURL:  curl -i -X GET http://localhost:5000/api/list
</p>
<p>
- GET data by index: http:localhost:5000/api/get/<id> 
</p>
<p>
- POST data: curl -i -H "Content-Type: application/json" -X POST -d '{"new_key": "new_value"}' http://localhost:5000/api/add data
</p>

</body>
</html>
"""

def id_generator():
    with counter.get_lock():
        counter.value += 1
        return counter.value

@app.route('/', methods=['GET'])
def help():
    return help_message

@app.route('/api/list', methods=['GET'])
def list():
    return jsonify(a)

@app.route('/api/add', methods=['POST'])
def index():
    payload = request.json
    payload['id'] = id_generator()
    a.append(payload)
    return "Created: {} \n".format(payload)

@app.route('/api/get', methods=['GET'])
def get_none():
    return 'ID Required: /api/get/<id> \n'

@app.route('/api/get/<int:_id>', methods=['GET'])
def get(_id):
    for val in a:
        if _id == val['id']:
            selected_val = val
    return jsonify(selected_val)

if __name__ == '__main__':
    app.run()
