## Install zsh in your linux
*Install zsh in ubuntu, debian, parrot, kali linux*
```bash
sudo apt install zsh -y
```
*Install zsh in arch or arch based distro*
```bash
sudo pacman -S zsh
```
#### If you want zsh to be default you can use `sudo chsh -s /bin/zsh` but if you want to use fish with it ignore this step
_Install fish by_
```bash
sudo apt install fish -y
```
_or_
```bash
sudo pacman -S fish
```


## How to install oh-my-posh shell in your linux ?
```bash
curl -s https://ohmyposh.dev/install.sh | bash -s
```

## After installing oh-my-posh
```bash
git clone https://github.com/Alomgir-Bhuiyan/tiwahu-config &&
cd tiwahu-config &&
chmod +x setup.sh &&
./setup.sh
```
it will defaultly install **tiwahu** theme
if you want to install something else, you can find
the theme list in `~/.poshthemes/` 

_if you want to use other theme than tiwahu, edit ~/.config/fish/config.fish_
```bash
oh-my-posh init fish --config $HOME/.poshthemes/tiwahu.omp.json | source
if status is-interactive
    # Commands to run in interactive sessions can go here
end
```
edit _~/.../tiwahu.omp.json_ with your desire file name

**after that change the to fish**
```bash
sudo chsh -s /bin/fish
```

