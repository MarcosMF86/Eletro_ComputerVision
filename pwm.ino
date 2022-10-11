#include <RBDdimmer.h>
//Parameters
const int zeroCrossPin  = 2;
const int acdPin  = 3;
String dado_byte;
//Variables
int power  = 0;
int num;
//Objects
dimmerLamp acd(acdPin);
void setup()
{
Serial.begin(9600);
//pinMode(redPin, OUTPUT);
acd.begin(NORMAL_MODE, ON);
}
void loop()
{
if (Serial.available() > 0){
//int red = Serial.parseInt();
  
  //armazena dado recebido
  dado_byte = Serial.readStringUntil( '\n');
  //converte para um valor do tipo inteiro
  num = dado_byte.toInt();
   //power = constrain(num, 0, 255);
   power = map(num, 0, 100, 0, 90);
   //analogWrite(redPin, red);
   acd.setPower(power);//nível brilho lampada
   //Serial.print(red);
   }
   //delay(10);
}
