import os
import argparse
from git_profile_manager import utils 
from git_profile_manager.common_args import parent_parser


def create_profile(args):
    if not args.username:
        args.username = utils.user_input("Enter username: ").lower()
    if not args.email:
        args.email = utils.user_input("Enter email address (user.email): ")
    if not args.name:
        args.name = utils.user_input("Enter name (user.name): ")

    while utils.user_exists(args.username):
        args.username = utils.user_input("Username already exists.\nEnter username: ").lower()

    print("Setting up User Profile ....\n")
    os.environ["GIT_CONFIG"] = utils.get_user_config_path(args.username)

    utils.exec_command(["git", "config", "user.email", "%s" % args.email])
    utils.exec_command(["git", "config", "user.name", "%s" % args.username])

    utils.set_active_user(args.username)
    print("Profile %s created\nGit is now running as %s" % (args.username, args.username))


def cmd():
    parser = argparse.ArgumentParser(
        description="Parses create-profile arguments",
        prog="git create-profile",
        parents=[parent_parser,]
    )
    parser.add_argument(
        "-u", "--username", 
        help="Username of user profile to be created"
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
