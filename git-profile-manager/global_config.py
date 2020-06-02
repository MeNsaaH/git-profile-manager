import os
import argparse
import utils 
from common_args import parent_parser


def global_config(args):
    os.environ["GIT_CONFIG"] = utils.GLOBAL_GITCONFIG

    utils.exec_command(["git", "config", args.key, args.config])
    print("DONE")


def main():
    parser = argparse.ArgumentParser(
        description="Parses current-profile arguments",
        prog="git current-profile",
        parents=[parent_parser,]
    )

    parser.add_argument(
        "key", 
        help="the git key for the config e.g user.name"
    )

    parser.add_argument(
        "config", 
        help="config to add to global config"
    )

    args = parser.parse_args()
    global_config(args)

if __name__ == "__main__":
    main()
