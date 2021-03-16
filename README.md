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

###### pcre dependency
```shell script
wget https://ftp.pcre.org/pub/pcre/pcre-8.43.tar.bz2
tar -xvf pcre-8.43.tar.bz2
cd pcre-8.43/
./configure --prefix=/usr                     \
            --docdir=/usr/share/doc/pcre-8.43 \
            --enable-unicode-properties       \
            --enable-pcre16                   \
            --enable-pcre32                   \
            --enable-pcregrep-libz            \
            --enable-pcregrep-libbz2          \
            --enable-pcretest-libreadline     \
            --disable-static
make
make install
mv -v /usr/lib/libpcre.so.* /lib
ln -sfv ../../lib/$(readlink /usr/lib/libpcre.so) /usr/lib/libpcre.so
```

###### swig dependency
```shell script
# Download and extract files
wget https://ufpr.dl.sourceforge.net/project/swig/swig/swig-4.0.1/swig-4.0.1.tar.gz
chmod 777 swig-4.0.1.tar.gz
tar -xvf swig-4.0.1.tar.gz

# Configure lib folder and install
cd swig-4.0.1
./configure --prefix=/home/$USER/library/swigtool
make
make install

# Configure swig path
sudo nano /etc/profile
export SWIG_PATH=/home/$USER/library/swigtool/bin
export PATH=$SWIG_PATH:$PATH

# Load changes
source /etc/profile

# Check swig version
swig -version

# To check the build, run the tests:
make check-python-examples
```

### [dev] How to compile c code to python library using swing

```shell script
# 'Compile' interface file
swig -python example.i

# Complile code
gcc -c -fPIC example.c example_wrap.c -I/usr/include/python3.6/

# Link files to create .py
ld -shared example.o example_wrap.o -o _example.so
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
