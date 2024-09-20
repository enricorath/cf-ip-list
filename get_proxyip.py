import requests
import ipaddress
import os
import json
import random
import zipfile
import re
from pathlib import Path

headers={
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}
def get_cf_proxyip():
	url='https://zip.baipiao.eu.org'
	data=requests.get(url,headers=headers)
	with open('cloudflare.zip','wb') as file:
		file.write(data.content)
		file.close()
	with zipfile.ZipFile('cloudflare.zip', 'r') as zip_ref:
		zip_ref.extractall('cf') 
	# 目标文件夹路径
	folder_path = Path('./cf')
	# 遍历文件夹中的所有文件
	tls_json=[]
	notls_json=[]
	for file_path in folder_path.rglob('*'):
	    ports=re.split(r'-',file_path.stem)[-1]
	    with open(file_path,'r',encoding='utf-8') as file:
	    	text=file.read()
	    	# news_text=text.replace('\n',f':{ports}\n')
	    	news_text=re.split(r'\n',text)
	    	if ports=='443':
	    		for i in news_text:
	    			ip_info=requests.get(f'https://ipinfo.io/{i}/json').json()
	    			tls_json.append({'ip':i,'port':ports,'colo':f'{ip_info['country']}-{ip_info['city']}-{ip_info['org']}'})
	    	else:
	    		for i in news_text:
	    			ip_info=requests.get(f'https://ipinfo.io/{i}/json').json()
	    			tls_json.append({'ip':i,'port':ports,'colo':f'{ip_info['country']}-{ip_info['city']}-{ip_info['org']}'})
	    	file.close()
	    print(f'{ports}\n{text}')
	file_info={'cloudflare-proxyip':json1,'cloudflare-proxyip-notls':json2}
	for filename,ip_info in file_info:
		ips=''
		for j in ip_info:
			ips=ips+f'{j['ip']}:{j['port']}#{j[colo]}'
		with open(f'{filename}.txt','w') as file:
			file.write(ips)
			file.close()
	os.remove('./cloudflare.zip')
	os.remkdir('./cf')
get_cf_proxyip()