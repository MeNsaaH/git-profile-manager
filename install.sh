#! /bin/bash

GIT_PROFILE_DIR="$HOME/.gitprofiles"
GIT_PROFILE_BIN_DIR="$GIT_PROFILE_DIR/bin"
global_git_config=
repo_url="https://github.com/mensaah/git-profile-manager.git"
success=1


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
  
  check_global_gitignore
  if [ $? -eq 0 ]; then
    printf "Existing git config found at $global_gitconfig, backing up"
    cp $global_gitconfig "$GIT_PROFILE_DIR/global"
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
  return return_val
}


# Check for existing Git Profile manager installations
if [ -d $GIT_PROFILE_BIN_DIR ]; then
  read -p "Git Profile Manager has already been installed, do you want to update?: (Y/n)" REPLY
  REPLY=$(echo "$REPLY" |tr '[:upper:]' '[:lower:]')
  if [ "$REPLY" != "y" ]; then
    proceed_installation
  else
    printf "installation aborted"
    exit 1
  fi
else
  proceed_installation
fi

export PATH=$PATH:$GIT_PROFILE_BIN_DIR

if [ $success -eq 1 ]; then
  printf "\nInstallation completed. Run 'git create-profile' to create a new profile"
else
  printf "Installation Failed, check logs and try again"
fi

