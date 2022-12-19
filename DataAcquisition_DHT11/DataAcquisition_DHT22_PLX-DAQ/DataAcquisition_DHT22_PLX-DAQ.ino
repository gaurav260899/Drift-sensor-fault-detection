// Data Collection Code from Sensor - Excel CSV datalogger using ESP8266 and DHT22 sensor
#include <DHT.h>              // Include DHT library code
#define DHTPIN  2             // DHT22 data pin is connected 
#define DHTTYPE DHT11         // DHT22 sensor is used
DHT dht(DHTPIN, DHTTYPE);     // Initialize DHT library
 
void setup() {
  Serial.begin(9600);         // Initialize serial communications with the PC
  dht.begin();                // Initialize the DHT library
}

void loop() {
  
    float b = 0.08; //Change this value according to drift fault
    float y = 0;
    
    for (float count=0; count<100; count++) {
      float t = dht.readTemperature();
      if (count<=50) {
        y = t;
        }
      else {
        y = t + b;
        b = b + 0.08; //Change this value according to drift fault
        }
        delay(100); //100ms 
        Serial.print(count);    
        Serial.print("DATA,");
        Serial.println(y);        
      }
}
