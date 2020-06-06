import os
import argparse
from git_profile_manager import utils 
from git_profile_manager.common_args import parent_parser


def current_profile(args):
    current_profile = utils.get_current_user(append_name=True)
    print("Current profile: %s" % current_profile)


def cmd():
    parser = argparse.ArgumentParser(
        description="Parses current-profile arguments",
        prog="git current-profile",
        parents=[parent_parser,]
    )

    args = parser.parse_args()
    current_profile(args)
