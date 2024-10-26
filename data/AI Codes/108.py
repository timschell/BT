import time
import threading

def set_alarm(alarm_time):
    def alarm():
        while True:
            current_time = time.strftime("%H:%M:%S")
            if current_time == alarm_time:
                print("Wake up!")
                break
            time.sleep(1)
    thread = threading.Thread(target=alarm)
    thread.start()

def main():
    print("Alarm Clock")
    alarm_time = input("Set alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()
