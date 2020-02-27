import os

hostname="www.itmorelia.edu.mx"
respuesta=os.system("ping -c 1 "+hostname)
if respuesta==0:
	print(hostname+" funciona")
else:
	print(hostname+" no funciona")
red = "200.33.171.0/24"
os.system("nmap -sP "+ red)

"""
Nmap scan report for 200.33.171.3
Host is up (0.0057s latency).
Nmap scan report for 200.33.171.13
Host is up (0.014s latency).
Nmap scan report for 200.33.171.65
Host is up (0.0079s latency).
Nmap scan report for 200.33.171.66
Host is up (0.014s latency).
Nmap scan report for 200.33.171.99
Host is up (0.024s latency).
Nmap scan report for 200.33.171.115
Host is up (0.0074s latency).
Nmap scan report for 200.33.171.124
Host is up (0.0041s latency).
Nmap scan report for 200.33.171.125
Host is up (0.0040s latency).
Nmap scan report for 200.33.171.127
"""