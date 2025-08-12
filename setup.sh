#!/bin/bash

rm -rf $HOME/.config/fish
cp -r ./.config/fish $HOME/.config/
rm -rf $HOME/.poshthemes
cp -r ./.poshthemes $HOME/
chmod u+rw $HOME/.poshthemes/*.omp.*
cp -r ./.zshrc $HOME/

DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR/.."
rm -rf "$DIR"
