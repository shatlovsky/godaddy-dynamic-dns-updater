#!/usr/bin/env python3

import configparser
import json
import os
import sys
import urllib.request

class GoDaddyDNSUpdater:

    def __init__(self, mode='production'):
        config = configparser.ConfigParser()
        config.read(['gddu.conf', os.path.expanduser('~/.gddu.conf'),'/etc/gddu.conf'])

        self.key      = config.get(mode, 'api_key')
        self.secret   = config.get(mode, 'api_secret')
        self.domain   = config.get(mode, 'domain')
        self.hostname = config.get(mode, 'hostname')
        self.base_url = config.get(mode, 'api_url')
        self.real_ip  = self.get_real_ip()


    def get_real_ip(self):
        url = 'http://whatismyip.akamai.com/'
        req = urllib.request.Request(url)
        res = urllib.request.urlopen(req).read().decode('UTF-8')
        return res

    def update_a_record(self):
        url = '{}/v1/domains/{}/records/A/{}'.format(self.base_url, self.domain, self.hostname)

        headers = {
            'Accept':        'application/json',
            'Authorization': 'sso-key {}:{}'.format(self.key, self.secret),
            'Content-Type':  'application/json',
        }
        data = json.dumps([{
            "name": self.hostname,
            "ttl":  600,
            "type": "A",
            "data": self.real_ip,
        }]).encode('UTF-8')

        req = urllib.request.Request(url, data, headers, None, False, 'PUT')
        res = urllib.request.urlopen(req)
        res.read()

def main():
    GoDaddyDNSUpdater().update_a_record()

if __name__ == "__main__":
    main()
