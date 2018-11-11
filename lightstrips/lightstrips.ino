#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#define PIN 6 //PIN connected on arduino
#define num_leds 23

int len = 5;
//int input_leds[5]={1,1,0,0,1};   // for incoming serial data
//int input_bytes[5] = {};
String input;
Adafruit_NeoPixel strip = Adafruit_NeoPixel(60, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  Serial.begin(9600); 
  strip.begin();
  strip.show(); 
}


void loop() {

  while (Serial.available() != 0) {

    input = Serial.readString();

    turn_on_led_chain(input);
  } 
}

void turn_on_led(int n){
  //fill_solid( leds, 60, CRGB(50,0,200));
  strip.setPixelColor(n, 0, 200, 200);
  strip.show();
  //delay(3000); 
  //strip.setPixelColor(n, 0, 0, 0);
  //strip.show();
}

void turn_on_led_chain(String input_bytes){
    for (int i=0; i<len; i++){
     
      if (input_bytes[i] == '1'){
        strip.setPixelColor(i, 0, 200, 200);
        strip.show();
      }
      else if (input_bytes[i] == '0'){
        strip.setPixelColor(i, 0, 0, 0);
        strip.show();
      }  
      else{
        strip.setPixelColor(i, 200, 0, 0);
        strip.show();
      }
     }
}

void follow_up_led_chain_action(int rate){
  
}
