from wifi import Cell, Scheme

if __name__ == '__main__':

    # need `sudo` to show all networks
    for cell in Cell.all('wlan0'):
      print(cell)