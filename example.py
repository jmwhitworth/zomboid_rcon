"""
Zomboid RCON: https://github.com/JMWhitworth/zomboid_rcon
    :copyright: (c) 2023 by JW: https://jackwhitworth.com
    :license: GPL-3.0, see LICENSE for more details.
"""


from zomboid_rcon       import ZomboidRCON
import os


# Sets to env variables for testing, with defaults set otherwise
IP          = os.getenv('IP')               if os.getenv('IP') is not None          else 'localhost'
PORT        = int(os.getenv('PORT'))        if os.getenv('PORT') is not None        else 27015
PASSWORD    = os.getenv('PASSWORD')         if os.getenv('PASSWORD') is not None    else 'myPassword'
RETRIES     = int(os.getenv('RETRIES'))     if os.getenv('RETRIES') is not None     else 5
LOGGING     = bool(os.getenv('LOGGING'))    if os.getenv('LOGGING') is not None     else False


if __name__ == "__main__":
    pz = ZomboidRCON(
        ip=IP,
        port=PORT,
        password=PASSWORD,
        retries=RETRIES,
        logging=LOGGING
    )
    
    # Shows list of all currently connected players
    print(pz.players().response)

    # Broadcasts message to all players
    print(pz.servermsg("This is how you all died!").response)

    # Shows list of current server options and values
    print(pz.showoptions().response)

    # For more, check the README.md
