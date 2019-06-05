#include "FastLED.h"

#define NUM_LEDS 8

// Data pin that led data will be written out over
#define DATA_PIN 3

CRGB leds[NUM_LEDS];

union raw_data {
    float f;
    char bytes[4];
} serial_data;


void setup()
{
	FastLED.addLeds<WS2812B, DATA_PIN, GRB>(leds, NUM_LEDS); // NeoPixel configuration
	Serial.begin(115200); // baud rate
	while (!Serial) {
		; // wait for serial port to connect. Needed for native USB
	}
}

void loop()
{
    delay(30);
	if (Serial.available() > 0) // Waiting for request
	{
        for (int i = 0; i < 4; i++) {
            serial_data.bytes[i] = Serial.read();
        }
        float current_RPM = serial_data.f;
        for (int i = 0; i < 4; i++) {
            serial_data.bytes[i] = Serial.read();
        }
        float max_RPM = serial_data.f;
        leds[0] = CRGB(0,0,0);
	}
}