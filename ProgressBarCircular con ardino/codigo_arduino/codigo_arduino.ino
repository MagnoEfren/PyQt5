// https://www.youtube.com/c/MagnoEfren
// Señal analógica en PorgressBar Circular en  PySide2 / PyQt5

float lectura;
float voltaje;

void setup() {
  
  Serial.begin(9600);
  pinMode(A0,INPUT);
}

void loop() {
  lectura = analogRead(A0);
  voltaje = ((lectura/1023)*5.5);

  Serial.println(voltaje);

  delay(200);
}
