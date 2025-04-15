const int chargePin      = 9;    
const int voltageOutPin  = A0;  

const int bufferSize = 512;
short outputBuffer[bufferSize];

const unsigned long chargeTimeMillis  = 2000;  

const unsigned long sampleIntervalMicros = 20; 
void setup() {
  Serial.begin(115200);
  

  while (!Serial) { }

  pinMode(chargePin, OUTPUT);
  pinMode(voltageOutPin, INPUT);

  // Speed up ADC => prescaler=16 => ~77 kS/s
  ADCSRA &= 0b11111000; // Clear prescaler bits
  ADCSRA |= 0b00000100; // Set prescaler to 16

  digitalWrite(chargePin, HIGH);
  delay(chargeTimeMillis);

  digitalWrite(chargePin, LOW);

  unsigned long startTime = micros();
  for (int i = 0; i < bufferSize; i++) {
    while (micros() - startTime < (unsigned long)(i * sampleIntervalMicros)) {
    }
    outputBuffer[i] = analogRead(voltageOutPin);
  }

  for (int i = 0; i < bufferSize; i++) {
    Serial.write(reinterpret_cast<const byte*>(&outputBuffer[i]), sizeof(short));
  }

}

void loop() {
.
}
