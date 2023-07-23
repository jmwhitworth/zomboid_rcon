# Zomboid-rcon: Python RCON for Project Zomboid Servers
 
Zomboid-rcon enables you to easily communicate with your Project Zomboid servers via RCON. With zomboid-rcon, you can send commands to your server, manage players, and more, all from within your Python script.

<br>

# Installation

To get started, simply install zomboid-rcon using pip:

``` pip install zomboid-rcon ```

[Pypi Package](https://pypi.org/project/zomboid-rcon/) / [GitHub Repo](https://github.com/jmwhitworth/zomboid_rcon)

<br>

# Usage

Using zomboid-rcon is easy. Here's a basic example:

```python
from zomboid_rcon import ZomboidRCON

if __name__ == "__main__":
    pz = ZomboidRCON(ip='localhost', port=27015, password='myPassword')
    command = pz.serverMsg("You dead yet?")
    print(command.response)
    print(command.successful)
```

This example connects to a server running on your local machine and sends the message "You dead yet?".

Zomboid-rcon provides several built-in methods for common server management tasks, such as getting a list of connected players:

```python
from zomboid_rcon import ZomboidRCON

if __name__ == "__main__":
    pz = ZomboidRCON(ip='localhost', password='myPassword')
    
    print(pz.players().response)
```

This example prints a list of all players currently connected to the server.

<br>

# Available Commands

Zomboid-rcon provides several built-in methods for common server management tasks:

- ```serverMsg("Your message")``` : Global server messages
- ```players()``` : List all players online
- ```save()``` : Save the game in it's current state
- ```quit()``` : Save & shut down the game server
- ```showoptions()``` : Get game server settings
- ```help()``` : Get all command options: Note that only the listed commands have pre-build methods. For any not listed here please use the 'command' method in the following example.

<br>

You can execute any custom command using the command method:
```python
from zomboid_rcon import ZomboidRCON

if __name__ == "__main__":
    pz = ZomboidRCON(ip='localhost', password='myPassword')
    print(pz.command("command", "arg1", "arg2").response)
```

<br>

# Known Issues

Please note that zomboid-rcon uses the [timeout_decorator](https://pypi.org/project/timeout-decorator/) package, which is currently only compatible with Unix/Linux systems. As a result, **timeouts may cause errors on Windows machines**. We are actively working on finding an alternative solution for Windows users.

<br>

# Contributing

We welcome contributions from anyone! If you would like to contribute to the project, please open an issue or submit a pull request on [Github](https://github.com/JMWhitworth/zomboid_rcon).

<br>

# License

Zomboid-rcon is licensed under the GPL-3.0 license.
