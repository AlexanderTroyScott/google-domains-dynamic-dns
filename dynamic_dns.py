import logging
import requests
import json
import os
import time

if bool(os.getenv('DEBUG')):
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
else:
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

def ip_get():
  headers = {'Accept':'application/json'}
  response = requests.get(url="http://ifconfig.co", headers=headers)
  if response.ok:
    ip = response.json()['ip']
    logging.debug('Returned IP: %s', ip)
  else:
    logging.error('Request for IP failed')
    ip = ''
  return ip

def ip_update(hostname, ip, username, password):
  response = requests.post(url=f"https://{username}:{password}@domains.google.com/nic/update?hostname={hostname}&myip={ip}")
  if response.ok:
    logging.info("A record %s updated to %s", hostname, ip)
  else:
    logging.warning(
      "Failed to update A record %s to %s, received status code %s and response %s",
       hostname, ip, response.status_code, response.text)

def main(hostname, username, password, time_sleep=3600):
   ip_expect = ip_get()
   while True:
      time.sleep(time_sleep)
      ip_return = ip_get()
      if (ip_expect != ip_return) and ip_expect:
         ip_update(
            hostname=hostname,
            ip=ip_return,
            username=username,
            password=password)
         ip_expect = ip_return

if __name__ == '__main__':
   with open(file='/run/secrets/username', mode='r', encoding='utf-8') as file:
      USERNAME = file.read()
   with open(file='/run/secrets/password', mode='r', encoding='utf-8') as file:
      PASSWORD = file.read()
   main(
      hostname = os.getenv('HOSTNAME'),
      username=USERNAME,
      password=PASSWORD,
      time_sleep=int(os.getenv('TIME_SLEEP')))
