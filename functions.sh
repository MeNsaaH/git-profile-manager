#! /bin/bash

GIT_PROFILE_DIR="$HOME/.gitprofiles"
# zshrc or bashrc or the likes
shell_config=
username=
email=
name=
# Used to search for where to replace current config
export_prefix="export GIT_CONFIG"

get_user_shell_profile_config() {
  if [ "$SHELL" = "/usr/bin/zsh" ];then 
    shell_config="$HOME/.zshrc"
  elif [ "$SHELL" = "/usr/bin/bash" ]; then
    shell_config="$HOME/.bashrc"
  fi
}


update_profile() {
  if grep -Fq "$export_prefix" $shell_config
  then
    sed -i "s|.*export GIT_CONFIG.*|$export_prefix=$GIT_PROFILE_DIR/$username|" "$shell_config"
  else
    echo "Git Runas config"
    echo "$export_prefix=$GIT_PROFILE_DIR/$username" >> $shell_config
  fi
}

get_user_shell_profile_config

