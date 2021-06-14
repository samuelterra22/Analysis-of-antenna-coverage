# Analysis of allocation of antenna coverage

![Release Multi Platform](https://github.com/samuelterra22/Analysis-of-antenna-coverage/workflows/Release%20Multi%20Platform/badge.svg)

### Preview of software:

![](screenshots/main_screen.png)

### Setup for development

-  Linux dependencies
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

- Create environment and install python dependencies

```shell script
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
``` 

- USING IN IDE

The command fbs run is great to quickly run your app. Many people however prefer working in an IDE such as PyCharm. It especially simplifies debugging.

To run a fbs app from other environments (such as an IDE, or the command line), you simply

- need the virtual environment to be active,
- have src/main/python on your PYTHONPATH and
- run src/main/python/main.py.

So for example on Mac and Linux, you can also run your app from the command line via

PYTHONPATH=src/main/python python src/main/python/main.py
(assuming the virtual environment is active).

Here are screenshots of how PyCharm can be configured for this:

![](images/pycharm-config-1.png)

![](images/pycharm-config-2.png)

![](images/pycharm-config-3.png)

See more in: [https://build-system.fman.io/manual/](https://build-system.fman.io/manual/)


### For deploy

```shell
fbs freeze
fbs installer
sudo dpkg -i target/analysis-of-antenna-coverage.deb
sudo dpkg --purge analysis-of-antenna-coverage
```

