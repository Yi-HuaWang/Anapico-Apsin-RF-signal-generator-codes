4. 4. 2014 AnaPico AG

These Python examples show how to communicate with AnaPico devices.
Python provides many ways to communicate with AnaPico devices. The examples cover telnet, VXI-11 and VISA.

Telnet:
telnet_example.py uses the telnet capability of AnaPico devices. There is no need to install any additional libraries since Python comes with telnet support. Supports network only. Tested on Python 2.7 and 3.4.

VXI-11:
vxi11_example.py uses the VXI-11 communication standard. It requires the Python VXI-11 libraries. VXI-11 is a standard provided by many T&M devices. Supports network only.
Please refer to
https://pypi.python.org/pypi/python-vxi11
http://www.alexforencich.com/wiki/en/python-vxi11/start
for downloads and additional information.
The example is based on version 0.5 of the Python VXI-11 library. Tested on Python 2.7 and 3.4.

PyVISA:
pyvisa_example.py uses VISA and the PyVISA library. It requires a VISA installation and the Python PyVISA libraries. VISA supports most T&M devices and different interfaces such as network, USB and GPIB.
Please refer to
http://pyvisa.readthedocs.org/
for downloads and additional information.
The example is based on version 1.4 of the PyVISA library. Tested on Python 2.7 only.