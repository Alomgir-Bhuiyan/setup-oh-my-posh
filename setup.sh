rm -rf $HOME/.config/fish
cp -r ./.config/fish $HOME/.config/
rm -rf $HOME/.poshthemes
cp -r ./.poshthemes $HOME/
chmod u+rw $HOME/.poshthemes/*.omp.*
cp -r ./.zshrc $HOME/
cd ..
#rm -rf tiwahu-config
