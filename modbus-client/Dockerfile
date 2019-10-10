FROM python

RUN mkdir /modbus

COPY modbus_client.py /modbus/modbus_client.py

RUN pip install pyModbusTCP

CMD python /modbus/modbus_client.py
