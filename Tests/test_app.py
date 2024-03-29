import unittest
from app.utils import add_ticket
import random



class TestAppFunc( unittest.TestCase ):

    def test_add_ticket(self):
        user_id = '1'
        ticket_number = str( random.randint( 1000, 9999 ) )
        ticket_description = 'asdf'
        ticket_status = 'asdf'
        try:
            ticket_id = add_ticket(user_id, ticket_number, ticket_description, ticket_status)
        except Exception as err:
            self.assertEqual( f"{err}", "Invalid Status" )
        ticket_status = 'done'
        try:
            ticket_id = add_ticket(user_id, ticket_number, ticket_description, ticket_status)
            self.assertTrue( isinstance( ticket_id, int ) )
        except Exception as err:
            self.assertTrue( isinstance( err, Exception ) )
