# Crie um código em Python que teste se o site python.org está acessível pelo computador usado.
import requests

site = requests.get('https://www.python.org')
if site.status_code == 200:
    print(f'\033[1;32mO site esta online\033[m')
else:
    print(f'\033[1;34mO site não esta recebendo funcionando\033[m')

