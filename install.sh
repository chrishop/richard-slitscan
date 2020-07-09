/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
brew install python3
brew install git
git install https://github.com/chrishop/richard-slitscan.git
cd richard-slitscan
chmod +x slitscan-gui.py
./slitscan-gui.py