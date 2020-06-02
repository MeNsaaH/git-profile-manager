#!/usr/bin/env bash

{ # this ensures the entire script is downloaded #

GIT_PROFILE_DIR="$HOME/.gitprofiles"
GIT_PROFILE_BIN_DIR="$GIT_PROFILE_DIR/bin"
PROFILE_RC="$GIT_PROFILE_DIR/.profilerc"
global_git_config=
repo_url="https://github.com/mensaah/git-profile-manager.git"
# To know when operation is successful
success=1
# shell env config file (.bashrc, .zshrc)
shell_config=
# To know if operation is update or normal installation
update=0


clone_repo(){
  git clone --depth=1 $repo_url $1
  if [ $? -ne 0 ]; then
    success=0
    printf "Failed to Clone repository"
    exit
  fi
}

proceed_installation(){
  mkdir -p $GIT_PROFILE_BIN_DIR
  clone_repo $GIT_PROFILE_BIN_DIR
  
  if [ $update -eq 0 ]; then
    check_global_gitignore
    if [ $? -eq 0 ]; then
      printf "Existing git config found at $global_gitconfig, backing up\n"
      cp $global_gitconfig "$GIT_PROFILE_DIR/global"
    else
      touch "$GIT_PROFILE_DIR/global"
    fi
  fi

  # Create the .profile_rc file if it does not exists
  if [ ! -f "$PROFILE_RC" ]; then
    touch $PROFILE_RC
  fi

}


# Return 0 if git_global exists
check_global_gitignore(){
  local return_val=0
  if [ -f "$HOME/.gitconfig" ]; then
    global_gitconfig="$HOME/.gitconfig"
  elif [ -f "$HOME/config/.gitconfig" ]; then
    global_gitconfig="$HOME/config/.gitconfig"
  else
    return_val=1
  fi
  return $return_val
}


# Check for existing Git Profile manager installations
if [ -d "$GIT_PROFILE_BIN_DIR" ]; then
  read -p "Git Profile Manager has already been installed, do you want to update?: (Y/n)" REPLY
  REPLY=$(echo "$REPLY" |tr '[:upper:]' '[:lower:]')
  if [ "$REPLY" == "y" ]; then
    rm -rf "$GIT_PROFILE_BIN_DIR"
    update=1
    proceed_installation
  else
    printf "Installation aborted"
    exit 1
  fi
else
  proceed_installation
fi

# Load shell config file
if [[ "$SHELL" = "/usr/bin/zsh" || "$SHELL" = "/bin/zsh" ]]; then 
  shell_config="$HOME/.zshrc"
elif [[ "$SHELL" = "/usr/bin/bash" || "$SHELL" = "/bin/bash" ]]; then
  shell_config="$HOME/.bashrc"
fi

# Append to shell env only during installation and not update
if [ $update -ne 1 ]; then
  # Add file to load gitprofiles in shell env
  echo 'export GIT_PROFILE_BIN_DIR="$HOME/.gitprofiles/bin"  && \. "$GIT_PROFILE_BIN_DIR/profile-manager.sh" ' >> $shell_config
fi

if [ $success -eq 1 ]; then
  printf "\nInstallation completed. Run 'git create-profile' to create a new profile\n\n"
else
  printf "Installation Failed, check logs and try again\n\n"
fi

}
