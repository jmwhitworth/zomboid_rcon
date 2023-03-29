import unittest

from zomboid_rcon.source.CommandResult import CommandResult

class CommandResult_test(unittest.TestCase):
    def setUp(self):
        self.cr = CommandResult("Default", "Default")
    
    def tearDown(self):
        return super().tearDown()
    
    
    def test_command_returns_expected(self):
        self.cr.command = "customCommand"
        self.assertEqual(self.cr.command, "customCommand")
    
    def test_command_validates_input(self):
        values = [0, 0.5, True, None]
        for value in values:
            with self.assertRaises(ValueError):
                self.cr.command = value
    
    def test_command_cleans_input(self):
        self.cr.command = "    customCommand  "
        self.assertEqual(self.cr.command, "customCommand")
    
    
    def test_failureMessage_returns_expected(self):
        self.cr.failureMessage = "Custom failure message"
        self.assertEqual(self.cr.failureMessage, "Custom failure message")
    
    def test_failureMessage_validates_input(self):
        values = [0, 0.5, True, None]
        for value in values:
            with self.assertRaises(ValueError):
                self.cr.failureMessage = value
    
    def test_failureMessage_cleans_input(self):
        self.cr.failureMessage = "    customFailureMessage  "
        self.assertEqual(self.cr.failureMessage, "customFailureMessage")
    
    
    def test_response_returns_expected(self):
        self.cr.response = "Response"
        self.cr.successful = True
        self.assertEqual(self.cr.response, "Response")
        
        self.cr.successful = False
        self.assertEqual(self.cr.response, self.cr.failureMessage)
    
    def test_response_validates_input(self):
        values = [0, 0.5, True, None]
        for value in values:
            with self.assertRaises(ValueError):
                self.cr.response = value
    
    def test_response_cleans_input(self):
        self.cr.response = "    Response  "
        self.cr.successful = True
        self.assertEqual(self.cr.response, "Response")
    
    
    def test_successful_returns_expected(self):
        self.cr.successful = True
        self.assertEqual(self.cr.successful, True)
        
        self.cr.successful = False
        self.assertEqual(self.cr.successful, False)
    
    def test_successful_validates_input(self):
        values = [0, 0.5, "Test", None]
        for value in values:
            with self.assertRaises(ValueError):
                self.cr.successful = value
