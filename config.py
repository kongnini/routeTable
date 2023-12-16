import json

def load_config(file_path):
    """ 加载配置文件 """
    with open(file_path, "r") as file:
        return json.load(file)
    
config = load_config("config.json")
DNS_SERVER = config["dns_server"]
DEFAULT_MAC = config["default_mac"]
DEFAULT_GATEWAY = config["default_gateway"]
POLLING_INTERVAL = config.get("polling_interval", 300)
ROUTES = config.get("routes", [])