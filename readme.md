Hacker tools
========

My personnals test in networks hacks.

WiFi Bruteforce
-----------------------

A **Python** script to find all Wifi Networks in the area and try the 
[100K most used passwords](https://github.com/danielmiessler/SecLists) on them.

### DOWNLOAD/INSTALL

1º - Download framework from github
```
git clone https://github.com/madeindjs/Wifi_BruteForce.git
```

2° - Install Python & requirements
```
sudo apt-get install python
sudo curl https://bootstrap.pypa.io/get-pip.py -o /get-pip.py
sudo python /get-pip.py
sudo pip install scapy
sudo pip install wifi


```

3º - Set execution permitions
```
cd Wifi_BruteForce
sudo find ./ -name "*.sh" -exec chmod +x {} \;
sudo find ./ -name "*.py" -exec chmod +x {} \;
```

4º - Run main tool
```
sudo python __main__.py
```

### TODO:

* add a percentage
* send on pip
* more & more

## Author


[Rousseau Alexandre][madeindjs]

## License


GNU GENERAL PUBLIC LICENSE


[madeindjs]: https://github.com/madeindjs/
