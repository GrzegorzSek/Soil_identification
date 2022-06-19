#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>

#define DHTPIN 4

#define DHTTYPE    DHT11     // DHT 11

DHT_Unified dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600); // open serial port, set the baud rate as 9600 bps
//  Serial.println((String)"sen_1  sen_2  sen_3  sen_4  air_temp  air_hum");
  dht.begin(); // dht sensor initialize
}
void loop() {
  sensors_event_t event;
  dht.temperature().getEvent(&event);
  float temp = event.temperature;
  dht.humidity().getEvent(&event);
  float air_humidity = event.relative_humidity;
  
  int sensor_1;
  int sensor_2;
  int sensor_3;
  int sensor_4;
  sensor_1 = analogRead(0); //connect sensor to Analog 0
  sensor_2 = analogRead(1); //connect sensor to Analog 1
  sensor_3 = analogRead(2); //connect sensor to Analog 1
  sensor_4 = analogRead(3); //connect sensor to Analog 1
//  Serial.println((String)"sns_1: "+val+" sns_2: "+val2);
//  Serial.println((String)"sns_1: "+val);
  Serial.println((String)sensor_1+"; "+sensor_2+"; "+sensor_3+"; "+sensor_4+"; "+temp+"; "+air_humidity);
  delay(3600000);
//  delay(3600);
}
