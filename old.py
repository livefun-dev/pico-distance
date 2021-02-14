import utime
from machine import PWM, Pin, ADC

pin = Pin(25, Pin.OUT)

duty = 0
direction = 1

adc = ADC(2)
conversion_factor = 3.3 / (65535)
while True:
    m = adc.read_u16() * conversion_factor

    if (m > 2):
        pin.value(0)
    else:
        pin.value(1)
    print("mes:", m)
    # duty += direction
    # if duty > 255:
    #     duty = 255
    #     direction = -1
    # elif duty < 0:
    #     duty = 0
    #     direction = 1
    # pin.duty_u16(duty*duty)
    utime.sleep(0.1)
