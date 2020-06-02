import sys
import os
import argparse
import utils 
from common_args import parent_parser


def list_profiles(args):


    current_user = utils.get_current_user()
    all_users = utils.get_all_users()
    for user in all_users:
        if user != current_user:
            print("%s" % user)
        else:
            print("%s (current user)" % user)
    print("")
        


def main():
    parser = argparse.ArgumentParser(
        description="Parses create-profile arguments",
        prog="git create-profile",
        parents=[parent_parser,]
    )

    args = parser.parse_args()
    list_profiles(args)

if __name__ == "__main__":
    main()
