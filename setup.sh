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
  mkdir -p "$HOME/.config/fish" # Ensure directory exists
  cp -r ./.config/fish/* "$HOME/.config/fish/" # Copy contents, not the directory itself

  log "Removing existing poshthemes..."
  rm -rf "$HOME/.poshthemes"

  log "Copying poshthemes..."
  cp -r ./.poshthemes "$HOME/"

  log "Setting permissions for poshthemes..."
  chmod u+rw "$HOME/.poshthemes/"*.omp.* || log "No matching poshthemes files to chmod."

  log "Copying .zshrc..."
  cp ./.zshrc "$HOME/"
}

select_oh_my_posh_theme() {
  log "Selecting Oh My Posh Theme..."
  local themes_dir="$HOME/.poshthemes"
  local theme_files=($(ls "$themes_dir" | grep -E '\.omp\.(json|yaml)
)) # Fixed regex
  local theme_names=()
  for file in "${theme_files[@]}"; do
    theme_names+=("$(basename "$file" | sed -E 's/\.omp\.(json|yaml)$//')")
  done

  local num_themes=${#theme_names[@]}
  local themes_per_page=60
  local num_pages=$(( (num_themes + themes_per_page - 1) / themes_per_page ))
  local current_page=0

  while true; do
    clear
    log "Available Oh My Posh Themes (Page $((current_page + 1))/$num_pages):"
    log "------------------------------------"

    local i=0
    local col1_themes=()
    local col2_themes=()

    local start_index=$((current_page * themes_per_page))
    local end_index=$((start_index + themes_per_page - 1))

    local idx="$start_index"
    while [ "$idx" -le "$end_index" ] && [ "$idx" -lt "$num_themes" ]; do # Fixed loop
      if [ $((i % 2)) -eq 0 ]; then
        col1_themes+=("${theme_names[idx]}")
      else
        col2_themes+=("${theme_names[idx]}")
      fi
      i=$((i + 1))
      idx=$((idx + 1))
    done

    local max_len=0
    for theme in "${col1_themes[@]}"; do
      if (( ${#theme} > max_len )); then
        max_len=${#theme}
      fi
    done

    local j=0
    while [ "$j" -lt "${#col1_themes[@]}" ]; do # Fixed second loop
      local theme1="${col1_themes[j]}"
      local theme2="${col2_themes[j]:-}" # Handle cases where col2 might be shorter
      printf "%-${max_len}s    %s\n" "$theme1" "$theme2"
      j=$((j + 1))
    done

    log "------------------------------------"
    if (( num_pages > 1 )); then
      if (( current_page < num_pages - 1 )); then
        log "Enter 'n' for next page, 'p' for previous page, or theme name to select."
      else
        log "Enter 'p' for previous page, or theme name to select."
      fi
    fi
    log "Enter theme name to select, or 'q' to quit:"
    read -r selected_theme_name

    if [[ "$selected_theme_name" == "q" ]]; then
      error_exit "Theme selection cancelled."
    elif [[ "$selected_theme_name" == "n" && current_page < num_pages - 1 ]]; then
      current_page=$((current_page + 1))
    elif [[ "$selected_theme_name" == "p" && current_page > 0 ]]; then
      current_page=$((current_page - 1))
    elif [[ " ${theme_names[*]} " =~ " ${selected_theme_name} " ]]; then
      log "You selected: $selected_theme_name"
      local selected_theme_file=""
      for file in "${theme_files[@]}"; do
        if [[ "$(basename "$file" | sed -E 's/\.omp\.(json|yaml)$//')" == "$selected_theme_name" ]]; then
          selected_theme_file="$file"
          break
        fi
      done

      if [[ -z "$selected_theme_file" ]]; then
        error_exit "Could not find file for selected theme: $selected_theme_name"
      fi

      local config_fish_path="$HOME/.config/fish/config.fish"
      local theme_line="oh-my-posh init fish --config \"$HOME/.poshthemes/$selected_theme_file\" | source"

      if grep -q "oh-my-posh init fish --config" "$config_fish_path"; then
        log "Updating Oh My Posh theme in $config_fish_path..."
        sed -i -E "s|oh-my-posh init fish --config ".*"|${theme_line}|" "$config_fish_path"
      else
        log "Adding Oh My Posh theme to $config_fish_path..."
        echo "$theme_line" >> "$config_fish_path"
      fi
      log "Oh My Posh theme set to $selected_theme_name."
      break
    else
      log "Invalid selection. Please try again."
      sleep 1
    fi
  done
}

change_shell() {
  local shell_path="/bin/fish"

  if ! command -v fish &>/dev/null;
    then
    error_exit "Fish shell is not installed at $shell_path"
  fi

  if command -v sudo &>/dev/null;
    then
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
  select_oh_my_posh_theme
  change_shell
  #cleanup_and_exit
}

main "$@"
