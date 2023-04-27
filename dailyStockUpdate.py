#This project is only for the educational purpose.

from bs4 import BeautifulSoup
import requests
import datetime

from smtplib import SMTP_SSL
from email.message import EmailMessage
import pandas as pd
from pretty_html_table import build_table

URL = "https://www.hdfcsec.com/market/equity/top-gainer-nse?indicesCode=22115"

response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

list = soup.find("div", {"id": "marketTodaycompanyList"})
stocks = list.find_all("div", class_="companyList")
print(len(stocks))
data = []
count = 0
for s in stocks :
    company = s.find("span", class_="cd-heading").text
    price = s.find("div", class_="companyDetail").find_all("div", class_="col-md-4")
    ltp = price[0].find("span", class_="cd-val").text
    gain = price[1].find("span", class_="cd-val").text
    gain_per = price[2].find("span", class_="cd-val").text
    s_range = s.find("div", class_="sliderDiv").find("div", class_="row").find_all("div", class_="col-md-4")
    day_low = s_range[0].find("span", class_="cd-val").text
    day_high = s_range[2].find("span", class_="cd-val").text
    vol = s.find("div", class_="volDiv").find("div", class_="row").find("div", class_="col-md-5").find("span", class_="value").text
    
    row = [company, ltp, gain, gain_per, day_low, day_high, vol]
    #print(row)
    data.append(row)
    count += 1
    if count >= 10 :
        break

#print(data)
df = pd.DataFrame(data, columns=["Company", "LTP", "Gain", "Gain %", "Day Low", "Day High", "Volume"])
print(df)

name = "Nilesh"
body = """
<html>
<head>
</head>
<body>
Hi {1},
<br><br>
Please find below the Market Update of 10 stocks from Nifty 500. 
        {0}
<br/><br/>
--<br/>
Regards,<br/>
Nikhil Pawar,<br/>
nikhilpawar151@gmail.com
</body>
</html>
""".format(
    build_table(
        df,
        "blue_light",
        width="auto",
        font_family="Open Sans",
        font_size="13px",
        text_align="justify",
    ),
    name,
)

def send_mail(SENDER_EMAIL, RECEIVER_EMAIL, MAIL_PASSWORD, subject, body):
    msg = EmailMessage()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = subject
    msg.add_alternative(body, subtype="html")

    with SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SENDER_EMAIL, MAIL_PASSWORD)
        smtp.send_message(msg)
        smtp.close()
    print("Mail Sent Successfully")

today = datetime.date.today()
subject = f'Nifty 500 | Top 10 stocks | {today}'
SENDER_EMAIL = "<Add your email ID>"
MAIL_PASSWORD = "<Add your App Code from Gmail account>"
RECEIVER_EMAIL = "<Add receiver's email ID>"

#Create CSV file for the data.
file_name = f"{today}.csv"
df.to_csv(file_name, index=False)

send_mail(SENDER_EMAIL, RECEIVER_EMAIL, MAIL_PASSWORD, subject, body)