
from app import app
from app import HandleMinians
import unittest
import configparser

#Config parser to get configuration from config.ini file
CONFIG = configparser.ConfigParser()
CONFIG._interpolation = configparser.ExtendedInterpolation()
CONFIG.read('config.ini')

USERNAME = CONFIG.get('config', 'username')
PASSWORD = CONFIG.get('config', 'password')
HOSTNAME = CONFIG.get('config', 'hostname')
CMD = CONFIG.get('config', 'cmd')
CMD_STD_OUT = CONFIG.get('config', 'result')

class FlaskAppTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        #generate test client
        self.app = app.test_client()
        #passes exceptions in the line to the test client.
        self.app.testing = True
        #passes port number
        self.port_no = 22
        self.username = USERNAME
        self.password = PASSWORD
        self.hostname = HOSTNAME
        self.cmd = CMD
        self.cmd_std_out = CMD_STD_OUT

    def tearDown(self):
        pass

    def test_home_status_code(self):
        #send GET to root
        result = self.app.get("/")
        #check that result matches as expected
        self.assertEqual(result.status_code, 200)

    def test_home_data(self):
        #sends
        result = self.app.get("/")
        data ='<title>Cisco Project</title>'

        #assert the response data
        self.assertIn(data,result.data)

    def test_port_no(self):
        #sends port no
        port = self.port_no
        self.assertEqual(port,22)

    def test_executing_command(self):
        #creating instance
        handle_minians = HandleMinians()
        expected_std_out = self.cmd_std_out
        #passes values to function
        out = handle_minians.execute_cmd(self.hostname,self.username,self.password,self.cmd)
        #checks with expected result
        self.assertIn(expected_std_out, out)

if __name__ == '__main__':
    unittest.main()