import os
import sys
import time

saved_profiles = os.popen('netsh wlan show profiles').read()
# print(saved_profiles)
available_profiles = os.popen('netsh wlan show networks').read()
# print(available_profiles)

preferred_ssid = 'Xender_AP4a48'
response = os.popen("netsh wlan disconnect").read()
print(response)

if preferred_ssid not in saved_profiles:
    print("Profile for " + preferred_ssid + "is not saved in system")
    print("Sorry but can't establish the connection")
    sys.exit()
else:
    print("Profile for " + preferred_ssid + " is saved in system")

time.sleep(5)
while True:
    avail = os.popen('netsh wlan show networks').read()
    if preferred_ssid in avail:
        print('Found')
        break

print('---Connecting---')
resp = os.popen('netsh wlan connect name='+'"'+preferred_ssid+'"').read()
print(resp)