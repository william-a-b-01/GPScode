
#include <SoftwareSerial.h>

SoftwareSerial mySerial(4, -1); // RX, TX

void setup()
{
  // Open serial communications
  Serial.begin(9600);
  Serial.println("Neo6M GPS module test code\n");
  
  // set the data rate for the SoftwareSerial port
  mySerial.begin(9600);
}

void loop()
{
  if (mySerial.available())
  {
     Serial.print(char(mySerial.read()));
  }
}
