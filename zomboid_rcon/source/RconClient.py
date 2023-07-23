"""
Zomboid RCON: https://github.com/JMWhitworth/zomboid_rcon
    :copyright: (c) 2023 by JW: https://jackwhitworth.com
    :license: GPL-3.0, see LICENSE for more details.
"""


from rcon.source        import Client
from timeout_decorator  import timeout, TimeoutError

from .CommandResult     import CommandResult

class RconClient:
    """ Parent class for handling RCON core functionality """
    
    def __init__(self,
            ip:str,
            port:int,
            password:str,
            retries:int=5,
            logging:bool=False
        ):
        """
        Args:
            ip (str): The IP Address of the server.
            port (int): The RCON port of the server.
            password (str): The RCON password of the server.
            retries (int): Number of times to retry on request timeout.
            logging (bool): Print processes in terminal while running, used in debugging.
        """
        self._ip = ip
        self._port = port
        self._password = password
        self._retries = retries
        self.logging = logging
    
    def createClient(self) -> Client:
        """ Returns an rcon.source.Client object for requests """
        return Client(self._ip, self._port, passwd=self._password)
    
    def command(self, command:str, *args) -> CommandResult:
        """
        Attempts to execute a given command.
        Upon TimeoutError it will retry according to self._retries
        """
        tries = 0
        while tries < self._retries:
            try:
                result = self._command(command, *args)
                return CommandResult(
                    command = command,
                    successful = True,
                    response = result
                    )
            except TimeoutError:
                if self.logging:
                    print(f"({tries+1}/{self._retries}) Request timed out, retrying...")
                tries += 1
        return CommandResult(
            command = command,
            successful = False,
            response = f"Session timed out (after {self._retries} attempt(s))"
            )
    
    @timeout(10)
    def _command(self, command:str, *args) -> str:
        """ Private method to handle timeouts """
        try:
            with self.createClient() as client:
                return client.run(command, *args)
        except ConnectionRefusedError:
            return "Connection refused"
    
    def getInfo(self) -> dict:
        """ Returns dict of current object's information """
        return {
            "ip": self._ip,
            "port": self._port,
            "password": self._password,
            "retries": self._retries
        }
