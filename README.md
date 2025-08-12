# Tiwahu-Config: A Professional Shell Environment

![Shell: zsh](https://img.shields.io/badge/shell-zsh-blue)
![Shell: fish](https://img.shields.io/badge/shell-fish-blue)
![Theme Engine: Oh-My-Posh](https://img.shields.io/badge/theme%20engine-Oh--My--Posh-orange)

---

A streamlined and visually appealing shell configuration for `zsh` and `fish`, powered by the `oh-my-posh` theme engine. This setup is designed for developers who value a clean, informative, and efficient command-line experience.

## Table of Contents

*   [Prerequisites](#prerequisites)
*   [Installation](#installation)
*   [Configuration](#configuration)
    *   [Setting the Default Shell](#setting-the-default-shell)
    *   [Customizing the Theme](#customizing-the-theme)
*   [Included Themes](#included-themes)
*   [The `setup.sh` Script](#the-setupsh-script)
*   [Contributing](#contributing)

## Prerequisites

Before proceeding, ensure that your system has the following dependencies installed:

*   `git`: For cloning the repository.
*   `curl`: For downloading `oh-my-posh`.
*   `zsh` or `fish`: The shell environment you intend to use.

## Installation

Follow these steps to install and configure your new shell environment:

1.  **Install Shells:**

    *   **Debian/Ubuntu-based systems:**
        ```bash
        sudo apt-get update && sudo apt-get install -y zsh fish
        ```
    *   **Arch Linux-based systems:**
        ```bash
        sudo pacman -Syu --noconfirm zsh fish
        ```

2.  **Install Oh-My-Posh:**

    ```bash
    curl -s https://ohmyposh.dev/install.sh | bash -s
    ```

3.  **Clone and Set Up:**

    ```bash
    git clone https://github.com/Alomgir-Bhuiyan/tiwahu-config.git && \
    cd tiwahu-config && \
    chmod +x setup.sh && \
    ./setup.sh
    ```

4.  **Restart your terminal** to apply the changes.

## Configuration

### Setting the Default Shell

To make `zsh` or `fish` your default shell, use the `chsh` command:

*   **For `fish`:**
    ```bash
    chsh -s $(which fish)
    ```
*   **For `zsh`:**
    ```bash
    chsh -s $(which zsh)
    ```

### Customizing the Theme

The configuration files for `zsh` and `fish` are located at `~/.zshrc` and `~/.config/fish/config.fish`, respectively. To change the theme, you will need to edit the `oh-my-posh` initialization line.

**Example for `fish`:**

1.  Open `~/.config/fish/config.fish` in your preferred editor.
2.  Locate the following line:
    ```fish
    oh-my-posh init fish --config '$HOME/.poshthemes/tiwahu.omp.json' | source
    ```
3.  Change `tiwahu.omp.json` to the filename of your desired theme.

## Included Themes

A wide variety of themes are included in the `~/.poshthemes` directory. You can browse this directory to see the available options.

## The `setup.sh` Script

The `setup.sh` script automates the following tasks:

*   Creates symbolic links from the repository's configuration files (`.zshrc`, `config.fish`) to the appropriate locations in your home directory.
*   Copies the `.poshthemes` directory to your home directory, making the themes available to `oh-my-posh`.

## Contributing

Contributions are welcome! If you have suggestions for improvements, new themes, or bug fixes, please feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/Alomgir-Bhuiyan/tiwahu-config).