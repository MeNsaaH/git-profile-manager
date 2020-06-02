#! /bin/bash

GIT_PROFILE_DIR="$HOME/.gitprofiles"
# Store details of the current profile
PROFILE_RC="$GIT_PROFILE_DIR/.profilerc"
# zshrc or bashrc or the likes
shell_config=
username=
email=
name=
# Used to search for where to replace current config
export_prefix="export GIT_CONFIG"

# LoadUP appropriate variables
setup_env() {
  # Load shell config file
  if [ "$SHELL" = "/usr/bin/zsh" ];then 
    shell_config="$HOME/.zshrc"
  elif [ "$SHELL" = "/usr/bin/bash" ]; then
    shell_config="$HOME/.bashrc"
  fi

  # Check if git-profile-manager is properly installed
  if [ ! -d $GIT_PROFILE_DIR ]; then
    printf "Git profile manager is not properly installed. Visit https://github.com/mensaah/git-profile-manager for how to install"
    exit
  fi
}

# Set the git config to new user's config
update_profile() {
  local username=$1
  if grep -Fq "CURRENT_PROFILE" $PROFILE_RC
  then
    sed -i "s|.*CURRENT_PROFILE.*|CURRENT_PROFILE=$username|" "$PROFILE_RC"
  else
    printf "CURRENT_PROFILE=$username" >> $PROFILE_RC
  fi
  # Copy global profile to git config location and append user config at the bottom
  cp "$GIT_PROFILE_DIR/global" "$HOME/.gitconfig"
  cat $GIT_PROFILE_DIR/$username >> "$HOME/.gitconfig"
}

get_current_profile(){
  # Maybe use source and load the variables directly
  #  source $PROFILE_RC
  current_profile=$(grep  'CURRENT_PROFILE' $PROFILE_RC)
  IFS='='
  read -ra ADDR <<< "$current_profile"
  username="${ADDR[-1]}"
}

setup_env

