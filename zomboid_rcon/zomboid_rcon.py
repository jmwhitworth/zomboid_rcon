"""
Zomboid RCON: https://github.com/JMWhitworth/zomboid_rcon
    :copyright: (c) 2023 by JW: https://jackwhitworth.com
    :license: GPL-3.0, see LICENSE for more details.
"""


from .source import CommandResult, RconClient

"""
Credit to Shockbyte for the following resource:
https://shockbyte.com/billing/knowledgebase/479/All-Console-Commands-for-Your-Project-Zomboid-Server.html
"""


class ZomboidRCON(RconClient):
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


    """
        GENERAL COMMANDS
    """

    def additem(self, user:str, item:str) -> CommandResult:
        """
        Gives the specified player a specified item.
        /additem “user” “module.item”
        Items can be found on the PZ wiki: https://pzwiki.net/wiki/Items
        """
        return self.command("additem", user, item)


    def addvehicle(self, user:str) -> CommandResult:
        """
        Spawns a vehicle.
        /addvehicle “user”
        """
        return self.command("addvehicle", user)


    def addxp(self, user:str, perk:str, XP:int) -> CommandResult:
        """
        Gives XP to a player.
        /addxp “user” “perk=XP”
        """
        return self.command("addxp", user, f"{perk}={str(XP)}")


    def alarm(self) -> CommandResult:
        """
        Sounds a building alarm at the admin's position. Must be in a room.
        /alarm
        """
        return self.command("alarm")


    def changeoption(self, option:str, newOption:str) -> CommandResult:
        """
        Changes a server option.
        /changeoption option="newOption"
        """
        return self.command("changeoption", f'{option}="{newOption}"')


    def chopper(self) -> CommandResult:
        """
        Places a helicopter event on a random player.
        /chopper
        """
        return self.command("chopper")
    

    def changepwd(self, pwd:str, newPwd:str) -> CommandResult:
        """
        Changes your password.
        /changepwd “pwd” “newPwd”
        """
        return self.command("changepwd", pwd, newPwd)


    def createhorde(self, number:int) -> CommandResult:
        """
        Spawns a horde near a player.
        /createhorde “number”
        """
        return self.command("createhorde", str(number))


    def godmode(self, user:str) -> CommandResult:
        """
        Makes a player invincible.
        /godmode "user"
        """
        return self.command("godmode", user)


    def gunshot(self) -> CommandResult:
        """
        Makes a gunshot noise near the player.
        /gunshot
        """
        return self.command("gunshot")


    def help(self) -> CommandResult:
        """
        Brings up the help menu.
        /help
        Not to be confused with the commands available within zomboid_rcon. For a list of these commands see zomboid_rcon's Github repo: https://github.com/jmwhitworth/zomboid_rcon
        """
        return self.command("help")
    

    def invisible(self, user:str) -> CommandResult:
        """
        Makes a player invisible to zombies.
        /invisible “user”
        """
        return self.command("invisible", user)


    def noclip(self, user:str) -> CommandResult:
        """
        Allows a player to pass through solid objects.
        /noclip “user”
        """
        return self.command("noclip", user)


    def quit(self) -> CommandResult:
        """
        Saves and quits the server.
        /quit
        """
        return self.command("quit")


    def releasesafehouse(self) -> CommandResult:
        """
        Releases a safehouse you own.
        /releasesafehouse
        """
        return self.command("releasesafehouse")


    def reloadoptions(self) -> CommandResult:
        """
        Reloads server options.
        /reloadoptions
        """
        return self.command("reloadoptions")


    def replay(self, user:str, command:str, filename:str) -> CommandResult:
        """
        Records and plays a replay for a moving player.
        /replay “user” [-record | -play | -stop] “filename”
        """
        return self.command("replay", user, command, filename)


    def save(self) -> CommandResult:
        """
        Saves the current world.
        /save
        """
        return self.command("save")


    def sendpulse(self) -> CommandResult:
        """
        Toggles sending server performance info to the client.
        /sendpulse
        """
        return self.command("sendpulse")


    def showoptions(self) -> CommandResult:
        """
        Shows a list of current server options and values.
        /showoptions
        """
        return self.command("showoptions")


    def startrain(self) -> CommandResult:
        """
        Starts rain on the server.
        /startrain
        """
        return self.command("startrain")


    def stoprain(self) -> CommandResult:
        """
        Stops rain on the server.
        /stoprain
        """
        return self.command("stoprain")


    def teleport(self, user:str, toUser:str) -> CommandResult:
        """
        Teleports to a player.
        /teleport "toUser" or /teleport "user" "toUser"
        """
        if toUser is not None:
            return self.command("teleport", user, toUser)
        return self.command("teleport", user)


    def teleportto(self, x:int, y:int, z:int) -> CommandResult:
        """
        Teleports to certain coordinates.
        /teleportto x,y,z
        """
        return self.command("teleportto", f"{str(x)},{str(y)},{str(z)}")


    """
        MODERATION COMMANDS
    """

    def addalltowhitelist(self) ->CommandResult:
        """
        Adds all current users connected with a password to the whitelist.
        /addalltowhitelist
        """
        return self.command("addalltowhitelist")


    def adduser(self, user:str, pwd:str) -> CommandResult:
        """
        Adds a new user to the whitelist.
        /adduser “user” “pwd”
        """
        return self.command("adduser", user, pwd)


    def addusertowhitelist(self, user:str) -> CommandResult:
        """
        Adds a single user connected with a password to the whitelist.
        /addusertowhitelist “user”
        """
        return self.command("addusertowhitelist", user)


    def removeuserfromwhitelist(self, user:str) -> CommandResult:
        """
        Removes a single user connected with a password to the whitelist.
        /removeuserfromwhitelist “user”
        """
        return self.command("removeuserfromwhitelist", user)


    def banid(self, SteamID:str) -> CommandResult:
        """
        Bans a Steam ID.
        /banid “SteamID”
        """
        return self.command("banid", SteamID)


    def unbanid(self, SteamID:str) -> CommandResult:
        """
        Unbans a Steam ID.
        /unbanid “SteamID”
        """
        return self.command("unbanid", SteamID)


    def banuser(self, user:str) -> CommandResult:
        """
        Bans a user.
        /ban "user"
        """
        return self.command("banuser", user)


    def unbanuser(self, user:str) -> CommandResult:
        """
        Unbans a user.
        /unban "user"
        """
        return self.command("unbanuser", user)


    def grantadmin(self, user:str) -> CommandResult:
        """
        Gives admin rights to a user.
        /grantadmin "user"
        """
        return self.command("grantadmin", user)


    def removeadmin(self, user:str) -> CommandResult:
        """
        Removes admin rights to a user.
        /removeadmin "user"
        """
        return self.command("removeadmin", user)


    def kickuser(self, user:str) -> CommandResult:
        """
        Kicks a user from the server.
        /kickuser “user”
        """
        return self.command("kickuser", user)


    def players(self) -> CommandResult:
        """
        Lists all connected players.
        /players
        """
        return self.command("players")
    

    def servermsg(self, message:str) -> CommandResult:
        """
        Broadcast a message to all players.
        /servermsg “message”
        Spaces are replaced with underscores for compatibility.
        """
        return self.command("servermsg", message.replace(' ', '_').strip())


    def setaccesslevel(self, user:str, accesslevel:str) -> CommandResult:
        """
        Set the access/permission level of a player.
        /setaccesslevel “user” “[admin | moderator | overseer | gm | observer]”
        """
        return self.command("setaccesslevel", user, accesslevel)


    def voiceban(self, user:str, ban:str) -> CommandResult:
        """
        Ban a user from using the voice feature.
        /voiceban “user” [-true | -false]
        """
        return self.command("voiceban", user, ban)
