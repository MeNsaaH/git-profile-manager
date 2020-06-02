import os
import argparse
from git_profile_manager import utils 
from git_profile_manager.common_args import parent_parser


def global_config(args):
    os.environ["GIT_CONFIG"] = utils.GLOBAL_GITCONFIG

    utils.exec_command(["git", "config", args.key, args.config])
    print("DONE")


def cmd():
    parser = argparse.ArgumentParser(
        description="Parses current-profile arguments",
        prog="git global-config",
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
