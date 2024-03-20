basic.forever(function () {
    if (maqueenPlusV2.readUltrasonic(DigitalPin.P13, DigitalPin.P14) > 15) {
        maqueenPlusV2.controlMotor(maqueenPlusV2.MyEnumMotor.AllMotor, maqueenPlusV2.MyEnumDir.Forward, 50)
    }
    if (maqueenPlusV2.readUltrasonic(DigitalPin.P13, DigitalPin.P14) < 15 && maqueenPlusV2.readUltrasonic(DigitalPin.P13, DigitalPin.P14) > 15) {
        maqueenPlusV2.controlMotorStop(maqueenPlusV2.MyEnumMotor.AllMotor)
    }
    if (maqueenPlusV2.readUltrasonic(DigitalPin.P13, DigitalPin.P14) < 15) {
        maqueenPlusV2.controlMotor(maqueenPlusV2.MyEnumMotor.AllMotor, maqueenPlusV2.MyEnumDir.Forward, 50)
    }
})
