source .venv/bin/activate

read -p 'Choose what library to install to the virtual enviroment: ' library

pip install --upgrade pip

pip install $library