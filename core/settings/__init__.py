import json
import platform
from distro import linux_distribution

def detect_os():
    system = platform.system()
    
    if system == 'Windows':
        # Do something for Windows
        config_file = "C:\\Users\\benwa\\etc\\secondchance_config.json"
        # Your Windows-specific code here
            
    else:
        config_file = '/etc/secondchance_config.json'


    return config_file


CONFIG_FILE = detect_os()

try:
    with open(CONFIG_FILE) as config_file:
        config = json.load(config_file)
        config['PROD']
    from .prod import *


except KeyError:
    from .dev import *

SECRET_KEY = config['SECRET_KEY']