#!/usr/bin/env python3

import board
import busio
import digitalio
import adafruit_max31865
import datetime
import time
import numpy as np
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go

# Setup plotly credentials
in_stream_token = ''
out_stream_token = ''

#tls.set_credentials_file(username=username, api_key=api_key) # ensure the ~/.plotly/.credentials file is set, otherwise use this line to init

# Setup chart
trace1 = go.Scatter(
    x=[],
    y=[],
    stream=dict(
        token=in_stream_token,
        maxpoints=10000
    ),
    mode = 'lines',
    name = 'in'
)

trace2 = go.Scatter(
    x=[],
    y=[],
    stream=dict(
        token=out_stream_token,
        maxpoints=10000
    ),
    mode = 'lines',
    name = 'out'
)

data = go.Data([trace1,trace2])

layout = go.Layout(
    title='Floor Temperature'
)

fig = go.Figure(data=data, layout=layout)

py.plot(data, filename='Floor Temperature', fileopt='extend')

# Init SPI bus and sensor
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs1 = digitalio.DigitalInOut(board.D5)  # Chip select of MAX31865 board 1 (upper)
cs2 = digitalio.DigitalInOut(board.D6)  # Chip select of MAX31865 board 2 (lower)
sensor1 = adafruit_max31865.MAX31865(spi, cs1, wires=3, rtd_nominal=1000.0, ref_resistor=4300.0)
sensor2 = adafruit_max31865.MAX31865(spi, cs2, wires=3, rtd_nominal=1000.0, ref_resistor=4300.0)

# Open streams
in_stream = py.Stream(in_stream_token)
in_stream.open()

out_stream = py.Stream(out_stream_token)
out_stream.open()

while True:

    # Timestamp of measurement
    now = datetime.datetime.now()

    # Sensor readout
    temp_in = sensor1.temperature
    temp_out = sensor2.temperature

    # Values should be within acceptable bounds
    if temp_in > 0 and temp_in < 70 and temp_out > 0 and temp_in < 70:
        temp_in = '{0:0.3f}'.format(temp_in)
        temp_out = '{0:0.3f}'.format(temp_out)

        in_stream.write(dict(x=now,y=temp_in))
        out_stream.write(dict(x=now,y=temp_out))

    time.sleep(30.0)

in_stream.close()
out_stream.close()
