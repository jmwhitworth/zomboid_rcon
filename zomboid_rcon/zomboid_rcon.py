"""
Zomboid RCON.

    :copyright: (c) 2023 by JW.
    :license: GPL-3.0, see LICENSE for more details.
"""

from rcon.source        import Client
from timeout_decorator  import timeout, TimeoutError
from dotenv             import load_dotenv
import os

"""
Credit to Shockbyte for the following resource:
https://shockbyte.com/billing/knowledgebase/479/All-Console-Commands-for-Your-Project-Zomboid-Server.html
"""

class CommandResult:
    """ A class representing the result of executing a command. """
    
    def __init__(self,
            command:str,
            response:str,
            successful:bool=False,
            failureMessage:str="Command was unsuccessful"
        ):
        """        
        Args:
            command (str): The command that was executed.
            response (str): The response to the command.
            successful (bool, optional): Whether the command was successful. Defaults to False.
            failureMessage (str, optional): The message to display if the command was unsuccessful. Defaults to "Command was unsuccessful".
        """
        self.command = command
        self.response = response
        self.successful = successful
        self.failureMessage = failureMessage
    
    @property
    def command(self) -> str:
        """ Returns command used """
        return self._command
    
    @command.setter
    def command(self, command:str) -> None:
        """
        Validates input as string
        Returns true if set successfully
        """
        if isinstance(command, str):
            self._command = command.strip()
        else:
            raise ValueError("Command used must be a string")
    
    @property
    def failureMessage(self) -> str:
        """ Returns failure message if command unsuccessful """
        return self._failureMessage
    
    @failureMessage.setter
    def failureMessage(self, failureMessage:str) -> None:
        """
        Validates input as string
        Returns true if set successfully
        """
        if isinstance(failureMessage, str):
            self._failureMessage = failureMessage.strip()
        else:
            raise ValueError("Failure message used must be a string")
    
    @property
    def response(self) -> str:
        """
        Returns the command's response.
        If command failed, returns failure message.
        """
        if self.successful:
            return self._response
        
        return self.failureMessage
    
    @response.setter
    def response(self, newResponse:str) -> None:
        """
        Validates input as string
        Returns true if set successfully
        """
        if isinstance(newResponse, str):
            self._response = newResponse.strip()
        else:
            raise ValueError("Command response must be a string")
    
    @property
    def successful(self) -> bool:
        """ Returns if command was successful """
        return self._successful
    
    @successful.setter
    def successful(self, successStatus:bool) -> None:
        """
        Validates input as boolean
        Returns true if set successfully
        """
        if isinstance(successStatus, bool):
            self._successful = successStatus
        else:
            raise ValueError("Success status must be a boolean")


class RConClient:
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
    
    @timeout(5)
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


class ZomboidRCON(RConClient):
    """
    Used to interact with Zomboid servers via RCON
    """
    def __init__(self,
            ip:str='localhost',
            port:int=27015,
            password:str='',
            retries:int=5,
            logging:int=False
        ):
        super().__init__(ip, port, password, retries, logging)
    
    def serverMsg(self, message:str) -> CommandResult:
        return self.command("servermsg", message.replace(' ', '_').strip())
    
    def players(self) -> CommandResult:
        return self.command("players")
    
    def save(self) -> CommandResult:
        return self.command("save")
    
    def quit(self) -> CommandResult:
        return self.command("quit")
    
    def help(self) -> CommandResult:
        return self.command("help")
    
    def showOptions(self) -> CommandResult:
        return self.command("showoptions")


if __name__ == "__main__":
    load_dotenv()
    
    pz = ZomboidRCON(
        str(os.getenv('SERVER_IP')),
        int(os.getenv('SERVER_PORT')),
        str(os.getenv('SERVER_PASSWORD')),
        int(os.getenv('RETRIES'))
    )
    
    print(pz.players().response)
