# Analysis of allocation of antenna coverage

![Release Multi Platform](https://github.com/samuelterra22/Analysis-of-antenna-coverage/workflows/Release%20Multi%20Platform/badge.svg)

### Dependencies for development

###### Linux dependencies
```shell script
sudo apt update
sudo apt install -y \
                 software-properties-common \
                 libpcre3 libpcre3-dev \
                 libpython3-all-dev \
                 python3-distutils \
                 build-essential \
                 libpython3-dev \
                 python3-pip \
                 python3-pyqt5.qtwebengine \
                 g++ 
```

### Create environment and install python dependencies

```shell script
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
``` 

Fist preview of software:

![](screenshots/main_screen.png)

fbs freeze
fbs installer
sudo dpkg -i target/analysis-of-antenna-coverage.deb
sudo dpkg --purge analysis-of-antenna-coverage