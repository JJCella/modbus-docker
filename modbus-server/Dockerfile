FROM python

RUN mkdir /modbus

COPY modbus_server.py /modbus/modbus_server.py

RUN pip install pyModbusTCP

CMD python modbus/modbus_server.py
