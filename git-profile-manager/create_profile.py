import argparse
import utils 
from common_args import parent_parser


def create_profile(args):
    if not args.username:
        args.username = utils.user_input("Enter username: ").lower()
    if not args.email:
        args.email = utils.user_input("Enter email address (user.email): ")
    if not args.name:
        args.name = utils.user_input("Enter name (user.name): ")

    while user_exists(args.username):
        args.username = utils.user_input("Username already exists.\nEnter username: ").lower()

    print("Setting up User Profile ....\n")
    os.environ["GIT_CONFIG"] = utils.get_user_config()

    utils.exec_command("git config user.name %s" % args.username)
    utils.exec_command("git config user.email %s" % args.email)

    update_current_user(username)


def main():
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

if __name__ == "__main__":
    main()
