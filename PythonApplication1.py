import json
from flask import Flask, jsonify

app = Flask(__name__)
"""
getHomeInfo
"""
@app.route('/getHomeInfo', methods=['GET'])
def getHomeInfo():
    with open('./res/db.json' , encoding="utf-8") as userFile:
       fileContents = userFile.read()
    y = json.loads(fileContents)
    print(y["HomeInfo"])
    return jsonify(y["HomeInfo"])

"""
Login
"""
@app.route('/getLogin', methods=['POST'])
def login():
    with open('./res/db.json' , encoding="utf-8") as userFile:
       fileContents = userFile.read()
    y = json.loads(fileContents)
    print(y["USERLOGIN"])
    return jsonify(y["USERLOGIN"])




"""
@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for record in records:
            if record['name'] == name:
                return jsonify(record)
        return jsonify({'error': 'data not found'}
                       """
app.run()


