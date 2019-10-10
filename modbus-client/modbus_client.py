#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Modbus/TCP client

from pyModbusTCP.client import ModbusClient
import socket
import time
from datetime import datetime
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
modbus_servers = []

logging.info('Starting scanning')

#scan hosts

for i in range(1,101):
    try:
        host = 'modbus_server_{}'.format(i)
        ip = socket.gethostbyname(host)
    except:
        pass
    else:
        modbus_servers.append({'host' : host, 'ip': ip, 'connection': None})

for ms in modbus_servers:
    ms['connection'] = ModbusClient(host=ip, port=5020)

logging.info('{} host(s) found ! Starting reading loop'.format(len(modbus_servers)))

#read registers for each host

while True:
    for ms in modbus_servers:
        c = ms['connection']
        if c.is_open():
           regs = c.read_holding_registers(0, 10)
           logging.info('Regs read from {}'.format(ms['ip']))
        else:
           logging.info('Trying to connect to : {}'.format(ms['ip']))
           c.open()
    time.sleep(2)
