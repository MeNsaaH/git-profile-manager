import sys
import os
import argparse
import utils 
from common_args import parent_parser


def use_profile(args):

    if not utils.user_exists(args.username):
        print("user profile %s does not exist" % args.username)
        sys.exit(1)

    utils.save_current_user_profile()
    #TODO update current user files
    utils.set_active_user(args.username)

    print("Git is now using %s profile\n" % args.username)
        


def main():
    parser = argparse.ArgumentParser(
        description="Parses create-profile arguments",
        prog="git create-profile",
        parents=[parent_parser,]
    )
    parser.add_argument(
       "username", 
        help="Username of user profile to be created"
    )

    args = parser.parse_args()
    use_profile(args)

if __name__ == "__main__":
    main()
