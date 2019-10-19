FROM python

RUN mkdir /modbus

COPY modbus_server.py /modbus/modbus_server.py

RUN pip install pyModbusTCP

CMD ["python", "-u", "modbus/modbus_server.py"]
