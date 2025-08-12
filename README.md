# Tiwahu-Config

Your Zsh and Fish shell configuration with Oh-My-Posh.

## Quick Install

1.  **Install shell (choose one):**

    ```bash
    # For Debian/Ubuntu
    sudo apt update && sudo apt install zsh fish -y

    # For Arch Linux
    sudo pacman -Syu zsh fish
    ```

2.  **Install Oh-My-Posh and setup config:**

    ```bash
    curl -s https://ohmyposh.dev/install.sh | bash -s && \
    git clone https://github.com/Alomgir-Bhuiyan/tiwahu-config && \
    cd tiwahu-config && \
    chmod +x setup.sh && \
    ./setup.sh
    ```

3.  **Set your default shell and restart:**

    ```bash
    # For fish
    chsh -s /usr/bin/fish

    # For zsh
    chsh -s /usr/bin/zsh
    ```
    Now, restart your terminal.

## Switch Theme

Your theme configuration is in `~/.config/fish/config.fish` (for fish) or `~/.zshrc` (for zsh). Find themes in `~/.poshthemes`.

**Example for fish:**

Edit `~/.config/fish/config.fish` and change the theme name:

```fish
oh-my-posh init fish --config '$HOME/.poshthemes/your-theme.omp.json' | source
```

