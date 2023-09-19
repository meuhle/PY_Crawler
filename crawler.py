import requests
from bs4 import BeautifulSoup
import re
import time

depth = 10
email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,4}"
regex = "^(?:(?=[a-z0-9@.!#$%&'*+/=?^_`{|}~-]{6,254}$)(?!.*\.\.)[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$"
regex_s = "^(?=[a-z0-9@.!#$%&'*+/=?^_`{|}~-]{6,254}$)[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*"
base_r = "^[a-zA-Z0-9][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

#URL = "https://www.uando.it/"
#URL = "https://www.medicalexpo.it/"
#URL = "https://www.simfer.it/"
#URL = "https://www.rehabweek.org/"
#URL = "https://www.medimec.it/"
URL = "https://elitemedicale.fr/"

link_list = []
emails = []
#resp = requests.get(URL)
#soup = BeautifulSoup(resp.content, 'html.parser')
#links = soup.find_all('a')

def scanURL(UR,cont):
    try:
        resp = requests.get(UR)
        soup = BeautifulSoup(resp.content, 'html.parser')
        links = soup.find_all('a')
        if (resp.status_code == 200):
            if cont < depth:
                cont += 1
                for link in links:
                    if link.get('href') != None:
                        if "twitter" not in link.get('href')and ".zip" not in link.get('href')and ".jpg" not in link.get('href')and ".png" not in link.get('href') and "youtube" not in link.get('href')and "spain" not in link.get('href') and "spain.kenes.com" not in link.get('href')and "facebook" not in link.get('href') :
                        #if "twitter" and "youtube"  and "spain" and "facebook" and "instagram"and "pdf"and "jpg"and "zip" not in link.get('href') :

                            if "https" in link.get('href'):
                                if link.get('href') not in link_list:
                                    #print(link.get('href'))
                                    link_list.append(link.get('href'))
                                    mails = re.findall(email_pattern, resp.text)
                                    for mail in mails:
                                        if mail not in emails:
                                            print(mail)
                                            emails.append(mail)
                                    #print(link.get('href'))
                                            time.sleep(0.2)
                                    scanURL(link.get('href'),cont)
    except Exception as e: print(e)

scanURL(URL,0)

#for mail in emails:
   # print(mail)
#for link in links:
    #print(link.get('href'))
#print(resp.status_code)
#print(resp.text)
