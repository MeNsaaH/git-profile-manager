""" Utility functions """
import os
import configparser
import sys
import subprocess


SHELL = os.getenv("SHELL", "")
HOME =  os.path.expanduser("~")
# Directory to store all git-profile-manager config
GIT_PROFILE_DIR = os.path.join(HOME, ".gitprofiles")

GLOBAL_GITCONFIG = os.path.join(GIT_PROFILE_DIR, "global")
# Store config for current active user
PROFILE_RC=os.path.join(GIT_PROFILE_DIR, ".profilerc")

def get_user_config(username):
    """ Get the path to user config """
    return os.path.join(GIT_PROFILE_DIR, username)

def user_exists(username):
    """ A user exists if the corresponding config file is present """
    return os.path.exists(get_user_config(username))

def get_unix_profile():
    """ get the profiles for the shell """
    profiles = []
    if "zsh" in SHELL:
        profile = os.path.join(HOME, ".zshrc")

    bash_profile = os.path.join(HOME, ".bashrc")
    if os.path.exists(bash_profile):
        profiles.append(bash_profile)
    return profiles

def user_input():
    """ User input string for python independent version """
    x = None
    if sys.version_info >= (3, 0):
        x = input
    else:
        x = raw_input
    return x


def exec_command(command):
    comp = subprocess.run([command,], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if comp.returncode != 0:
        sys.exit(1)
    return comp

def update_current_user(user):
    config = configparser.ConfigParser()
    config.read(PROFILE_RC)
    try:
        config["current"]["user"] = user
    except KeyError:
        config["current"] = {}
        config["current"]["user"] = user

    with open(PROFILE_RC, 'w') as configfile:
        config.write(configfile)


def get_current_user():
    """ Get the current active user """
    config = configparser.ConfigParser()
    config.read(PROFILE_RC)
    current_user = None
    try:
        current_user = config["current"]["user"]
    except KeyError:
        pass
    return current_user
        

