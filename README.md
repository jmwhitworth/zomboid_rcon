# zomboid-rcon version 0.2.2 (Beta)
 
A Python package for interacting with Project Zomboid Servers using RCON. [Pypi Package](https://pypi.org/project/zomboid-rcon/0.2.2/)

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
    print(command.success)
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
from zomboid_rcon       import ZomboidRCON

if __name__ == "__main__":
    pz = ZomboidRCON(
        ip='localhost',
        password='myPassword',
    )
    
    print(pz.players().response)
```



<br>

# To do:

- Add all possible commands
- Find alternate solution for timeouts for Windows
