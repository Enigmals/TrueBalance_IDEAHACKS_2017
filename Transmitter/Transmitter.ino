#include <SPI.h>
#include <WiFi101.h>
#include "Private.h"

int status = WL_IDLE_STATUS;     // the Wifi radio's status

WiFiClient client;

void setup() {
  // put your setup code here, to run once:

  Serial.begin(115200);

  while ( status != WL_CONNECTED) {
    Serial.print("Attempting to connect to WPA SSID: ");
    Serial.println(ssid);
    // Connect to WPA/WPA2 network:
    status = WiFi.begin(ssid, pass);

    // wait 10 seconds for connection:
    delay(10000);
  }

  Serial.print("You're connected to the network");
}

void loop() {
  // put your main code here, to run repeatedly:
  
}
