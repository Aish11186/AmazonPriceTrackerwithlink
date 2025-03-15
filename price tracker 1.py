import requests 
from bs4 import BeautifulSoup
import smtplib
import schedule
import time      

URL= 'https://www.amazon.in/Fresh-Onion-1kg-Pack/dp/B07BG62MBV/ref=sr_1_1_f3_0o_fs?crid=1ITTDLKZPGJY&dib=eyJ2IjoiMSJ9.4eguaIy6zyytBGhlj2SQtF88nZ8GTGJeIW6ObBXoYVL_VnqtugBw0jt2EEaUqVJp2JEdQSC5XMw2PMhpnDuezMsVH5LD4Y57ChAfNWHND3eODjZxNizLsvqjLpzG70XcE5tfoCW7d5weJYbJkokiekT5z2ap-llzL3Hyzb5uDQ8wl8KLOKTaPOB8Ljtxw9e4B8JD7QgZXGqim2_ZCQWpc29Q3H7RtC5jRGtPYsJ7D7dgGcdA1gjtoQjZGTsYvZInGAtIhUQ-RLLJubH64UiShtj3xGiO9fMbnCN48cjCpHI.hvTdGbZSqkDgAw2B9sWiDU7yxNEZixhr7s8OmGByuTQ&dib_tag=se&keywords=onion&qid=1741878170&sprefix=onio%2Caps%2C351&sr=8-1&th=1'

headers = { "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 OPR/117.0.0.0'}

page= requests.get(URL, headers=headers)

#returns data from website

soup = BeautifulSoup(page.content, 'html.parser')

price = soup.find( class_= "a-price-whole").get_text()

convertedprice = float(price[0:2])


print (convertedprice)

def sendmail():
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('extra.ash1811@gmail.com','ajqp rhoa crow psqx')
    subject= "CHECK OUT THE PRICE!"
    body= 'price just dropped check out the link https://www.amazon.in/Fresh-Onion-1kg-Pack/dp/B07BG62MBV/ref=sr_1_1_f3_0o_fs?crid=1ITTDLKZPGJY&dib=eyJ2IjoiMSJ9.4eguaIy6zyytBGhlj2SQtF88nZ8GTGJeIW6ObBXoYVL_VnqtugBw0jt2EEaUqVJp2JEdQSC5XMw2PMhpnDuezMsVH5LD4Y57ChAfNWHND3eODjZxNizLsvqjLpzG70XcE5tfoCW7d5weJYbJkokiekT5z2ap-llzL3Hyzb5uDQ8wl8KLOKTaPOB8Ljtxw9e4B8JD7QgZXGqim2_ZCQWpc29Q3H7RtC5jRGtPYsJ7D7dgGcdA1gjtoQjZGTsYvZInGAtIhUQ-RLLJubH64UiShtj3xGiO9fMbnCN48cjCpHI.hvTdGbZSqkDgAw2B9sWiDU7yxNEZixhr7s8OmGByuTQ&dib_tag=se&keywords=onion&qid=1741878170&sprefix=onio%2Caps%2C351&sr=8-1&th=1'
    msg= f"subject:{subject}\n\n{body}"

    reciever1= input ("enter reciever")



    server.sendmail(
        'extra.ash1811@gmail.com',
        reciever1,
        msg

    )
    server.quit()

    
schedule.every(30).minutes.do(check_price)
print("bot checking")



idealprice= int(input('enter price'))
if (convertedprice<idealprice):
    sendmail()

print("mailsent")


