#!/usr/bin/env python3
import sys
import argparse
from os import linesep as os_linesep
from ArgparseEnvDefault import EnvDefault
from MACLookup import mac_lookup
from MACLookupException import MACLookupException as exception


""" CLI tool to lookup details on a MAC address from macaddress.io API

usage: main.py [-h] [-o OUTPUT_FORMAT] [-v] -a API_KEY MAC_ADDRESS

positional arguments:
  MAC_ADDRESS           MAC address or OUI to lookup in hex format

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_FORMAT, --output OUTPUT_FORMAT
                        Output format: text, verbose, json. Default: text
  -v, --verbose         Same as '-o verbose'. Takes precedence over -o
  -a API_KEY, --api_key API_KEY
                        Specify API Key from macaddress.io. You can either pass the API key as argument here or set environment variable MAC_ADDRESS_IO_API_KEY

"""


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Lookup details on a MAC address from macaddress.io API')
    parser.add_argument('-o', '--output', dest='output_format', default='text',
                        help="Output format: text, verbose, json. Default: text")
    parser.add_argument('-v', '--verbose', action='store_true', default=False,
                        help="Same as '-o verbose'. Takes precedence over -o")
    parser.add_argument('mac', metavar='MAC_ADDRESS',
                        help='MAC address or OUI to lookup in hex format')
    parser.add_argument('-a', '--api_key', action=EnvDefault, envvar='MAC_ADDRESS_IO_API_KEY',
                        help='''Specify API Key from macaddress.io.
                                You can either pass the API key as argument here
                                or set environment variable MAC_ADDRESS_IO_API_KEY''')
    args = parser.parse_args()
    if args.verbose:
        args.output_format = 'verbose'
    try:
        res = mac_lookup(args.mac, args.api_key, args.output_format)
        sys.stdout.write(res+ os_linesep)
    except exception as err:
        sys.stderr.write(err.msg + os_linesep)
        sys.exit(1)
