import sys
import os
import argparse
import utils 
from common_args import parent_parser


def remove_profile(args):
    current_user = utils.get_current_user()

    args.username = args.username.lower()

    if not utils.user_exists(args.username):
        print("User %s does not exist" % args.username)
        sys.exit(1)

    confirm_delete = utils.user_input("Are you sure you want to remove %s profile? (Y/n): " % args.username).lower()
    if confirm_delete != "y":
        print("Operation aborted")
        sys.exit(0)

    if args.username == current_user:

        if args.force:
          print("You are deleting the active user, your Current profile will be set to global config")
          utils.set_active_user("global")

        else:
            print("You cannot delete the active user. Add the -f/--force flag to force remove") 
            sys.exit(0)
    os.remove(utils.get_user_config_path(args.username))
    print("Profile %s deleted" % args.username)


def main():
    parser = argparse.ArgumentParser(
        description="Parses remove-profile command",
        prog="git remove-profile",
        parents=[parent_parser,]
    )

    parser.add_argument(
        "-f", "--force", 
        action="store_true",
        help="Username of user profile to be created"
    )

    parser.add_argument(
        "username", 
        help="User to be removed"
    )

    args = parser.parse_args()
    remove_profile(args)

if __name__ == "__main__":
    main()
