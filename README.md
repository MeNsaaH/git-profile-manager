# Git Profile Manager
A git extension to allow you manage multiple git profiles on your workstation. User profiles can have independent configurations. They can also share configurations.

[![Python 3](https://img.shields.io/badge/python-3-blue)](https://www.python.org/downloads/)
[![PyPI version](https://badge.fury.io/py/git-profile-manager.png)](https://badge.fury.io/py/git-profile-manager)
[![Build Status](https://travis-ci.com/mensaah/git-profile-manager.svg?branch=master)](https://travis-ci.com/mensaah/git-profile-manager)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
 
<hr/>

## Installation

### using Pip
Git-profile-manager can be installed using the python `pip` tool.

```bash
pip3 install git-profile-manager

# pip install git-profile-manager

## Upgrade
pip3 install git-profile-manager --upgrade

````

NOTE: After installation, your current git config will be used as a shared configuration. All users inherit from the configuration

## Usage

### Create Profile
To create a profile
```bash
  git create-profile 

  git create-profile -e foo@bar.com -n "Foo Bar"
```

To Configure profile: 

```bash
  # Sets up ssh for that user
  git config --global core.sshCommand "ssh -i /full/path/to/id_a/id_rsa"
```
NOTE: Git Profile Manager stores the user config as global config. Hence all configurations must carry the `--global` flag. That means running config without the `--global` flag creates a local config that overrides values set on user config
```bash
  # Sets up ssh for that user
  # Set config for present repository
  # This Config overrides the user profile created config value for core.sshCommand
  git config core.sshCommand "ssh -i /full/path/to/id_a/id_rsa"
```

All initial global configurations are added to the user config. For conflicts, the user's config override the global config. 


#### Global Configuration
To add configurations that would be shared by all users:
```bash
  git global-config core.sshCommand "ssh -i /full/path/to/id_rsa"
```
User's configuration always override global configuration

### Apply profile
Applies a profile to a particular directory. Once applied, any repository within the directory uses the config. 

```bash
  # Applies current user profile 
  git apply-profile /home/user/company

  # Applies specified user profile
  git apply-profile /home/user/personal -u personal
```
implemented using https://git-scm.com/docs/git-config#_conditional_includes

### Switch between Profiles
To Switch Profile:

```bash
  git use-profile foo@bar.com
```

### Remove Existing Profile
To Remove an existing Profile:

```bash
  git remove-profile foo@bar.com
```

### Current Profile
To get the Current Profile:

```bash
  git current-profile
```
### List Profiles
To list the Current Profile:

```bash
  git list-profiles
```

## TODO
- [ ] Add bash completions
- [ ] Check and add windows compatibility
- [ ] Tests
