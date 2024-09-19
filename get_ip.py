import requests
import ipaddress
import os


data={
	'cloudflare':['https://monitor.gacjie.cn/api/client/get_ip_address?cdn_server=1&type=v4','https://monitor.gacjie.cn/api/client/get_ip_address?cdn_server=1&type=v6'],
	'cloudfront':['https://monitor.gacjie.cn/api/client/get_ip_address?cdn_server=2&type=v4','https://monitor.gacjie.cn/api/client/get_ip_address?cdn_server=2&type=v6'],
	'gcore':['https://monitor.gacjie.cn/api/client/get_ip_address?cdn_server=3&type=v4','https://monitor.gacjie.cn/api/client/get_ip_address?cdn_server=3&type=v6'],
}
headers={
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}
for key,value in data.items():
	print(key)
	ips=''
	for x in value:
		get_info=requests.get(x,headers=headers).json()
		get_cm=get_info['info']['CM']
		get_cu=get_info['info']['CU']
		get_ct=get_info['info']['CT']
		get_info_list=get_cm+get_cu+get_ct
		# print(get_info_list)
		if get_info_list==[]:
			break
		for i in get_info_list:
			proxy_ip=i['ip']
			proxy_info=i['colo']
			try:
			    check_ip=ipaddress.IPv6Address(proxy_ip)
			    proxy_ip=f'[{proxy_ip}]'
			except Exception as e:
				pass
			ips=ips+f'{proxy_ip}:443#{proxy_info}\n'
	print(ips)
	with open(f'{key}-ip.txt','w') as file:
		file.write(ips)