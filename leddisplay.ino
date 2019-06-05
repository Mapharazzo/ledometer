#include "FastLED.h"

#define NUM_LEDS 8

// Data pin that led data will be written out over
#define DATA_PIN 3

// number of leds for each zone
#define LEDS_LOW 2
#define LEDS_MED 3
#define LEDS_HIGH 3

// color of each zone
#define COLOR_LOW (CRGB(0, 255, 0))
#define COLOR_MED (CRGB(0, 0, 0))
#define COLOR_HIGH (CRGB(0, 0, 0))
#define COLOR_BLACK (CRGB(0, 0, 0))

#define TRESHOLD_LOW 0.65
#define TRESHOLD_MED 0.8
#define THRESHOLD_HIGH 0.93

CRGB leds[NUM_LEDS];

union raw_data {
    float f;
    char bytes[4];
} serial_data;


float read_serial_float()
{
    for (int i = 0; i < 4; i++) {
            serial_data.bytes[i] = Serial.read();
        }
    return serial_data.f;
}

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
        float current_RPM = read_serial_float();
        float max_RPM = read_serial_float();

        float percent_RPM = current_RPM / max_RPM;        
        float zone_part = THRESHOLD_LOW / LEDS_LOW;

        for (int i = 0; i < LEDS_LOW; i++) {
            if (percent_RPM > zone_part * i) {
                leds[i] = COLOR_LOW;
            } else {
                leds[i] = COLOR_BLACK;
            }
        }

        zone_part = (THRESHOLD_MED - TRESHOLD_LOW) / LEDS_MED;
        for (int i = 0; i < LEDS_MED; i++) {
            if (percent_RPM > TRESHOLD_LOW + zone_part * i) {
                leds[i + LEDS_LOW] = COLOR_MED;
            } else {
                leds[i + LEDS_LOW] = COLOR_BLACK;
            }
        }

        zone_part = (THRESHOLD_HIGH - TRESHOLD_MED) / LEDS_HIGH;
        for (int i = 0; i < LEDS_HIGH; i++) {
            if (percent_RPM > TRESHOLD_MED + zone_part * i) {
                leds[i + LEDS_LOW + LEDS_MED] = COLOR_HIGH;
            } else {
                leds[i + LEDS_LOW + LEDS_MED] = COLOR_BLACK;
            }
        }
	}
}
