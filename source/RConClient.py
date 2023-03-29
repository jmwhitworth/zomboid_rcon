from rcon.source        import Client
from timeout_decorator  import timeout, TimeoutError

from .CommandResult     import CommandResult


class RConClient:
    def __init__(self, ip:str, port:int, password:str, retries:int=5):
        self._ip = ip
        self._port = port
        self._password = password
        self._retries = retries
    
    def createClient(self) -> Client:
        return Client(self._ip, self._port, passwd=self._password)
    
    def command(self, command:str, *args) -> CommandResult:
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
                print(f"({tries+1}/{self._retries}) Request timed out, retrying...")
                tries += 1
        return CommandResult(
            command = command,
            successful = False,
            response = f"Session timed out (after {self._retries} attempt(s))"
            )
    
    @timeout(5)
    def _command(self, command:str, *args) -> str:
        try:
            with self.createClient() as client:
                return client.run(command, *args)
        except ConnectionRefusedError:
            return "Connection refused"
    
    def getInfo(self) -> dict:
        return {
            "ip": self._ip,
            "port": self._port,
            "password": self._password,
            "retries": self._retries
        }
