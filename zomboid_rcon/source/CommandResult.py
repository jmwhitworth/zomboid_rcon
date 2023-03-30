"""
Zomboid RCON: https://github.com/JMWhitworth/zomboid_rcon
    :copyright: (c) 2023 by JW: https://jackwhitworth.com
    :license: GPL-3.0, see LICENSE for more details.
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
