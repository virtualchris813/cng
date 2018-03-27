#!/usr/bin/python
from flask import Flask, jsonify, request, abort
from queryByName import queryByName
from deleteByName import deleteByName
from buildName import addNewName

app = Flask(__name__)

@app.route('/cng/api/v0.1/queryByName', methods=['POST'])

def get_name():
    if not request.json or not 'host_name' in request.json:
        abort(400)
    hName = request.json['host_name']
    hNameResult = queryByName(hName)
    if hNameResult:
        return jsonify({'Name': hName, 'Found': True})
    else:
        return jsonify({'Name': hName, 'Found': False})

@app.route('/cng/api/v0.1/deleteByName', methods=['POST'])

def delete_name():
    if not request.json or not 'host_name' in request.json:
        abort(400)
    hName = request.json['host_name']
    hNameResult = deleteByName(hName)
    if hNameResult:
        return jsonify({'Name': hName, 'Found': True})
    else:
        return jsonify({'Name': hName, 'Found': False})

@app.route('/cng/api/v0.1/createName', methods=['POST'])

def create_name():
    if not request.json or not 'name_fields' in request.json:
        abort(400)
    hFields = request.json['name_fields']
    hName = addNewName(hFields)
    print(hName)
    if "Error" in hName:
        abort(400, hName)
    else:
        return hName

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

