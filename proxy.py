import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import certifi
import OpenSSL
print(OpenSSL.__file__)

# URL of the web page you want to extract
url = "https://www.google.com"

# initialize a session
session = requests.Session()
# set the User-agent as a regular browser
session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
html = session.get(url, verify=certifi.where()).content
soup = bs(html, "html.parser")
script_files = []

for script in soup.find_all("script"):
    if script.attrs.get("src"):
        # if the tag has the attribute 'src'
        script_url = urljoin(url, script.attrs.get("src"))
        script_files.append(script_url)

css_files = []

for css in soup.find_all("link"):
    if css.attrs.get("href"):
        # if the link tag has the 'href' attribute
        css_url = urljoin(url, css.attrs.get("href"))
        css_files.append(css_url)

# write file links into files
with open("javascript_files.txt", "w") as f:
    for js_file in script_files:
        print(js_file, file=f)

with open("css_files.txt", "w") as f:
    for css_file in css_files:
        print(css_file, file=f)