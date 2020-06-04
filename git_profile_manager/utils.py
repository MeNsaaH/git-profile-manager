""" Utility functions """

import os
import shutil
import configparser
import sys
import subprocess


HOME =  os.path.expanduser("~")
# Directory to store all git-profile-manager config
GIT_PROFILE_DIR = os.path.join(HOME, ".gitprofiles")

GLOBAL_GITCONFIG = os.path.join(GIT_PROFILE_DIR, "global")
# Store config for current active user
PROFILE_RC=os.path.join(GIT_PROFILE_DIR, ".profilerc")

GIT_CONFIG = os.path.join(HOME, '.gitconfig')

def get_user_config_path(user):
    """ Get the path to user config """
    return os.path.join(GIT_PROFILE_DIR, user)


def get_user_from_config_path(path):
    """ Get user from path """
    return os.path.split(path)[-1]


def user_exists(user, alias=False):
    """ A user exists if the corresponding config file is present """
    exists = False
    config = configparser.ConfigParser()
    config.read(PROFILE_RC)
    return user in config["users"].keys() or os.path.exists(get_user_config_path(user))


def add_alias(alias, user):
    """ Add new alias to PROFILE_RC """
    config = configparser.ConfigParser()
    config.read(PROFILE_RC)
    config["users"][alias] = user

    with open(PROFILE_RC, 'w') as configfile:
        config.write(configfile)


def user_input(prompt, lower=True):
    """ User input string for python independent version """

    r = input(prompt)
    return r.lower() if lower else r

def exec_command(command):
    """ Executes a command and exit if it fails """
    comp = subprocess.run(command)
    if comp.returncode != 0:
        sys.exit(1)
    return comp

def update_current_user(user):
    """ update PROFILE_RC with to `user` """
    config = configparser.ConfigParser()
    config.read(PROFILE_RC)
    try:
        config["current"]["user"] = user
    except KeyError:
        config["current"] = {}
        config["current"]["user"] = user

    with open(PROFILE_RC, 'w') as configfile:
        config.write(configfile)


def set_active_user(user):
    """ set the current active user
    This updates GIT_CONFIG with user data and update PROFILE_RC to reflect user is in session
    """

    current_user = get_current_user()
    update_current_user(user)

    # load config and override global configuration
    config = configparser.ConfigParser()
    config.read(GLOBAL_GITCONFIG)

    config.read(get_user_config_path(user))

    with open(GIT_CONFIG, "w") as configfile:
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
        
def get_all_users():
    """ Get all users
    All files within the GIT_PROFILE_DIR are user data except the .profilerc and global
    """
    users = [f for f in os.listdir(GIT_PROFILE_DIR) if os.path.isfile(os.path.join(GIT_PROFILE_DIR, f)) and f not in [".profilerc", "global"]]
    return users

def save_current_user_profile():
    """ Save the config for the current user to personal config
    If git config had been executed, the GIT_CONFIG file must have changed, update the personal user's config 
    """
    current_user = get_current_user()

    # Remove entries that match in global config
    global_config = configparser.ConfigParser()
    global_config.read(GLOBAL_GITCONFIG)

    current_config = configparser.ConfigParser()
    current_config.read(GIT_CONFIG)

    # Use a different config to make modifications. current_config cannot be modified during iteration
    config = configparser.ConfigParser()
    config.read(GIT_CONFIG)

    # Delete every matching config that exists in global config
    for section in current_config:
        if section in global_config._sections.keys():
            for key, value in current_config[section].items():
                if key in global_config[section].keys():
                    if value == global_config[section][key]:
                        del config[section][key]

    # remove sections with no entry
    for section in current_config:
        if section != "DEFAULT" and len(current_config[section].keys()) == 0:
            del config[section]

    # Write current user config
    with open(get_user_config_path(current_user), "w") as configfile:
        config.write(configfile)

    
def setup():
    """ 
    Setup user machine for git-profile-manager. This backups the current config as global config, creates the necessary files
    """
    # create GIT_PROFILE_DIR and backup only when it doesn't exist. If it does, user may be upgrading
    if not os.path.exists(GIT_PROFILE_DIR):
        os.makedirs(GIT_PROFILE_DIR)

        if os.path.isfile(GIT_CONFIG):
            shutil.copyfile(GIT_CONFIG, GLOBAL_GITCONFIG)
        else:
            # create an empty global config file
            with open(GLOBAL_GITCONFIG, 'a'):
                os.utime(GLOBAL_GITCONFIG, None)

    # Create `users` entry in profilerc
    config = configparser.ConfigParser()
    config.read(PROFILE_RC)
    if "users" not in config._sections.keys():
        config["users"] = {}

    with open(PROFILE_RC, 'w') as configfile:
        config.write(configfile)




def apply_profile(path, user):
    """ Adds includeIf command to gitconfig for path """
    path = os.path.abspath(path)
    print(path)
    global_config = configparser.ConfigParser()
    global_config.read(GLOBAL_GITCONFIG)

    user_config_path = get_user_config_path(user)
    includeIf_key = "includeIf \"gitdir:%s\"" % path

    if not os.path.isdir(path):
        print("path %s does not exist" % path)
        return

    if includeIf_key in global_config._sections.keys():
        path_user = get_user_from_config_path(global_config[includeIf_key]["path"])
        response = user_input("Path is already configured to use %s, do you want to override (y/N)? " % path_user)
        if response != "y":
            print("Path %s configuration skipped" % path)
            return
    global_config[includeIf_key] = {}
    global_config[includeIf_key]["path"] = user_config_path

    with open(GLOBAL_GITCONFIG, "w") as configfile:
        global_config.write(configfile)
    print("Path %s configured to use %s config" % (path, user))
