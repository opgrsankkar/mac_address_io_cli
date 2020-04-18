from urllib.error import HTTPError


class MACLookupException (Exception):
    def __init__(self, err):
        self.AccessRestrictedError = False
        if(isinstance(err, HTTPError)):
            if err.code == 401:
                self.msg = 'Access Restricted. Please verify your API_KEY'
            elif err.code == 402:
                self.msg = 'Access Restricted. Please check your credit balance'
            elif err.code == 422:
                self.msg = 'Invalid MAC or OUI provided'
            else:
                self.msg = 'Server Error. Please try again later'
        else:
            self.msg = err
