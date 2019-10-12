# Serial-communication-in-python
### Serial communication tx-rx of raspberry pi in python.
A simple python example program  to show serial communication on raspberry pi

## Requirement

* Two Raspberry pi 
* Knowledge to run python program :blush: 
* One jumperwire connecting the UART port 




### To search for available serial ports use the command

```
dmesg | grep tty
```

you will get to know the avalable ports, since we will be using ttyAMA0
and not USB go  to configuration and change the ports by 

```
sudo raspi-config
```
these steps should be done for both the raspberry pi 

## starting up 

* [write.py](https://github.com/santoshkrishnanr/serial-communication-in-python/blob/master/write.py) - Use this Program in Transmitter
* [read.py](https://github.com/santoshkrishnanr/serial-communication-in-python/blob/master/read.py) - Use this in Receiver



## Wire connection 

* GPIO 14 is called the tx pin and is used from the raspberryPi 1 so called as transmitter 
* GPIO 15 is called the rx pin is used from the raspberry Pi 2 so called Receiver 
![](https://github.com/santoshkrishnanr/serial-communication-in-python/blob/master/transreceiver.jpeg)


### data transfer

A simple date and time is generated in [write.py](https://github.com/santoshkrishnanr/serial-communication-in-python/blob/master/write.py) and seconds is transmitted using

```
ser.write(.....)
```

in the receiver side,  the transmitted data is received using 
```
ser.readline()
```
just to compare the time taken to transffer:wink:  the received data was compared with the actual time 


-

-to DO
* there are some limitation as data to be transfered
* things to be taken care port, baudrate,bitsize,stop bit etc

happy coading !! 
