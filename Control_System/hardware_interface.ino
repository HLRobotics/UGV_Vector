/*Author:Akhil Jacob*/
/* include library */
#include <ESP8266WiFi.h>
#include <Servo.h>
 
/* define port */
WiFiClient client;
WiFiServer server(80);
 
/* WIFI settings */
const char* ssid = "GNXS-5G-A15067";
const char* password = "mrf37600";
 
/* data received from application */
String  data = "";
 
/* define L298N or L293D motor control pins */
int leftMotorForward = 16;      /* GPIO16(D0) -> IN3   */
int rightMotorForward = 12;     /* GPIO12(D6) -> IN1  */
int leftMotorBackward = 15;     /* GPIO15(D8) -> IN4   */
int rightMotorBackward = 13;    /* GPIO13(D7) -> IN2  */
int leftEnable=2;               /* GPIO2(D4) -> IN2  */
int rightEnable=14;             /* GPIO14(D5) -> IN2  */
int speed=75;   
int servo_default_position=90;                

/* define servo */
Servo baseServo;
Servo panServo;
 
 
void setup()
{
  Serial.begin(115200);
  /* initialize motor control pins as output */
  pinMode(leftMotorForward, OUTPUT);
  pinMode(rightMotorForward, OUTPUT);
  pinMode(leftMotorBackward, OUTPUT);
  pinMode(rightMotorBackward, OUTPUT);
  pinMode(leftEnable,OUTPUT);
  pinMode(rightEnable,OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  baseServo.attach(4);      /* GPIO4(D2) -> IN2  */
  panServo.attach(0);       /* GPIO0(D3) -> IN2  */

  //connect to your local wi-fi network
  WiFi.begin(ssid, password);
 
  // Attempt to connect to WiFi network:
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    // Connect to WPA/WPA2 network. Change this line if using open or WEP  network:
    // Wait 3 seconds for connection:
    delay(3000);
  }
 
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());   //You can get IP address assigned to ESP
 
  /* start server communication */
  server.begin();
}
 
void loop()
{


  /* If the server available, run the "checkClient" function */
  client = server.available();

  if (!client) return;
  data = checkClient ();
 
  /************************ Run function according to incoming data from application *************************/
 
  /* If the incoming data is "w", run the "MotorForward" function */
  if (data == "w") MotorForward();
  /* If the incoming data is "s", run the "MotorBackward" function */
  else if (data == "s") MotorBackward();
  /* If the incoming data is "a", run the "TurnLeft" function */
  else if (data == "a") TurnLeft();
  /* If the incoming data is "d", run the "TurnRight" function */
  else if (data == "d") TurnRight();
  /* If the incoming data is "x", run the "MotorStop" function */
  else if (data == "x") MotorStop();
  /* controlling the speed according to input */
  if (data.toInt() > 50 || data.toInt() <120)
  {
     speedController(data.toInt());
  }
  /* Servo controller pending */
}
 
/********************************************* FORWARD *****************************************************/
void MotorForward(void)
{
  digitalWrite(leftMotorForward, HIGH);
  digitalWrite(rightMotorForward, HIGH);
  digitalWrite(leftMotorBackward, LOW);
  digitalWrite(rightMotorBackward, LOW);
  speedController(speed);
  Serial.println("Moving Forward");
}
 
/********************************************* BACKWARD *****************************************************/
void MotorBackward(void)
{
  digitalWrite(leftMotorBackward, HIGH);
  digitalWrite(rightMotorBackward, HIGH);
  digitalWrite(leftMotorForward, LOW);
  digitalWrite(rightMotorForward, LOW);
  speedController(speed);
  Serial.println("Moving Backward");
}
 
/********************************************* TURN LEFT *****************************************************/
void TurnLeft(void)
{
  digitalWrite(leftMotorForward, LOW);
  digitalWrite(rightMotorForward, HIGH);
  digitalWrite(rightMotorBackward, LOW);
  digitalWrite(leftMotorBackward, HIGH);
  speedController(speed);
  Serial.println("Moving Left");
}
 
/********************************************* TURN RIGHT *****************************************************/
void TurnRight(void)
{
  digitalWrite(leftMotorForward, HIGH);
  digitalWrite(rightMotorForward, LOW);
  digitalWrite(rightMotorBackward, HIGH);
  digitalWrite(leftMotorBackward, LOW);
  speedController(speed);
  Serial.println("Moving Right");
}
 
/********************************************* STOP *****************************************************/
void MotorStop(void)
{
  digitalWrite(leftMotorForward, LOW);
  digitalWrite(leftMotorBackward, LOW);
  digitalWrite(rightMotorForward, LOW);
  digitalWrite(rightMotorBackward, LOW);
  speedController(0);
  Serial.println("Stop");
}
 
/********************************** RECEIVE DATA FROM the APP ******************************************/
String checkClient (void)
{
  while (!client.available()) delay(1);
  String request = client.readStringUntil('\r');
  request.remove(0, 5);
  request.remove(request.length() - 9, 9);
  return request;
}

/********************************** SPEED CONTROLLER ******************************************/

void speedController(int speed)
{
  analogWrite(rightEnable,speed);
  analogWrite(leftEnable,speed);
}

/********************************** BASE SERVO POSITION CONTROLLER ******************************************/

void servoController(int base_angle,int pan_angle)
{
  baseServo.write(base_angle);
  panServo.write(pan_angle);
}