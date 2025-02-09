import RPi.GPIO as GPIO
import time

# GPIOピンの設定（各モーターの制御用ピン）
Motor1A = 17  # 左モーター IN1（前進）
Motor1B = 18  # 左モーター IN2（後退）
Motor1E = 24  # 左モーター ENA (PWM制御)
Motor2A = 22  # 右モーター IN3（前進）
Motor2B = 23  # 右モーター IN4（後退）
Motor2E = 27  # 右モーター ENB (PWM制御)

# GPIOの初期化
GPIO.setmode(GPIO.BCM)  # GPIOピンの番号指定方式をBCMに設定
GPIO.setup([Motor1A, Motor1B, Motor1E, Motor2A, Motor2B, Motor2E], GPIO.OUT)  # 全ピンを出力モードに設定

# PWMの設定
pwm_left = GPIO.PWM(Motor1E, 100)  # 左モーターのPWM（100Hz）
pwm_right = GPIO.PWM(Motor2E, 100)  # 右モーターのPWM（100Hz）
pwm_left.start(0)  # 初期デューティサイクル0%
pwm_right.start(0)

def motor_forward(speed=50, duration=1):
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    pwm_left.ChangeDutyCycle(speed)
    pwm_right.ChangeDutyCycle(speed - 5)
    time.sleep(duration)
    motor_stop()

def motor_backward(speed=50, duration=1):
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    pwm_left.ChangeDutyCycle(speed)
    pwm_right.ChangeDutyCycle(speed - 5)
    time.sleep(duration)
    motor_stop()

def turn_left(speed=50, duration=1):
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    pwm_left.ChangeDutyCycle(0)
    pwm_right.ChangeDutyCycle(speed)
    time.sleep(duration)
    motor_stop()

def turn_right(speed=50, duration=1):
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.LOW)
    pwm_left.ChangeDutyCycle(speed)
    pwm_right.ChangeDutyCycle(0)
    time.sleep(duration)
    motor_stop()

def motor_stop():
    for speed in range(50, -1, -5):
        pwm_left.ChangeDutyCycle(speed)
        pwm_right.ChangeDutyCycle(speed)
        time.sleep(0.1)
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.LOW)
    pwm_left.ChangeDutyCycle(0)
    pwm_right.ChangeDutyCycle(0)

def move(direction, speed=50, duration=1):
    try:
        if direction == "forward":
            motor_forward(speed, duration)
        elif direction == "backward":
            motor_backward(speed, duration)
        elif direction == "left":
            turn_left(speed, duration)
        elif direction == "right":
            turn_right(speed, duration)
        else:
            print("Invalid direction!")
    finally:
        print("ループ中")
