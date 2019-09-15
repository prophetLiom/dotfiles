import subprocess as sp

networks = sp.call('iwlist wlan0 scan')

print(networks)
