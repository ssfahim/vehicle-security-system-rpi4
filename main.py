import config
import time
from sensor_handlers import setup_sensors, monitor_sensors
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def main():
    print("[INFO] Vehicle Security System Starting...")
    setup_sensors()
    try:
        while True:
            monitor_sensors()
            time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
