# mBot Line follower

Use the mBot to follow a black line on a white floor. Like this:

<iframe src="https://www.youtube.com/embed/bwMmDUPhPLE" frameborder="0" allowfullscreen></iframe>

Use the Arduino environment to program the mBot, not the mBlock ide. Follow [these instructions](https://support.makeblock.com/hc/en-us/articles/4419572961943-Program-mBot-in-Arduino-IDE) to get started.


To get started here below are some example sketches.

### Read line sensor

    /*
      Read mBot line sensor
    */

    // sensor is connected to mBlock input 3 (A2 and A3)
    int sensor1 = A2;
    int sensor2 = A3;


    void setup() {
      Serial.begin(9600);

      pinMode(sensor1, INPUT);
      pinMode(sensor2, INPUT);
    }

    void loop() {
      // read the sensors
      int sensorState1 = digitalRead(sensor1);
      int sensorState2 = digitalRead(sensor2);

      // show
      Serial.print(sensorState1);
      Serial.print("-");
      Serial.println(sensorState2);

      delay(10);
    }

### Use motors

    /*
      Control mBot motors
    */
    // Each motor has a pwm input to set the speed
    int pwm1 = 5; //right
    int pwm2 = 6; //left

    // Each motor has a direction pin to set it to forward or backward driving
    int dir1 = 4;
    int dir2 = 7;

    void setup() {
      pinMode(pwm1, OUTPUT);
      pinMode(pwm2, OUTPUT);

      pinMode(dir1, OUTPUT);
      pinMode(dir2, OUTPUT);

    }

    void loop() {
      analogWrite(pwm1, 255);   // full speed
      digitalWrite(dir1, HIGH); // forward
      analogWrite(pwm2, 255);   // full speed
      digitalWrite(dir2, LOW);  // forward
    }

### Use sonar

    /*
      Ping mBot sonar
    */

    // this constant won't change. It's the pin number of the sensor's output:
    const int pingPin = A1;

    void setup() {
      // initialize serial communication:
      Serial.begin(9600);
    }

    void loop() {
      long duration, cm;

      duration = ping(pingPin);
      cm = microsecondsToCentimeters(duration);

      Serial.print(cm);
      Serial.print("cm");
      Serial.println();
      delay(100);
    }

    long ping(int pin) {
      // send pulse
      pinMode(pin, OUTPUT);
      digitalWrite(pin, LOW);
      delayMicroseconds(2);
      digitalWrite(pin, HIGH);
      delayMicroseconds(5);
      digitalWrite(pin, LOW);

      // get response
      pinMode(pin, INPUT);
      return pulseIn(pin, HIGH);
    }

    long microsecondsToCentimeters(long microseconds) {
      return microseconds / 29 / 2;
    }
