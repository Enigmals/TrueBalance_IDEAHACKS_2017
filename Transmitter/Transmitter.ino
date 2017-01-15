#include <SPI.h>
#include <WiFi101.h>
#include "Private.h"

#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_LSM303_U.h>

int status = WL_IDLE_STATUS;     // the Wifi radio's status

IPAddress server(192,168,43,189);

WiFiClient client;
/* Assign a unique ID to this sensor at the same time */
Adafruit_LSM303_Accel_Unified accel = Adafruit_LSM303_Accel_Unified(54321);

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  accel.begin();

  // Configure accel to 16gs
  //byte accelSensitivityReg = accel.read8(LSM303_ADDRESS_ACCEL, LSM303_REGISTER_ACCEL_CTRL_REG4_A);
  //accelSensitivityReg = ((accelSensitivityReg & B11001001) | B00000000);
  //accel.write8(LSM303_ADDRESS_ACCEL, LSM303_REGISTER_ACCEL_CTRL_REG4_A, accelSensitivityReg);

  while ( status != WL_CONNECTED) {
    Serial.print("Attempting to connect to WPA SSID: ");
    Serial.println(ssid);
    // Connect to WPA/WPA2 network:
    status = WiFi.begin(ssid, pass);

    // wait 10 seconds for connection:
    delay(10000);
  }

  displaySensorDetails();

  while (!client.connect(server, 82))
  {
	  Serial.println("Client Failed to connect");
    delay(10);
  }
  Serial.print("You're connected to the network");
}

sensors_event_t event;

void loop() {
  accel.getEvent(&event);
  Serial.println("Transmitting.");
  
  sendUpdate(String(event.acceleration.x) + " " + 
             String(event.acceleration.y) + " " + 
             String(event.acceleration.z) + " " +
             String(millis()));

  delay(10);
}

void sendUpdate(String data)
{
  if (client.connected())
  {
    client.print(data + "\n");
  } else
  {
    Serial.println("Failed to connect. Attempting to reconnect.");
    client.connect(server, 80);
  }
}

void displaySensorDetails(void)
{
  sensor_t sensor;
  accel.getSensor(&sensor);
  Serial.println("------------------------------------");
  Serial.print  ("Sensor:       "); Serial.println(sensor.name);
  Serial.print  ("Driver Ver:   "); Serial.println(sensor.version);
  Serial.print  ("Unique ID:    "); Serial.println(sensor.sensor_id);
  Serial.print  ("Max Value:    "); Serial.print(sensor.max_value); Serial.println(" m/s^2");
  Serial.print  ("Min Value:    "); Serial.print(sensor.min_value); Serial.println(" m/s^2");
  Serial.print  ("Resolution:   "); Serial.print(sensor.resolution); Serial.println(" m/s^2");
  Serial.println("------------------------------------");
  Serial.println("");
  delay(500);
}

