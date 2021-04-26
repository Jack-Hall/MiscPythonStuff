import requests

import smtplib
import time

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup 

def sendMail(subject, message):
     username = 'itemsyouwant.noreply@gmail.com'
     password = "Proj2054"
     Sendto = "ojackh54@gmail.com"
     s = smtplib.SMTP(host="smtp.gmail.com", port=587)
     s.starttls()
     s.login(username, password)
     msg = MIMEMultipart()
     msg['From'] = username
     msg['To'] = Sendto
     msg['Subject'] = ("Here's an ad for a " + subject)
     msg.attach(MIMEText(message, 'plain'))
     s.send_message(msg)
     del msg
     s.quit()
for k in range (100):
    url = "https://www.kijiji.ca/b-calgary/l1700199?dc=true"
    page = requests.get(url)
    src = page.content
    soup = BeautifulSoup(src, features="html.parser")
    divs = soup.find_all('div', class_= "clearfix" )
    titles = []
    times = []
    prices =[]
    tlinks = []
    links = []
    descripts = []
    for div in divs:
        descripts.append(div.find('div', class_= "description" ))
        titles.append(div.find('div', class_= "title" ))
        times.append(div.find('span', class_= 'date-posted'))
        prices.append(div.find('div', class_="price"))
        tlinks.append(div.find('a'))
    for tag in tlinks:
        link = tag.get('href', None)
        links.append(link)

    for i in range(6):
        del titles[0]
        del times[0]
        del prices[0]
        del links[0]
        del descripts[0]
    print(len(links))
    print(links)
    print(len(titles))
    for i in range(20):
      print(titles[i].text.strip(), "\n", times[i].text.strip(), "\n", prices[i].text.strip(), "\n")
    keywords = [" table", "chair", "work", "pixel", "barrel"]
    for title, price, link, descript in zip(titles, prices, links, descripts):
        for keyword in keywords:
            if keyword in title.text.strip().lower():
                print("found one")
                info = (title.text.strip() + "\n " + descript.text.strip() + price.text + "\n" + ("Kijiji.ca" +link))
                sendMail(keyword, info)
            
    time.sleep(60)

