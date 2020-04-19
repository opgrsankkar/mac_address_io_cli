FROM python:3.8

WORKDIR /usr/src/mac_address_lookup/

COPY src/ .

RUN chmod +x ./*.py

ENTRYPOINT [ "python", "main.py" ]