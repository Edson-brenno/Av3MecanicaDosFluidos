#include <SoftwareSerial.h>

// Constantes
const int bombaSubirSubmarinoPin = 8;

SoftwareSerial Bluetooth(11, 10); // RX, TX

int contador = 0;
bool subirSubmarino = false;
bool descerSubmarino = false;
bool pararSubmarino = false;

void tipoComando(char comando){
  if (comando == '1'){
    subirSubmarino = true;
  }
  else if (comando == '2'){
    descerSubmarino = true;
  }
  else{
    pararSubmarino = true;
  }
}

void analiseSubirSubmarino(){
  if (subirSubmarino == true){
    Serial.println("Subindo submarino");
    digitalWrite(bombaSubirSubmarinoPin, HIGH);
  }
  else{
    digitalWrite(bombaSubirSubmarinoPin, LOW);
  }
}

void analisePararSubmarino(){
  if (pararSubmarino == true){
    Serial.println("parando submarino");
    subirSubmarino = false;
    pararSubmarino = false;
  }
}


void setup() {
  Serial.begin(9600);             // Inicia comunicação com o PC
  while (!Serial) {
    ; // Aguarda a conexão com o Monitor Serial
  }

  Serial.println("Monitor Serial conectado!");
  Serial.println("Inicializando Bluetooth...");

  Bluetooth.begin(9600);          // Inicia comunicação com o HC-06
  Bluetooth.println("Conexão Bluetooth estabelecida.");
  Serial.println("Bluetooth inicializado com sucesso!");

  // Configurando bombas
  pinMode(8,OUTPUT);
}

void loop() {
  digitalWrite(8, HIGH);
  analisePararSubmarino();

  analiseSubirSubmarino();

  if (contador > 18){
      contador = 0;
  }

  if (Bluetooth.available()) {
    char c = Bluetooth.read();
    if (c == '+'){
      contador += 1;
    }
    else if (contador > 0 && contador < 19){
      contador += 1;
    }
    else{
      // Serial.print("Recebido via Bluetooth: ");
      // Serial.println(c);
      tipoComando(c);
    }
    
  }

  if (Serial.available()) {
    char c = Serial.read();
    Bluetooth.write(c);
    Serial.print("Enviado ao Bluetooth: ");
    Serial.println(c);
  }
}
