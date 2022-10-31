import csv

proxylist = []
working_proxy_list = []

with open("proxy_data/proxies.csv", encoding="utf8") as f:
    all_rows = csv.reader(f)
    all_rows = list(all_rows)
    with open('proxy_data/proxies.txt','a') as p:
        for row in all_rows[1:]:
            try:
                p.write(f'{row[0]}:{row[7]}')
                p.write('\n')
            except:
                pass
