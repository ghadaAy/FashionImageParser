import requests
from  concurrent.futures import ThreadPoolExecutor


proxylist = []
working_proxy_list = []
with open("proxy_data/proxies.txt",'r') as f:
    proxylist = f.readlines()

def extract_working_proxy(proxy):
    try:
        requests.get('https://www.bershka.com/es/en/3-pack-of-coloured-socks-c0p114441793.html?colorId=500',
        proxies={'http':proxy, 'https':proxy},
        timeout=3)
        working_proxy_list.append(proxy)
    except:
        pass
    return proxy

with ThreadPoolExecutor() as extractor:
    extractor.map(extract_working_proxy, proxylist)

with open("working_proxy.txt",'w') as w_p:
    w_p.write('\n'.join(working_proxy_list))

print('done')