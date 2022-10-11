String dado_byte;
//Pinos onde as lâmpadas serão conectadas  
int L_1=4,L_2=5,L_3=6,L_4=7,L_5=8;
//valor de acionamento de cada lampada
int ac_L1 = 0, ac_L2 = 0, ac_L3 = 0, ac_L4 = 0, ac_L5 = 0;
int num;
int LIGA = LOW;
int DESL = HIGH;
void setup( )  
{
//Inicializa porta serial    
Serial.begin(9600);
//configura pinos como saídas  
pinMode(L_1,OUTPUT);
pinMode(L_2,OUTPUT);
pinMode(L_3,OUTPUT);
pinMode(L_4,OUTPUT);
pinMode(L_5,OUTPUT);
}

int separa_bit_0(int n)
{
  return n % 10;
}
int separa_bit_1(int n)
{
  return (n % 100)/10;
}
int separa_bit_2(int n)
{
  return (n % 1000)/100;
}
int separa_bit_3(int n)
{
  return (n % 10000)/1000;
}
int separa_bit_4(int n)
{
  return (n/10000);
}
void loop( )  
{
if(Serial.available( ) > 0) 
 {  
    //armazena dado recebido
    dado_byte = Serial.readStringUntil( '\n');
    //converte para um valor do tipo inteiro
    num = dado_byte.toInt();
    //encontra o bit de acionamento de cada lampada
    ac_L1 = separa_bit_0(num);
    ac_L2 = separa_bit_1(num);
    ac_L3 = separa_bit_2(num);
    ac_L4 = separa_bit_3(num);
    ac_L5 = separa_bit_4(num);
    //aciona lampadas
    digitalWrite(L_1,!ac_L1);
    digitalWrite(L_2,!ac_L2);
    digitalWrite(L_3,!ac_L3);
    digitalWrite(L_4,!ac_L4);
    digitalWrite(L_5,!ac_L5);
    delay(10);
 }
}  
