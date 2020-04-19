import json
import urllib.parse
import urllib.request
from os import linesep as os_linesep
from urllib.error import HTTPError
from MACLookupException import MACLookupException as exception

URL = 'https://api.macaddress.io/v1'


def format_output(output, output_format):
    if output_format == 'json':
        return json.dumps(output)
    elif output_format == 'text':
        return output['vendorDetails']['companyName']
    elif output_format == 'verbose':
        return (
            "OUI: {o[vendorDetails][oui]}{l}"
            "Is private: {o[vendorDetails][isPrivate]}{l}"
            "Is valid: {o[macAddressDetails][isValid]}{l}"
            "Company name: {o[vendorDetails][companyName]}{l}"
            "Company address: {o[vendorDetails][companyAddress]}{l}"
            "Country code: {o[vendorDetails][countryCode]}{l}"
            "Left border: {o[blockDetails][borderLeft]}{l}"
            "Right border: {o[blockDetails][borderRight]}{l}"
            "Block size: {o[blockDetails][blockSize]}{l}"
            "Assignment Block size: {o[blockDetails][assignmentBlockSize]}{l}"
            "Created at: {o[blockDetails][dateCreated]}{l}"
            "Updated at: {o[blockDetails][dateUpdated]}{l}"
            "Transmission type: {o[macAddressDetails][transmissionType]}{l}"
            "Administration type: {o[macAddressDetails][administrationType]}{l}"
        ).format(o=output, l=os_linesep)
    else:
        raise exception("Invalid Output format requested")


def mac_lookup(mac, api_key, output_format='text'):
    """Lookup details on a MAC address from macaddress.io API

    Arguments:
        mac {str} -- MAC Address or OUI to lookup
        api_key {str} -- API Key from macaddress.io

    Keyword Arguments:
        output_format {str} -- default: 'text'

    Returns:
        str -- MAC address lookup output in required format
    """

    query_params = {
        'search': mac,
        'apiKey': api_key,
        'output': 'json'
    }
    encoded_query_params = urllib.parse.urlencode(query_params)
    try:
        res = urllib.request.urlopen(URL + '?' + encoded_query_params).read()
        formatted_res = format_output(
            json.loads(res.decode('utf-8')), output_format)
        return formatted_res
    except HTTPError as err:
        raise exception(err)
