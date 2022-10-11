String dado_byte;
//Pinos onde as lâmpadas serão conectadas  
int L_1=4,L_2=5,L_3=6,L_4=7,L_5=8;
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

void loop( )  
{
if(Serial.available( ) > 0) 
 {  
  //armazena dado recebido
  dado_byte = Serial.readStringUntil( '\n');
  //converte para um valor do tipo inteiro
  num = dado_byte.toInt();
  switch (num){
    case 1:
    //Aciona 1 Lamp
    digitalWrite(L_1,LIGA);
    digitalWrite(L_2,DESL);
    digitalWrite(L_3,DESL);
    digitalWrite(L_4,DESL);
    digitalWrite(L_5,DESL);
    break;
    case 2:
    //Aciona 2 Lamps
    digitalWrite(L_1,LIGA);
    digitalWrite(L_2,LIGA);
    digitalWrite(L_3,DESL);
    digitalWrite(L_4,DESL);
    digitalWrite(L_5,DESL);
    break;
    case 3:
    //Aciona 3 Lamps
    digitalWrite(L_1,LIGA);
    digitalWrite(L_2,LIGA);
    digitalWrite(L_3,LIGA);
    digitalWrite(L_4,DESL);
    digitalWrite(L_5,DESL);
    break;
    case 4:
    //Aciona 4 Lamps
    digitalWrite(L_1,LIGA);
    digitalWrite(L_2,LIGA);
    digitalWrite(L_3,LIGA);
    digitalWrite(L_4,LIGA);
    digitalWrite(L_5,DESL);
    break;
    case 5:
    //Aciona 5 Lamps
    digitalWrite(L_1,LIGA);
    digitalWrite(L_2,LIGA);
    digitalWrite(L_3,LIGA);
    digitalWrite(L_4,LIGA);
    digitalWrite(L_5,LIGA);
    break;
    default:
    digitalWrite(L_1,DESL);
    digitalWrite(L_2,DESL);
    digitalWrite(L_3,DESL);
    digitalWrite(L_4,DESL);
    digitalWrite(L_5,DESL);
    break;
  }
 }
}
