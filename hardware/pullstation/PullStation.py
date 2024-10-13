import RPi.GPIO as GPIO
import time


# Script for pi zero (mount pi inside pullstation)


# Pin configuration
PULL_STATION_PIN = 17  # GPIO pin for the pull station
BUZZER_PIN = 18        # GPIO pin for the buzzer

# Setup
GPIO.setmode(GPIO.BCM)  # Use BCM numbering
GPIO.setup(PULL_STATION_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Pull-up resistor
GPIO.setup(BUZZER_PIN, GPIO.OUT)  # Set buzzer pin as an output

pulled = False  # Variable to track the pull state

try:
    print("Press CTRL+C to exit.")
    while True:
        input_state = GPIO.input(PULL_STATION_PIN)
        if input_state == GPIO.LOW and not pulled:
            print("Fire alarm pull station activated!")  # Message displayed when pulled
            GPIO.output(BUZZER_PIN, GPIO.HIGH)  # Activate buzzer
            pulled = True  # Set pulled to True
        elif input_state == GPIO.HIGH and pulled:
            # Do nothing; the buzzer stays on indefinitely
            pass  # Added a pass statement for clarity

        time.sleep(0.1)  # Short delay to avoid excessive checking

except KeyboardInterrupt:
    print("Program interrupted")

finally:
    GPIO.output(BUZZER_PIN, GPIO.LOW)  # Ensure buzzer is off on exit
    GPIO.cleanup()  # Clean up GPIO when the program is terminated
