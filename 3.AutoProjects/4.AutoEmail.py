import yagmail

sender = 'f.liu2916@gmail.com'
receiver = 'f.liu2916@gmail.com'

subject = "This is the subject"

content = """
Here is the content of the email!
Hi!
"""

yag = yagmail.SMTP(user=sender, password=)
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Sent!")

# email with attachment
context_attached = [""""
Here is the content of the email!
Hi!                   
""", 'text.txt']

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEText
from email.mime.base import MIMEBase

sender = 'sender@gmail.com'
receiver = 'receiver@gmail.com'
password = 'pw'

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'Hello Again'

body = """"
<h2>Hi there<h2/>
There are only two cats flying today!
Let's hope for more!
"""

mimetext = MIMText(body, 'html')
message.attach(mimetext)

# add attachment file
# file path
attachment_path = 'tiger.jpeg'
# read file into object
attachment_file = open(attachment_path, 'rb')
# create payload
payload = MIMEbase('application', 'octate-stream')
# read file into payload object
payload.set_payload(attachment_file.read())
# configurate payload header
payload.add_header('Content-Disposition', 'attachment', filename=attachment_path)
# add payload into message
message.attach(payload)

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message.as_string())
server.quit()

# ---- Amazon Price Email Notifier ----
from selenium import webdriver

def get_driver():
# Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://www.amazon.com/PF-WaterWorks-PF0989-Disposal-Installation/dp/B078H38Q1M/")
  return driver

def main():
  driver = get_driver()
  # xpath was taken in Chrome by right-clicking
  # over <span aria-hidden="true">$15.12</span>
  # and then Copy -> xpath
  element = driver.find_element(by="xpath", value='//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[2]')
  # print('element', element.text)
  return element.text

def clean_price(raw):
    return float(raw.replace('$',''))

raw_price = main()
price = clean_price(raw_price)
