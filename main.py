import configparser
import json
import time
from routeTable.klog import logger
from routeTable.config import POLLING_INTERVAL,DNS_SERVER,DEFAULT_MAC
import dnstools.resolve as dnstools


def load_config(file_path):
    """ 加载配置文件 """
    with open(file_path, "r") as file:
        return json.load(file)

def main():
    config = load_config("config.json")
    logger.debug(f"DNS服务器: {DNS_SERVER} 默认网关: {DEFAULT_MAC}")
    
    while True:
        try:
            print("Performing some task...")
            time.sleep(POLLING_INTERVAL)
            dnstools.resolve_domains()
            pass
        except Exception as e:
            # 处理异常
            logger.error(f"发生异常: {e}")
        
        # 可以在这里添加一些等待时间，以免无限循环造成 CPU 占用
        time.sleep(1)    

if __name__ == "__main__":
    main()