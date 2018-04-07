from server import app, socketio, db
from flask_socketio import emit
from flask import send_from_directory
import os

@app.route('/', methods=['GET', 'POST'])
def index():
    return send_from_directory(os.path.join(os.getcwd(), 'static'), 'index.html')

'''
WS request for Classes
{data}: dict
'''
@socketio.on('Classes')
def get_class_names(data):
    print("[routes/get_class_names]: receive msg from user {0}".format(data['userId']))
    classeNames = db.get_all_class_names()
    rdata = {
        'data': {
            'pages': len(classeNames),
            'classNames': classeNames
        }
    }
    emit('rClasses', rdata)

'''
WS request for Nodes
{data}: dict
'''
@socketio.on('Nodes')
def get_node_names(data):
    print('[routes/get_node_names]: receive msg from user {0}'.format(data['userId']))
    nodeNames = db.get_nodes_of_class(data['class'])
    rdata = {
        'data': {
            'nodes': len(nodeNames),
            'nodeNames': nodeNames
        }
    }
    emit('rNodes', rdata)

'''
WS request for Node Info
{data}: dict
'''
@socketio.on('NodeInf')
def get_node_info(data):
    print('[routes/get_node_info]: receive msg from user {0}'.format(data['userId']))
    node = db.get_node_info(data['node'], data['class'])
    rdata = {
        'data': node
    }
    emit('rNodeInf', rdata)
