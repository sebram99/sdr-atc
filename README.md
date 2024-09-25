# sdr-atc


## Install pluto drivers and libraries

This side shows how to compile necessary files from source.
The following snipe
[pysdr guide](https://pysdr.org/content/pluto.html)

```
sudo apt-get update
sudo apt-get install build-essential git libxml2-dev bison flex libcdk5-dev cmake python3-pip libusb-1.0-0-dev libavahi-client-dev libavahi-common-dev libaio-dev
cd ~
git clone --branch v0.23 https://github.com/analogdevicesinc/libiio.git
cd libiio
mkdir build
cd build
cmake -DPYTHON_BINDINGS=ON ..
make -j$(nproc)
sudo make install
sudo ldconfig

cd ~
git clone https://github.com/analogdevicesinc/libad9361-iio.git
cd libad9361-iio
mkdir build
cd build
cmake ..
make -j$(nproc)
sudo make install

cd ~
git clone --branch v0.0.14 https://github.com/analogdevicesinc/pyadi-iio.git
cd pyadi-iio
pip3 install --upgrade pip
pip3 install -r requirements.txt
sudo python3 setup.py install
```


## Create a python enviroment

### VScode Python enviroment

- If you have python already installed, hold down **CTRL + SHIFT + P**, type create virtual enviroment and press **ENTER**.

- Activate environment `source .venv/bin/activate`

- Activate environment and then in the terminal ```pip install -r requirements.txt``` to install all the required python modules.