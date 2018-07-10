#! /usr/bin/env python

import xml.etree.ElementTree as tree
import csv
import sys 
    
# Parse XML and get root
nmap = tree.parse(sys.argv[1])
root_nmap = nmap.getroot()

# Open output CSV file
scan_table = open('table.csv', 'w')

# CSV writer
csv_writer = csv.writer(scan_table)
headings = []
info = {}


headings.append('Open Port')
headings.append('Hosts')
csv_writer.writerow(headings)

for host in root_nmap.findall('host'):
    ports = host.find('ports')
    for port in ports.findall('port'):
        key = port.get('portid') + '/' + port.get('protocol').upper()
        if key in info:
            info[key] = info[key] + ', ' + host.find('address').get('addr')
        else:
            info[key] = host.find('address').get('addr')

for key, value in sorted(info.items()):
    print(key + ': ' + value)
    out = []
    out.append(key)
    out.append(value)
    csv_writer.writerow(out)

scan_table.close()

