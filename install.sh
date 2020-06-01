#! /bin/bash
set -e

GIT_PROFILE_BIN_DIR="$HOME/gitprofiles/bin"

clone_repo(){
  git clone --depth=1 https://github.com/mensaah/git-profile-manager.git $GIT_PROFILE_BIN_DIR
}

mkdir -p $GIT_PROFILE_BIN_DIR
clone_repo
