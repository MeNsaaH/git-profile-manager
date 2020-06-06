import sys
import os
import argparse
from git_profile_manager import utils 
from git_profile_manager.common_args import parent_parser


def apply_profile(args):
    """ 
    Apply config to path https://git-scm.com/docs/git-config#_includes
    """
    if args.username:
        if not utils.user_exists(args.username):
            print("User %s does not exist" % args.username)
            sys.exit(1)
    else:
        args.username = utils.get_current_user()

    if not utils.is_email(args.username):
        args.username = utils.get_user_from_alias(args.username)

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

