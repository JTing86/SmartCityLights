#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#define PIN 6 //PIN connected on arduino
#define num_leds 23

int len = 6;
//int input_bytes[6] = {};
String input;


Adafruit_NeoPixel strip = Adafruit_NeoPixel(60, PIN, NEO_GRB + NEO_KHZ800);
uint32_t low = strip.Color(30, 18, 0); 

void setup() {
  Serial.begin(9600); 
  // dim
  for( int i = 0; i<len; i++){
      strip.setPixelColor(i, low);
      strip.show();
  }  
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
        strip.setPixelColor(i, 255, 120, 0);
        strip.show();
      }
      else if (input_bytes[i] == '0'){
        strip.setPixelColor(i, 30, 18, 0);
        strip.show();
      }  
      else{
        strip.setPixelColor(i, 30, 18, 0);
        strip.show();
      }
     }
}
