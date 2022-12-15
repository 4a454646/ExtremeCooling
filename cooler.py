import portio
import time
import os

class EmbeddedController:
    # Embedded Controller Command, EC_SC
    EC_SC = 0x66
    # Embedded Controller Data
    EC_DATA = 0x62
    # Input Buffer Full (IBF) flag, Input Buffer is full 1, Input Buffer is empty 0
    IBF = 1
    # Output Buffer Full (OBF) flag, Output buffer is full 1, Output buffer is empty 0
    OBF = 0
    # Read Embedded Controller(RD_EC)
    RD_EC = 0x80
    # Write Embedded Controller(WR_EC)
    WR_EC = 0x81
    # Query Embedded Controller(QR_EC)
    QR_EC = 0x84
    # Extreme Cooling Register
    EXTREME_COOLING_REGISTER = 0xBD
    # ACTIVATE
    ACTIVATE_EXTREME_COOLING = 0x40
    # DEACTIVATE
    DEACTIVATE_EXTREME_COOLING = 0x00

    def __init__(self):
        for register in [self.EC_DATA, self.EC_SC]:
            status = portio.ioperm(register, 1, 1)

    def ec_wait(self, port, flag, value):
        for i in range(100):
            data = portio.inb(port)
            if ((data >> flag) & 0x1) == value:
                condition = True
                break
            time.sleep(0.001)

    def ec_read(self, port):
        self.ec_wait(self.EC_SC, self.IBF, 0)
        portio.outb(self.RD_EC, self.EC_SC)
        self.ec_wait(self.EC_SC, self.IBF, 0)
        portio.outb(port, self.EC_DATA)
        self.ec_wait(self.EC_SC, self.OBF, 1)
        result = portio.inb(self.EC_DATA)
        return result

    def ec_write(self, port, value):
        self.ec_wait(self.EC_SC, self.IBF, 0)
        portio.outb(self.WR_EC, self.EC_SC)
        self.ec_wait(self.EC_SC, self.IBF, 0)
        portio.outb(port, self.EC_DATA)
        self.ec_wait(self.EC_SC, self.IBF, 0)
        portio.outb(value, self.EC_DATA)
        self.ec_wait(self.EC_SC, self.IBF, 0)

    def activate_extreme_cooling(self):
        print("activated cooling")
        self.ec_write(self.EXTREME_COOLING_REGISTER, self.ACTIVATE_EXTREME_COOLING)

    def extreme_cooling_status(self):
        val = self.ec_read(self.EXTREME_COOLING_REGISTER)
        if hex(val) == hex(self.ACTIVATE_EXTREME_COOLING):
            print("cooling was active")
            return True
        else:
            print("cooling was inactive")
            return False

    def deactivate_extreme_cooling(self):
        print("deactivated cooling")
        self.ec_write(self.EXTREME_COOLING_REGISTER, self.DEACTIVATE_EXTREME_COOLING)


embeddedController = EmbeddedController()
if (embeddedController.extreme_cooling_status()):
    embeddedController.deactivate_extreme_cooling()
else:
    embeddedController.activate_extreme_cooling()
