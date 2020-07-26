import bs4, requests, smtplib
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
getPage = requests.get('https://www.worldometers.info/coronavirus/country/china-hong-kong-sar/')
getPage.raise_for_status()
data = bs4.BeautifulSoup(getPage.text, 'html.parser')
from_address = 'email'
from_password = 'password'
num = data.select('.maincounter-number')
str1=str(num)
TAG_RE = re.compile(r'<[^>]+>')
new = TAG_RE.sub('', str1)
s='Subject: HK COVID UPDATE\n\n' + new
conn = smtplib.SMTP('smtp.gmail.com', 587) 
conn.ehlo()
conn.starttls() # starts tls encryption so the password will be encrypted.
conn.login(from_address, from_password )
conn.sendmail('fromemail', 'toemail', s)
conn.quit()
print('Sent email to fromemail\n')
