import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.facebook.com')
#except:
#    print('Deu erro!')
except urllib.error.URLError:
    print('O site não está acessível no momento.')
else:
    print('Consegui acessar o site com sucesso.')
#    print(site.read())    Lê todo o conteúdo HTML do site.
