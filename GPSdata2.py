from machine import Pin, UART
import time

data = UART(1, baudrate=9600,tx=Pin(8),rx=Pin(9)) #obtains raw data gathered from the NEO GPS module


def Convert_To_Deg(GPGGA_RAWLat,GPGGA_RAWLong):

    GPGGA_RAWLat = round((float(GPGGA_RAWLat)/100),5)
    GPGGA_RAWLong = round((float(GPGGA_RAWLong)/100),5) #Converts to float and rounds so that it follows format DD.MMMMM instead of standard NMEA format DDMM.MMM/DDDMM.MMM

    GPGGA_RAWLat = str(GPGGA_RAWLat) #Converts back to string for seperation DD from MMMMM
    GPGGA_RAWLong = str(GPGGA_RAWLong)

    GPGGA_RAWLong = GPGGA_RAWLong.split('.')
    GPGGA_RAWLat = GPGGA_RAWLat.split('.') #seperates DD from MMMMM (degrees from minutes for calculation)

    GPGGA_Long = ((float(GPGGA_RAWLong[0])) + ((float(GPGGA_RAWLong[1]))/1000)/60 )* -1

    GPGGA_Lat = ((float(GPGGA_RAWLat[0])) + (float(GPGGA_RAWLat[1])/1000)/60)

    print("Latitude: ",GPGGA_Lat,"\nLongitude: ",GPGGA_Long)

def main():
    
    if data.any():

        raw_data=data.readline().strip() #reads individual lines and strips white spaces as well

        if raw_data.startswith("$GPGGA"): #isolates lines that start with the $GPGGA identifier which includes information such as lat/long/time/etc.

            print(raw_data) #exclusively prints those lines and ignores the rest of the data

            GPGGA_DATA = str(raw_data) #declares GPGGA_DATA as raw_data
            GPGGA_PART = GPGGA_DATA.split(',') #Converts single string to list seperated by commas

            GPGGA_RAWLat = (GPGGA_PART[2])
            GPGGA_RAWLong = (GPGGA_PART[4])


            Convert_To_Deg(GPGGA_RAWLat,GPGGA_RAWLong)

    time.sleep(1)
    
def GPSDATA():
    while True:
        try:
            main()
        
        except Exception as e:
            print("Function errored out!", e)
            print("Retrying ... ")

    
