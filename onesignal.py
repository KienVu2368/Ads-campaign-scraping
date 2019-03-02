import requests
from bs4 import BeautifulSoup
import pandas as pd

header = {

'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'max-age=0',
'cookie': <cookie>,
'referer': 'https://onesignal.com/<appid>',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'

}

s = requests.Session()

contents = []
sent_date = []
delivered = []
delivered_pct = []
unsubscribed = []
Error = []
clicked_pct = []

for j in range(1,<max rage>):    
    r = s.get('https://onesignal.com/apps/<app id>/notifications?page=' + str(j),
              headers = header)    
    soup = BeautifulSoup(r.content, 'html.parser')
    
    content = [i.get_text().replace('\n', "") for i in soup.find_all(class_='notification-content')]
    if len(content) == 0: break
    contents = contents + [i.get_text().replace('\n', "") for i in soup.find_all(class_='notification-content')]
    sent_date = sent_date + [i.get_text().replace('\n', "") for i in soup.find_all(class_='utc-date hidden')]
    clicked_pct = clicked_pct + [float(i.get_text().replace('\n', "").replace('%', '')) for i in soup.find_all(class_='conversion')]
    
    results = soup.find_all(class_='result')
    for rs in results:
        delivered.append(int(str(rs).split("'delivery-statistics-legend-description'>")[1].split(' Delivered')[0]))
        delivered_pct.append(float(str(rs).split("italicized subtext'>(")[1].split('%)<')[0]))
        
        try:
            unsubscribed.append(int(str(rs).split(' Failed (Unsubscribed)')[0].split("legend-description\'>")[2]))
        except:
            unsubscribed.append(0)
            
        try:
            Error.append(int(str(rs).split(" Failed (Error) <")[0].split("legend-description\'>")[3]))
        except:
            Error.append(0)

data = pd.DataFrame.from_dict({
    'contents': contents,
    'sent_date': sent_date,
    'delivered': delivered,
    'delivered_pct': delivered_pct,
    'unsubscribed': unsubscribed,
    'Error': Error,
    'clicked_pct': clicked_pct
})