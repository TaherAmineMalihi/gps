import serial
import pynmea2

# configure the serial port
ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)

while True:
    # read a line of NMEA data from the GPS module
    line = ser.readline().decode('ascii', errors='replace')
    
    # check if the line is a valid GPS sentence
    if line.startswith('$GPGGA'):
        # parse the GPS sentence using the pynmea2 library
        try:
            data = pynmea2.parse(line)
        except pynmea2.ParseError:
            continue
        
        # extract the latitude and longitude from the data
        latitude = data.latitude
        longitude = data.longitude

        # print the location data
        print('Latitude: {0:.6f}, Longitude: {1:.6f}'.format(latitude, longitude))
 