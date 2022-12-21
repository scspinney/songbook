# songbook


## Installation instructions for mac

  - Install Homebrew: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  - brew install pyenv
  - pyenv install 3.10.9
  
  
 
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew install pyenv

pyenv install 3.10.9
pyenv versions
python --version

pyenv global 3.10.2
pyenv global 3.10.9

brew install pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
source ~/.bash_profile

pyenv virtualenv <python-version> <name>
pyenv activate <name>
pyenv install 3.10.9

# Add pyenv-virtualenv initializer to shell startup script
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"


brew install pyenv-virtualenv
source ~/.bash_profile

brew install portaudio
pip install pyaudio

brew link portaudio
brew --prefix portaudio


sudo nano $HOME/.pydistutils.cfg
[build_ext]
include_dirs=<PATH FROM STEP 3>/inclu
