FROM python:3.8

WORKDIR /usr/src/mac_address_lookup/

ADD main.py .
ADD ArgparseEnvDefault.py .
ADD MACLookup.py .
ADD MACLookupException.py .

RUN chmod +x ./*.py

ENTRYPOINT [ "python", "main.py" ]