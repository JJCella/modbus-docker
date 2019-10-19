FROM python

RUN mkdir /modbus

COPY modbus_client.py /modbus/modbus_client.py

RUN pip install pyModbusTCP docker

CMD ["python", "-u", "/modbus/modbus_client.py"]
