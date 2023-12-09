import json
import platform

def detect_os():
    system = platform.system()
    
    if system == 'Windows':
        # Do something for Windows
        config_file = "C:\\Users\\benwa\\etc\\secondchance_config.json"
        # Your Windows-specific code here
        
    elif system == 'Linux':
        distro = platform.linux_distribution()
        if 'Ubuntu' in distro:
            # Do something for Ubuntu
            config_file = '/etc/secondchance_config.json'
            # Your Ubuntu-specific code here
        
    else:
        print("Unknown or unsupported operating system")

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