import dns.resolver
import json
from routeTable.klog import logger
from routeTable.main import DNS_SERVER, DEFAULT_MAC
from routeTable.config import DNS_SERVER, DEFAULT_MAC,DEFAULT_GATEWAY, ROUTES


def get_ips():
    new_resolved_ips = resolve_domains()
    changes = compare_dns_resolutions(new_resolved_ips)
    try:
        with open('old_resolved_ips.json', 'w') as file:
            json.dump(new_resolved_ips, file)
    except OSError as e:  
        logger.error(f"无法写入到文件old_resolved_ips.json: {e}")
    return changes



def resolve_domains():
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [DNS_SERVER]
    resolved_ips = {}
    for route in ROUTES:
        domain = route["domain"]
        # gateway = route["gateway"]
        # interface = route["interface_mac"]
        gateway = route.get("gateway", DEFAULT_GATEWAY)
        interface = route.get("interface_mac", DEFAULT_MAC)
        try:
            answers = resolver.resolve(domain)
            ips = [answer.to_text() for answer in answers]
            resolved_ips[domain] = {"ips": ips, "gateway": gateway, "interface": interface}
            logger.debug(f"domain: {domain}, ips: {ips} ,gateway: {gateway}, interface: {interface}")
        except Exception as e:
            logger.error(f"发生异常: domain:{domain},{e}")
    return resolved_ips

def compare_dns_resolutions(new_resolved_ips):
    if new_resolved_ips is None:
        return None
    elif len(new_resolved_ips) == 0:
        return None
    try:
        with open('old_resolved_ips.json', 'r') as file:
            old_resolved_ips = json.load(file)
    except FileNotFoundError:
        old_resolved_ips = {}
    changes = {'add': [], 'remove': []}
    for domain, new_ips, gateway, interface in new_resolved_ips.items():
        old_ips = old_resolved_ips.get(domain, {}).get('ips', [])
        # 查找新增的IP
        for ip in new_ips:
            if ip not in old_ips:
                changes['add'].append({'ip': ip, 'gateway': gateway, 'interface': interface})
        # 查找移除的IP
        for ip in old_ips:
            if ip not in new_ips:
                changes['remove'].append({'ip': ip})
    return changes

