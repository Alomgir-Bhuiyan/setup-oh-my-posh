rm -rf $HOME/.config/fish
mv ./.config/fish $HOME/.config/
mv ./.poshthemes $HOME/
chmod u+rw $HOME/.poshthemes/*.omp.*
mv ./.zshrc $HOME/
cd ..
rm -rf tiwahu-config
