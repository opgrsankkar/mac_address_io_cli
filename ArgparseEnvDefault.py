# SO Question: https://stackoverflow.com/questions/10551117/setting-options-from-environment-variables-when-using-argparse
# SO Author: https://stackoverflow.com/users/445507/russell-heilling
import os
import argparse


class EnvDefault(argparse.Action):
    """Custom action for an argparse argument
    to check and use if corresponding Environment variable exists.
    """

    def __init__(self, envvar, required=True, default=None, **kwargs):
        if not default and envvar:
            if envvar in os.environ:
                default = os.environ[envvar]
        if required and default:
            required = False
        super(EnvDefault, self).__init__(default=default, required=required,
                                         **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)
