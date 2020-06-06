import sys
import os
import argparse
from git_profile_manager import utils 
from git_profile_manager.common_args import parent_parser


def use_profile(args):

    if not utils.user_exists(args.username):
        print("user profile %s does not exist" % args.username)
        sys.exit(1)

    if not utils.is_email(args.username):
        args.username = utils.get_user_from_alias(args.username)
        if not args.username:
            print("Alias does not exist")
            sys.exit(1)
        if not utils.config_exists(args.username):
            print("Could not find config file for %s at %s" % (args.username, utils.get_user_config_path(args.username)))
            sys.exit(1)

    utils.save_current_user_profile()
    utils.set_active_user(args.username)

    print("Git is now using %s profile\n" % args.username)
        

def cmd():
    parser = argparse.ArgumentParser(
        description="Parses create-profile arguments",
        prog="git use-profile",
        parents=[parent_parser,]
    )
    parser.add_argument(
       "username", 
        help="Username of user profile to be created"
    )

    args = parser.parse_args()
    use_profile(args)
