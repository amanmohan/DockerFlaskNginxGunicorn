'''
Flask restplus API
'''
import paramiko

from flask import Flask
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix

#app configuration
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='Cisco Project',\
    description='Handiling minians API')

ns = api.namespace('API', description='Restful operations')

json_data = api.model('json_format',{
    'hostname': fields.String(required=True, description='VM Name'),
    'username' : fields.String(required=True, description='VM Username'),
    'password' : fields.String(required=True, description='VM Password'),
    'command': fields.String(required=True, description='command')
})

class HandleMinians(object):
    '''
    Handling minions configuration
    '''
    def __init__(self):
        self.port = 22
        self.cmd_executed = []

    def execute_cmd(self, hostname, username, password, command):
        '''
        connection to master using ssh
        '''
        sshClient = paramiko.SSHClient()
        sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshClient.load_system_host_keys()
        sshClient.connect(hostname, self.port, username, password)
        stdin, stdout, stderr = sshClient.exec_command(command)
        self.cmd_executed.append(command)
        return stdout.read()
handle_minian = HandleMinians()

@ns.route('/')
class AddMinian(Resource):
    '''
    Shows a list of all minian, and lets you POST to add new tasks
    '''
    @ns.doc('pass_json')
    @ns.expect(json_data)
    def post(self):
        '''
        Posting data to minions
        '''
        data = api.payload
        hostname = data['hostname']
        username = data['username']
        password = data['password']
        command = data['command']
        return handle_minian.execute_cmd(hostname, username, password, command), 201
    @ns.doc('list_commands')
    def get(self):
        '''
        List all tasks performed
        '''
        return handle_minian.cmd_executed


if __name__ == '__main__':
    app.run(debug=True)
