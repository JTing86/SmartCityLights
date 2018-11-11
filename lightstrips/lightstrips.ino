#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#define PIN 6 //PIN connected on arduino
#define num_leds 23

int input_leds[5]={};   // for incoming serial data
int input_bytes[60] = {};
//int LED_array[5];
//int input_leds[5];

Adafruit_NeoPixel strip = Adafruit_NeoPixel(60, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  Serial.begin(9600); 
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
}


void loop() {

  while (Serial.available() != 0) {
    for (int i=0;i<60;i++){
      input_bytes[60] = Serial.parseInt();
    }
    turn_on_led_chain(input_bytes);
  }     
}

void turn_on_led(int n){
  //fill_solid( leds, 60, CRGB(50,0,200));
  strip.show();
  delay(3000); 
  strip.setPixelColor(n, 0, 0, 0);
  strip.show();
}

void turn_on_led_chain(int LED_array[]){
    for (int i=0; i<60; i++){
     
      if (LED_array[i] == 1){
        strip.setPixelColor(i, 0, 200, 200);
        strip.show();
      }
      else if (LED_array[i] == 0){
        strip.setPixelColor(i, 0, 0, 0);
        strip.show();
      }  
     }
}

void follow_up_led_chain_action(int rate){
  
}
