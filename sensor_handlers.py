import config
import RPi.GPIO as GPIO
import time
from notifications import send_alert

def setup_sensors():
    GPIO.setup(config.BUZZER_PIN, GPIO.OUT)
    GPIO.setup(config.ALERT_LED_PIN, GPIO.OUT)
    GPIO.setup(config.ARM_DISARM_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(config.VIBRATION_PINS, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(config.REED_PINS, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(config.ULTRASONIC_TRIGGER_PIN, GPIO.OUT)
    GPIO.setup(config.ULTRASONIC_ECHO_PIN, GPIO.IN)

def measure_distance():
    GPIO.output(config.ULTRASONIC_TRIGGER_PIN, False)
    time.sleep(0.01)
    GPIO.output(config.ULTRASONIC_TRIGGER_PIN, True)
    time.sleep(0.00001)
    GPIO.output(config.ULTRASONIC_TRIGGER_PIN, False)

    while GPIO.input(config.ULTRASONIC_ECHO_PIN) == 0:
        pulse_start = time.time()
    while GPIO.input(config.ULTRASONIC_ECHO_PIN) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    return pulse_duration * 17150  # cm
    
    
def monitor_sensors():
    alert_triggered = False
    

    distance = measure_distance()
    if distance < config.ULTRASONIC_DISTANCE_CM:
        send_alert("Ultrasonic Proximity Alert!")
        print(distance)
        alert_triggered = True
        
    elif GPIO.input(config.VIBRATION_PINS) == 0:
        print("Vibration Detected!")
        alert_triggered = True
        
    elif GPIO.input(config.REED_PINS) == 0:
        print("Reed Switch Triggered!")
        alert_triggered = True



    # Flash LED and buzz if alert is triggered
    if alert_triggered:
        GPIO.output(config.ALERT_LED_PIN, GPIO.HIGH)
        GPIO.output(config.BUZZER_PIN, GPIO.LOW)

    else:
        GPIO.output(config.BUZZER_PIN, GPIO.HIGH)
        GPIO.output(config.ALERT_LED_PIN, GPIO.LOW)


