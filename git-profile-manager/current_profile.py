import os
import argparse
import utils 
from common_args import parent_parser


def current_profile(args):
    current_profile = utils.get_current_user()
    print("Current profile: %s" % current_profile)


def main():
    parser = argparse.ArgumentParser(
        description="Parses current-profile arguments",
        prog="git current-profile",
        parents=[parent_parser,]
    )

    args = parser.parse_args()
    current_profile(args)

if __name__ == "__main__":
    main()
