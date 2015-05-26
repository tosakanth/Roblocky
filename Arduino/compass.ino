#include <Wire.h>
#include <HMC5883L.h>


HMC5883L compass;

void setup() {
  // put your setup code here, to run once:
   Wire.begin();
   Serial.begin(9600);
   compass = HMC5883L(); //new instance of HMC5883L library
   setupHMC5883L();
}

void loop() {
  float heading = getHeading();
  Serial.print("Heading to ");
  Serial.print(heading,2);
  Serial.println(" degree");


 delay(500);
}

void setupHMC5883L(){
//Setup the HMC5883L, and check for errors
  int error;
  error = compass.SetScale(1.3); //Set the scale of the compass.
  if(error != 0) Serial.println(compass.GetErrorText(error)); //check if there is an error, and print if so
  error = compass.SetMeasurementMode(Measurement_Continuous); // Set the measurement mode to Continuous
  if(error != 0) Serial.println(compass.GetErrorText(error)); //check if there is an error, and print if so
}

float getHeading(){
  //Get the reading from the HMC5883L and calculate the heading
  MagnetometerScaled scaled = compass.ReadScaledAxis(); //scaled values from compass.
  float heading = atan2(scaled.YAxis, scaled.XAxis);

  // Correct for when signs are reversed.
  if(heading < 0) heading += 2*PI;
  if(heading > 2*PI) heading -= 2*PI;

  return heading * RAD_TO_DEG; //radians to degrees
}
