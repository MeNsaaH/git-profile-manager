""" commonly args shared by all commands """

import argparse
from __version__ import __version__

parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('--version')

parent_parser.set_defaults(version=__version__)
