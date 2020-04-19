# MAC Address Lookup CLI tool

Command line tool to lookup details on a MAC address from [macaddress.io][1] API.<br/>
The tool needs an API Key from [macaddress.io][1] to make the request.<br/>

**Note:** Since API Key is tied to a user profile on [macaddress.io][1], the same is not included in this repository.

## Usage:

-   Clone this repository: `git clone https://github.com/opgrsankkar/mac_address_io_cli.git`
-   Move to cloned directory: `cd mac_address_io_cli/src`
-   Execute `main.py` as per below help output.

```
$ ./main.py --help
usage: main.py [-h] [-o OUTPUT_FORMAT] [-v] -a API_KEY MAC_ADDRESS

Lookup details on a MAC address from macaddress.io API

positional arguments:
  MAC_ADDRESS           MAC address or OUI to lookup in hex format

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_FORMAT, --output OUTPUT_FORMAT
                        Output format: text, verbose, json. Default: text
  -v, --verbose         Same as '-o verbose'. Takes precedence over -o
  -a API_KEY, --api_key API_KEY
                        Specify API Key from macaddress.io. You can either
                        pass the API key as argument here or set environment
                        variable MAC_ADDRESS_IO_API_KEY
```

## Advanced

### Dockerfile

A Dockerfile has been included to enable building a docker image to containerize this application.
The Dockerfile uses python:3.8 as the base image.

[1]: https://macaddress.io/api
