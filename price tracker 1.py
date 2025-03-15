import requests 
from bs4 import BeautifulSoup
import smtplib



URL= input ("enter amazon link of the product you want to track")

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
    body= 'price just dropped check out the link www.amazon.in'
    msg= f"subject:{subject}\n\n{body}"

    receiver1= input("enter mail")



    server.sendmail(
        'extra.ash1811@gmail.com',
        reciever1,
        msg

    )
    server.quit()


idealprice= int(input('enter price'))
if (convertedprice<idealprice):
    sendmail()

print("mailsent")


