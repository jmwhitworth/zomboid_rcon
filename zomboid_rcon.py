"""
Zomboid RCON.

    :copyright: (c) 2023 by JW.
    :license: MIT, see LICENSE for more details.
"""

from dotenv             import load_dotenv
from source             import RConClient, CommandResult
import os

"""
Credit to Shockbyte for the following resource:
https://shockbyte.com/billing/knowledgebase/479/All-Console-Commands-for-Your-Project-Zomboid-Server.html
"""

class ZomboidRCON(RConClient):
    def __init__(self,
            ip:str='localhost',
            port:int=27015,
            password:str='',
            retries:int=5
        ):
        super().__init__(ip, port, password, retries)
    
    def serverMsg(self, response:str) -> CommandResult:
        return self.command("servermsg", response.replace(' ', '_').strip())
    
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
    
    print(pz.serverMsg().response)
