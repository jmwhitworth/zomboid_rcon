"""
Zomboid RCON: https://github.com/JMWhitworth/zomboid_rcon
    :copyright: (c) 2023 by JW: https://jackwhitworth.com
    :license: GPL-3.0, see LICENSE for more details.
"""


from zomboid_rcon       import ZomboidRCON

if __name__ == "__main__":
    pz = ZomboidRCON(
        ip='localhost',
        password='myPassword',
    )
    
    print(pz.players().response)
