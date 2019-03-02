import requests
from bs4 import BeautifulSoup
import pandas as pd

s = requests.Session()
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'}
r = s.get('https://<domain>.activehosted.com/admin/', headers = header)

login_data =  {'user': <user>, 'pass': <pass>, 'idt': ''}

header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'max-age=0',
'content-length': '45',
'content-type': 'application/x-www-form-urlencoded',
'origin': 'https://<domain>.activehosted.com',
'referer': 'https://<domain>.activehosted.com/admin/',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}

r = s.post('https://<domain>.activehosted.com/admin/login.php',
       headers = header,
       data=login_data)

r = s.get("https://<domain>.activehosted.com/admin/api.php?jq=1&f=report.report_campaigns&rand=0.6297052103720981&p[]=<page number>&p[]=01D&p[]=&p[]=0&p[]=%7C&p[]=0&p[]=0&p[]=undefined")