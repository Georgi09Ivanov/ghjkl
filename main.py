// Set servo angle at pin P13 (Servo 1) on start
maqueen.servoRun(maqueen.Servos.S1, 90)

// Example: Move the servo motor up and down
basic.forever(function () {
    // Move servo up (angle 0)
    maqueen.servoRun(maqueen.Servos.S1, 0)
    basic.pause(1000) // Adjust this delay based on your servo's response time
    
    // Move servo down (angle 180)
    maqueen.servoRun(maqueen.Servos.S1, 180)
    basic.pause(1000) // Adjust this delay based on your servo's response time
})
