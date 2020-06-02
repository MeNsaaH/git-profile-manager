# Git Profile Manager
A git extension to allow you manage multiple git profiles on your workstation. User profiles can have independent configurations. They can also share configurations.


## Installation
Git Profile Manager is dependent on python 3

### using Pip
Git-profile-manager can be installed using the python `pip` tool.

```bash
pip3 install git-profile-manager

# pip install git-profile-manager

````

It can also be installed using install script. To do that, you may either download and run the script manually, or use the following cURL or Wget command:

NOTE: After installation, your current git config will be used as a shared configuration. All users inherit from the configuration

## Usage

### Create Profile
To create a profile
```bash
  git create-profile <username>

  # who says username's are restricted to names, you can use emails
  git create-profile foo@bar.com
```

To Configure profile: 

```bash
  # Sets up ssh for that user
  git config core.sshCommand "ssh -i /full/path/to/id_a/id_rsa"
```
All git config after setting/creating profiles are stored under the user config. All global configurations are also available to the current profile, so your aliases get to work. In case of same config, the config of the profile is used

#### Global Configuration
To add configurations that would be shared by all users:
```bash
git global-config core.sshCommand "ssh -i /full/path/to/id_rsa"
```
User's configuration always override global configuration

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
