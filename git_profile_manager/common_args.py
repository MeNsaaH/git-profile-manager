""" commonly args shared by all commands """

import argparse
from git_profile_manager.__version__ import __version__

parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('-V', '--version', action="version", version="%(prog)s v" + __version__)

