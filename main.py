direction = False
U = 0
DFRobotMaqueenPlus.I2CInit()
DFRobotMaqueenPlus.PID(PID.OFF)

def on_forever():
    global U, direction
    U = DFRobotMaqueenPlus.ultraSonic(PIN.P1, PIN.P2)
    if U < 20 and U != 0:
        direction = Math.random_boolean()
        if direction == True:
            DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, 100)
            DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CW, 0)
            basic.pause(1000)
        else:
            DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, 0)
            DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CW, 100)
            basic.pause(1000)
    else:
        DFRobotMaqueenPlus.mototRun(Motors.ALL, Dir.CW, 100)
basic.forever(on_forever)
