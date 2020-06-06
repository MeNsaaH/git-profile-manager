import sys
import os
import argparse
from git_profile_manager import utils 
from git_profile_manager.common_args import parent_parser


def create_profile(args):
    if not args.name:
        args.name = utils.user_input("Enter name (user.name): ", lower=False)

    if not args.email:
        args.email = utils.user_input("Enter email address (user.email): ")

    while utils.user_exists(args.email):
        args.email = utils.user_input("Email already exists.\nEnter Email: ")

    while not utils.is_email(args.email):
        args.email = utils.user_input("Email is invalid.\nEnter Email: ")

    while args.alias and utils.user_exists(args.alias, alias=True):
        args.alias = utils.user_input("Alias already exists.\nEnter another alias: ")

    print("Setting up User Profile ....\n")
    os.environ["GIT_CONFIG"] = utils.get_user_config_path(args.email)

    utils.exec_command(["git", "config", "user.email", "%s" % args.email])
    utils.exec_command(["git", "config", "user.name", "%s" % args.name])

    utils.set_active_user(args.email)
    print("Profile %s created" % args.email)

    if not args.alias:
        response = utils.user_input("Do you want to create an alias (short name) for user (Y/n)?: ")
        if response == "n":
            print("Git is now using %s profile" % args.email)
            sys.exit()
        args.alias = utils.user_input("Enter alias: ")
        while utils.user_exists(args.alias):
            args.alias = utils.user_input("Alias already exists.\nEnter another alias: ").lower()

    utils.add_alias(args.alias, args.email)
    print("Alias %s configured for %s" % (args.alias, args.email))
    print("Git is now using %s profile" % args.email)


def cmd():
    parser = argparse.ArgumentParser(
        description="Parses create-profile arguments",
        prog="git create-profile",
        parents=[parent_parser,]
    )
    parser.add_argument(
        "-a", "--alias", 
        help="A short name to be associated with profile to be created"
    )
    parser.add_argument(
        "-n", "--name", 
        help="Name of user to be created. This would be used as git user.name config"
    )
    parser.add_argument(
        "-e", "--email", 
        help="User profile email address. This would be used as git user.name config"
    )

    args = parser.parse_args()
    create_profile(args)
