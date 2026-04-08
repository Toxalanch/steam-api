__version__ = '0.0.1'
__author__ = 'Toxalanch'

import os
from pathlib import Path
import yaml

_username: str = ""
_password: str = ""
_location: str = ""

def _startup():
    config_file = Path.cwd() / "config.yml"
    if not config_file.exists():
        with open(config_file, 'w') as f:
            _username = input("What is the steam username of the account?\n")
            _password = input("What is the steam password of the account?\n")
            quit = False
            while (not quit):
                _location = input("what is the location of steamcmd.exe? (leave out steamcmd.exe in the location)\n")
                file = os.path.abspath(_location)
                quit = os.path.isfile(file / _location)
            yaml.dump({
                'login': {
                    'username': _username,
                    'password': _password
                },
                'steamcmd location': _location
            }, f)
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
        _username = config['login']['username']
        _password = config['login']['password']
        _location = config['steamcmd location']