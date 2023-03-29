import unittest
from unittest.mock import MagicMock, Mock

from zomboid_rcon import ZomboidRCON

class ZomboidRCON_test(unittest.TestCase):
    def setUp(self):
        mock_client = Mock()
        
        # create an instance of the ZomboidRCON class with the mock client
        self.pz = ZomboidRCON(ip="localhost", port=27015, password="", retries=5)
        self.pz.createClient = Mock(return_value=mock_client)
    
    def tearDown(self):
        return super().tearDown()
    
    def test_serverMsg(self):
        pass
