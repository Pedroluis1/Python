import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.github.com')
except:
    print('Deu erro')
else:
    print('tudo okay')