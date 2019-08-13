# floortemp
Measure floor in- and out temperature using a Raspberry Pi and Plot.ly

# Install
- Copy `floorTemp.py` into `/home/pi/`
- Copy `floorTemp.service` into `/lib/systemd/system/`
- Run commands: ```sudo chmod 644 /lib/systemd/system/floorTemp.service 
sudo systemctl daemon-reload
sudo systemctl enable floorTemp.service```
