import sys
import os
import argparse
from git_profile_manager import utils 
from git_profile_manager.common_args import parent_parser


def apply_profile(args):
    """ 
    Apply config to path https://git-scm.com/docs/git-config#_includes
    """
    if not args.username:
        args.username = utils.get_current_user()

    for d in args.dir:
        utils.apply_profile(d, args.username)

def cmd():
    parser = argparse.ArgumentParser(
        description="Parses apply-config",
        prog="git apply-profile",
        parents=[parent_parser,]
    )
    parser.add_argument(
       "dir",  nargs="+",
        help="Directory to apply profile to"
    )
    parser.add_argument(
       "-u", "--username",  
        help="user config to apply to directory"
    )

    args = parser.parse_args()
    apply_profile(args)

