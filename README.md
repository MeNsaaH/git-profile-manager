# Git Profile Manager
A git extension to allow you manage multiple git profiles on your workstation. User profiles can have independent configurations. They can also share configurations.


## Installation

To install or update git-profile-manager, you should run the install script. To do that, you may either download and run the script manually, or use the following cURL or Wget command:

```bash 
  curl -o- https://raw.githubusercontent.com/mensaah/git-profile-manager/master/install.sh | bash
```

```bash
  wget -qO- https://raw.githubusercontent.com/mensaah/git-profile-manager/master/install.sh | bash
```
Running either of the above commands downloads a script and runs it. The script clones the git-remote-manager repository to `~/.gitprofiles/bin`, and attempts to add the source lines from the snippet below to the correct profile file (`~/.bash_profile`, `~/.zshrc`, `~/.profile`, or `~/.bashrc`).

```bash
  export GIT_PROFILE_BIN_DIR="$HOME/.gitprofiles/bin"  && \. "$GIT_PROFILE_BIN_DIR/profile-manager.sh" # This loads git-profile-manager
```


NOTE: After installation, your current git config will be used as a shared configuration. All users inherit from the configuration

## Usage
After any commands (aside `current-profile` you have to source your shell environment (bashrc, zshrc) 

```bash
  source ~/.bashrc
  # If Zsh
  # source ~/.zshrc
```
(Working on a convenience fix for this)

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

### Remove Exisint Profile
To Remove an existing Profile:

```bash
  git remove-profile foo@bar.com
```

### Current Profile
To get the Current Profile:

```bash
  git current-profile
```

## TODO
- [ ] Autosource shell environment after running each command
- [ ] Add bash completions
- [ ] Add support for other shells
- [ ] Add windows support if possible
- [ ] Unset GIT_CONFIG env if current profile is removed or disallow removing current profile
