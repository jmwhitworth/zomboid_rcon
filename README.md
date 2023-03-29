# zomboid-rcon version 0.2.1 (Beta)
 
A Python package for interacting with Project Zomboid Servers using RCON.

This project uses the timeout_decorator package which is Unix/Linux only. Timeouts will cause errors on Windows due to this.

<br>

# How to use

Example:
```
from zomboid_rcon import ZomboidRCON

if __name__ == "__main__":
    pz = ZomboidRCON(ip='localhost', password='myPassword')
    command = pz.serverMsg("You dead yet?")
    print(command.response)
    print(command.response)
```

Outputs:
```
Message sent.
True
```

<br>

# Available commands:

The follow commands are available through built-in methods:
- serverMsg
- players
- save
- quit
- help
- showoptions

Or execute any command using the command method:
```
from zomboid_rcon import ZomboidRCON

if __name__ == "__main__":
    pz = ZomboidRCON(ip='localhost', password='myPassword')
    command = pz.command("servermsg", "Hello!")
```



<br>

# To do:

- Add all possible commands
- Find alternate solution for timeouts for Windows