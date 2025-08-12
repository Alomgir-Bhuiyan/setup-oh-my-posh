# Tiwahu-Config: Zsh and Fish Shell Configuration with Oh-My-Posh

This repository provides a configuration setup for `zsh` and `fish` shells, along with the `oh-my-posh` theme engine for a customized and informative prompt.

## Features

*   Easy installation and setup script.
*   Includes a collection of `oh-my-posh` themes.
*   Provides instructions for both `zsh` and `fish` shells.
*   Customizable prompt configuration.

## Prerequisites

Before you begin, ensure you have the following installed:

*   `zsh` or `fish` shell
*   `git`
*   `curl`

## Installation

1.  **Install `zsh` or `fish`:**

    *   **For Debian/Ubuntu based distributions:**
        ```bash
        sudo apt update
        sudo apt install zsh fish -y
        ```

    *   **For Arch Linux based distributions:**
        ```bash
        sudo pacman -Syu zsh fish
        ```

2.  **Install Oh-My-Posh:**

    ```bash
    curl -s https://ohmyposh.dev/install.sh | bash -s
    ```

3.  **Clone this repository and run the setup script:**

    ```bash
    git clone https://github.com/Alomgir-Bhuiyan/tiwahu-config && \
    cd tiwahu-config && \
    chmod +x setup.sh && \
    ./setup.sh
    ```

4.  **Restart your terminal.**

## Setting your default shell

After installation, you may need to set your preferred shell as the default.

*   **To set `fish` as the default shell:**
    ```bash
    chsh -s /usr/bin/fish
    ```

*   **To set `zsh` as the default shell:**
    ```bash
    chsh -s /usr/bin/zsh
    ```

## Customization

### Changing the Oh-My-Posh Theme

The default theme is `tiwahu.omp.json`. To change the theme, you need to edit your shell's configuration file.

*   **For `fish` shell, edit `~/.config/fish/config.fish`:**

    ```fish
    # oh-my-posh init fish --config '$HOME/.poshthemes/your-theme-name.omp.json' | source
    oh-my-posh init fish --config '$HOME/.poshthemes/tiwahu.omp.json' | source
    ```
    Replace `tiwahu.omp.json` with the name of the theme you want to use. You can find the list of available themes in the `~/.poshthemes/` directory.

*   **For `zsh` shell, edit `~/.zshrc`:**

    ```zsh
    # eval "$(oh-my-posh init zsh --config ~/.poshthemes/your-theme-name.omp.json)"
    eval "$(oh-my-posh init zsh --config ~/.poshthemes/tiwahu.omp.json)"
    ```
    Replace `tiwahu.omp.json` with the name of the theme you want to use.

### Themes

This repository includes a variety of themes located in the `.poshthemes` directory. You can browse the files in that directory to see the available options.

## The `setup.sh` script

The `setup.sh` script performs the following actions:

*   Creates symbolic links for the `.zshrc` and `.config/fish/config.fish` files from the repository to your home directory.
*   Copies the `.poshthemes` directory to your home directory.

## Troubleshooting

If you don't see any changes after restarting your terminal, try the following:

1.  Ensure that you have set your default shell correctly.
2.  Verify that the `oh-my-posh` command is available in your `PATH`. You can check this by running `which oh-my-posh`.
3.  Make sure that the configuration files (`~/.zshrc` or `~/.config/fish/config.fish`) are being loaded correctly by your shell.

If you continue to experience issues, please open an issue on the GitHub repository.