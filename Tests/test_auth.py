import unittest
import auth
import random, string



class TestUserAuth( unittest.TestCase ):

    password = 'test4'
    name = 'test4'

    def test_register_user(self):
        username = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        token = auth.user.register( username, self.password, self.name )
        self.assertTrue( isinstance( token, str ) )


    def test_login_user(self):
        username = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        token = auth.user.register( username, self.password, self.name )
        auth_token = auth.user.login( username, self.password )
        self.assertTrue( isinstance( auth_token, str ) )


    def test_user_status(self):
        username = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        token = auth.user.register( username, self.password, self.name )
        details = auth.user.details( token )
        self.assertTrue( isinstance(details, dict) )
        self.assertTrue( details['token'] == token )


    def test_logout_user(self):
        username = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        token = auth.user.register( username, self.password, self.name )
        self.assertTrue( auth.user.logout( token ) )
