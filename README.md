# floortemp
Measure floor in- and out temperature using a Raspberry Pi and Plot.ly

**Note 2020**: This project is discontinued and replaced with a Node-RED node: https://github.com/MelvinRook/node-red-contrib-pi-max31865 - as Plot.ly limited the streaming functionality.

It's my first Node-RED node. If you have any feedback, please let me know or register a GitHub issue. :-)

# Install
- Copy `floorTemp.py` into `/home/pi/`
- Copy `floorTemp.service` into `/lib/systemd/system/`
- Run commands: ```sudo chmod 644 /lib/systemd/system/floorTemp.service 
sudo systemctl daemon-reload
sudo systemctl enable floorTemp.service```
