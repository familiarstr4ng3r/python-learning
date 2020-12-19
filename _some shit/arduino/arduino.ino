//hello world
/*
    multi
    line

    https://www.youtube.com/watch?v=CRRlbzzt3VA

    https://alexgyver.ru/lessons/syntax/
    https://alexgyver.ru/lessons/variables-types/
    https://alexgyver.ru/lessons/
    https://alexgyver.ru/arduino_lessons/
    https://alexgyver.ru/arduino-first/
*/

#include <Servo.h>

boolean bool_1 = 1;     // 1 = true, 0 = false
boolean bool_2 = true;  // 1 byte

char char_1 = 'a';  // [-128..127] = 1 byte
byte byte_1 = 0;    // [0..255] = 1 byte


int int_1 = 10;             // [-32k..32k] = 2 bytes
unsigned int int_2 = 10;    // [0..65k] = 2 bytes
word w = 1;                 // same as 'unsigned int'

long billion = 2147483647;          // 4 bytes
unsigned long billion = 4294967295; // 4 bytes

float f = 10.3;     // 4 bytes
double d = 10.4;    // equal to 'float'

void setup()
{
    
}

void loop()
{
    
}