import unittest

from ocaboxapi import Observatory

logo1 = """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░     ░░░░░░░░░░   ░░░░░░░░░░  ░░░░░░░░░░░░░░     ░░░░░░░░░░░░░░░░░░░░░░░░░
▒▒▒   ▒▒▒▒   ▒▒▒▒   ▒▒▒   ▒▒▒▒▒▒  ▒  ▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒   ▒▒▒▒▒▒▒▒   ▒   ▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒   ▒▒▒▒▒▒▒▒▒▒▒  ▒▒▒   ▒▒▒▒▒   ▒▒▒▒▒   ▒▒▒
▓   ▓▓▓▓▓▓▓▓   ▓   ▓▓▓▓▓▓▓▓▓▓▓   ▓▓▓   ▓▓▓▓▓▓▓▓▓▓      ▓▓▓▓▓   ▓▓   ▓▓▓▓  ▓   ▓
▓   ▓▓▓▓▓▓▓▓   ▓   ▓▓▓▓▓▓▓▓▓▓       ▓   ▓▓▓▓▓▓▓▓▓  ▓▓▓▓   ▓   ▓▓▓▓   ▓▓▓▓  ▓▓▓▓
▓▓▓   ▓▓▓▓▓   ▓▓▓   ▓▓▓   ▓▓   ▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓  ▓▓▓▓▓  ▓▓   ▓▓   ▓▓▓  ▓▓   ▓
█████     █████████     ███   █████████   ███████    █   █████   █████   ███
███████████████████████████████████████████████████████████████████████████████
"""
logo2 = """
  .oooooo.     .oooooo.         .o.            oooooooooo.                        
 d8P'  `Y8b   d8P'  `Y8b       .888.           `888'   `Y8b                       
888      888 888              .8"888.           888     888  .ooooo.  oooo    ooo 
888      888 888             .8' `888.          888oooo888' d88' `88b  `88b..8P'  
888      888 888            .88ooo8888.         888    `88b 888   888    Y888'    
`88b    d88' `88b    ooo   .8'     `888.        888    .88P 888   888  .o8"'88b   
 `Y8bood8P'   `Y8bood8P'  o88o     o8888o      o888bood8P'  `Y8bod8P' o88'   888o 
 """

logo3 = """
 ██████   ██████  █████      ██████   ██████  ██   ██ 
██    ██ ██      ██   ██     ██   ██ ██    ██  ██ ██  
██    ██ ██      ███████     ██████  ██    ██   ███   
██    ██ ██      ██   ██     ██   ██ ██    ██  ██ ██  
 ██████   ██████ ██   ██     ██████   ██████  ██   ██                                                       
𝙊𝘾𝘼 𝘽𝙊𝙓
𝙾𝙲𝙰 𝙱𝙾𝚇
"""

class AlpacaConnectionTestCase(unittest.TestCase):
    def test_scanning(self):
        from ocaboxapi.connectors import AlpacaConnector
        con = AlpacaConnector()
        devices = con.scan_connection()
        for d in devices:
            print(d)
        print(logo1)
        print(logo2)
        print(logo3)
        # self.assertIsInstance(ob, Observatory)


if __name__ == '__main__':
    unittest.main()
