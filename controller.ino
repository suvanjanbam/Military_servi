// Motor A connections
int enA1 = 3;
int in1_1 = 4;
int in2_1 = 5;
// Motor B connections
int enB1 = 8;
int in3_1 = 6;
int in4_1 = 7;

void setup() {

   // Initialize the serial communication
  Serial.begin(9600);

  // put your setup code here, to run once:
  pinMode(enA1, OUTPUT);
  pinMode(enB1, OUTPUT);
  pinMode(in1_1, OUTPUT);
  pinMode(in2_1, OUTPUT);
  pinMode(in3_1, OUTPUT);
  pinMode(in4_1, OUTPUT);

}
void backwardMove(){
  Serial.println("FOR");
  digitalWrite(enA1, HIGH);
  digitalWrite(enB1, HIGH);

  digitalWrite(in1_1, LOW);
  digitalWrite(in2_1, HIGH);
  digitalWrite(in3_1, LOW);
  digitalWrite(in4_1, HIGH);
  
}

void forwardMove(){
    Serial.print("Back");
  // Turn on motors
  digitalWrite(enA1, HIGH);
  digitalWrite(enB1, HIGH);

  digitalWrite(in1_1, HIGH);
  digitalWrite(in2_1, LOW);
  digitalWrite(in3_1, HIGH);
  digitalWrite(in4_1, LOW);
}

void stopMotors() {
  // Turn off motors
  Serial.print("Stop");
  digitalWrite(enA1, LOW);
  digitalWrite(enB1, LOW);
}

void turnRight(){
  Serial.print("Right");
  digitalWrite(enA1, LOW);
  digitalWrite(enB1, HIGH);
}

void turnLeft(){
  Serial.print("Left");
  digitalWrite(enA1, HIGH);
  digitalWrite(enB1, LOW);
}


void loop() {
  if (Serial.available()) {
    char command = Serial.read(); 


    switch (command) {
      case 'w':
        forwardMove();
        break;
      
      case 's':
        backwardMove();
        break;

      case 'q':
        stopMotors();
        break;        

      case 'a':
        turnLeft();
        break;        
      
      case 'd':
        turnRight();
        break;        

        
      default:
//        stopMotors();
        break;
    }
  }
}
