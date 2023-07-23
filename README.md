# Zomboid-rcon: Python RCON for Project Zomboid Servers
 
### Version: 1.0.0

Zomboid-rcon enables you to easily communicate with your Project Zomboid servers via RCON. With zomboid-rcon, you can send commands to your server, manage players, and more, all from within your Python script.

<br><br>

# Installation

To get started, simply install zomboid-rcon using pip:

```bash
pip install zomboid-rcon
```

- [Homepage](https://jackwhitworth.com/posts/zomboid-rcon/)
- [GitHub Repo](https://github.com/jmwhitworth/zomboid_rcon)
- [Pypi Package](https://pypi.org/project/zomboid-rcon/)

<br><br>

# Usage

Using zomboid-rcon is easy. Here's a basic example:

```python
from zomboid_rcon import ZomboidRCON

if __name__ == "__main__":
    pz = ZomboidRCON(ip='localhost', port=12345, password='myPassword')
    command = pz.serverMsg("You dead yet?")
    print(command.response)
```

This example connects to a server running on your local machine and sends the message "You dead yet?".

Zomboid-rcon provides several built-in methods for common server management tasks, such as getting a list of connected players:

```python
from zomboid_rcon import ZomboidRCON

if __name__ == "__main__":
    pz = ZomboidRCON(ip='localhost', port=12345, password='myPassword')
    print(pz.players().response)
```

This example prints a list of all players currently connected to the server.

<br><br>

# Available Commands

Zomboid-rcon provides built-in methods for the available RCON commands within Project Zomboid.

### General Commands

- `additem("user", "item")` : Items can be found on the PZ wiki: https://pzwiki.net/wiki/Items
- `addvehicle("user")` : Spawns a vehicle.
- `addxp("user", "perk", xp)` : Gives XP to a player.
- `alarm()` : Sounds a building alarm at the admin's position. Must be in a room.
- `changeoption("option", "newOption")` : Changes a server option.
- `chopper()` : Places a helicopter event on a random player.
- `changepwd("pwd", "newPwd")` : Changes your password.
- `createhorde("number")` : Spawns a horde near a player.
- `godmode("user")` : Makes a player invincible.
- `gunshot()` : Makes a gunshot noise near the player.
- `help()` : Brings up the help menu. (Lists native RCON commands. For all zomboid_rcon commands, refer to this list)
- `invisible("user")` : Makes a player invisible to zombies.
- `noclip("user")` : Allows a player to pass through solid objects.
- `quit()` : Saves and quits the server.
- `releasesafehouse()` : Releases a safehouse you own.
- `reloadoptions()` : Reloads server options.
- `replay("user", [-record | -play | -stop], "filename")` : Records and plays a replay for a moving player.
- `save()` : Saves the current world.
- `sendpulse()` : Toggles sending server performance info to the client.
- `showoptions()` : Shows a list of current server options and values.
- `startrain()` : Starts rain on the server.
- `stoprain()` : Stops rain on the server.
- `teleport("user", "toUser")` : Teleports to a player.
- `teleportto(x, y, z)` : Teleports to certain coordinates.

### Moderation Commands

- `addalltowhitelist()` : Adds all current users connected with a password to the whitelist.
- `adduser("user", "pwd")` : Adds a new user to the whitelist.
- `addusertowhitelist("user")` : Adds a single user connected with a password to the whitelist.
- `removeuserfromwhitelist("user")` : Removes a single user connected with a password to the whitelist.
- `banid("SteamID")` : Bans a Steam ID.
- `unbanid("SteamID")` : Unbans a Steam ID.
- `banuser("user")` : Bans a user.
- `unbanuser("user")` : Unbans a user.
- `grantadmin("user")` : Gives admin rights to a user.
- `removeadmin("user")` : Removes admin rights to a user.
- `kickuser("user")` : Kicks a user from the server.
- `players()` : Lists all connected players.
- `servermsg("message")` : Broadcast a message to all players. (Spaces are replaced with underscores for compatibility)
- `setaccesslevel("user", [admin | moderator | overseer | gm | observer])` : Set the access/permission level of a player.
- `voiceban("user", [-true | -false])` : Ban a user from using the voice feature.

<br>

### Command not listed?

You can execute any custom command using the command method:
```python
pz.command("command", "arg1", "arg2", "etc")
```

<br><br>

# Demonstration

![Zomboid RCON demonstration GIF](https://jackwhitworth.com/wp-content/uploads/2023/07/zomboid_rcon_demo.gif)

<br><br>

# Known Issues

Please note that zomboid-rcon uses the [timeout_decorator](https://pypi.org/project/timeout-decorator/) package, which is currently only compatible with Unix/Linux systems. As a result, **timeouts may cause errors on Windows machines**. We are actively working on finding an alternative solution for Windows users.

<br><br>

# Contributing

We welcome contributions from anyone! If you would like to contribute to the project, please open an issue or submit a pull request on [Github](https://github.com/JMWhitworth/zomboid_rcon).

<br><br>

# License

Zomboid-rcon is licensed under the GPL-3.0 license.
