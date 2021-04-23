// Transmit rate in bps
#define TX_RATE 5

// Pin assignments
#define TX_CLOCK D2
#define TX_DATA D3


const char *message = "Hello, world!";

void setup() {
  delay(5000);
  pinMode(TX_CLOCK, OUTPUT);
  pinMode(TX_DATA, OUTPUT);

  // Initialize the LCD screen
  Serial.begin(9600);

//  get per word
  for (int byte_idx = 0; byte_idx < strlen(message); byte_idx++) {
    char tx_byte = message[byte_idx];
    Serial.println(tx_byte);
    
//    get logic in 8 bit
    for (int bit_idx = 0; bit_idx < 8; bit_idx++) {
      
      bool tx_bit = tx_byte & (0x80 >> bit_idx); //check true or false in bit position by tx_byte
    
      digitalWrite(TX_DATA, tx_bit);
      delay((1000 / TX_RATE) / 2);

      
      Serial.print(tx_bit ? "1" : "0");
      

      // Pulse clock
      digitalWrite(TX_CLOCK, HIGH);
      delay((1000 / TX_RATE) / 2);
      digitalWrite(TX_CLOCK, LOW);      
    }
    Serial.println("");
  }
  digitalWrite(TX_DATA, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:

}
