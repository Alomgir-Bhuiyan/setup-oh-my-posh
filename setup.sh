#!/bin/bash
set -euo pipefail

log() {
  echo "[INFO] $*"
}

error_exit() {
  echo "[ERROR] $*" >&2
  exit 1
}

copy_configs() {
  log "Removing existing fish config..."
  rm -rf "$HOME/.config/fish"

  log "Copying fish config..."
  mkdir $HOME/.config/fish
  cp -r ./.config/fish "$HOME/.config/fish/"

  log "Removing existing poshthemes..."
  rm -rf "$HOME/.poshthemes"

  log "Copying poshthemes..."
  cp -r ./.poshthemes "$HOME/"

  log "Setting permissions for poshthemes..."
  chmod u+rw "$HOME/.poshthemes/"*.omp.* || log "No matching poshthemes files to chmod."

  log "Copying .zshrc..."
  cp ./.zshrc "$HOME/"
}

change_shell() {
  local shell_path="/bin/fish"

  if ! command -v fish &>/dev/null; then
    error_exit "Fish shell is not installed at $shell_path"
  fi

  if command -v sudo &>/dev/null; then
    log "Changing default shell with sudo..."
    sudo chsh -s "$shell_path"
  else
    log "Changing default shell without sudo..."
    chsh -s "$shell_path"
  fi
}

cleanup_and_exit() {
  local dir
  dir="$(cd "$(dirname "$0")" && pwd)"

  log "Changing to parent directory..."
  cd "$dir/.."

  log "Removing script directory: $dir"
  rm -rf "$dir"

  log "Killing parent shell to close current session..."
  kill -9 $PPID
}

main() {
  copy_configs
  change_shell
  cleanup_and_exit
}

main "$@"
