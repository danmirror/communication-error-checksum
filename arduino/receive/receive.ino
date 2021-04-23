#define RX_CLOCK D2
#define RX_DATA D3

char message[16];
volatile byte rx_byte = 0;
volatile int bit_position = 0;

void setup() {
  Serial.begin(9600);
  
  pinMode(RX_DATA, INPUT);
  strcpy(message, "");
  
  attachInterrupt(digitalPinToInterrupt(RX_CLOCK), onClockPulse, RISING);
}

ICACHE_RAM_ATTR void onClockPulse() {
  bool rx_bit = digitalRead(RX_DATA);

  if (bit_position == 8) {
    rx_byte = 0;
    bit_position = 0;
  }
  
  if (rx_bit) {
    rx_byte |= (0x80 >> bit_position);
  }

  bit_position += 1;

  if (bit_position == 8) {
    strncat(message, (const char *)&rx_byte, 1);
  }
  
  Serial.println(message);
}

void loop() {
   
//    for (int i = 0; i < 8; i += 1) {
//      if (i < bit_position) {
//        Serial.print(rx_byte & (0x80 >> i) ? "1" : "0");
//      }
//    }

}
