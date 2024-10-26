import time

class AlarmClock:
    def __init__(self):
        self.alarms = []

    def add_alarm(self, hour, minute):
        self.alarms.append((hour, minute))

    def list_alarms(self):
        for alarm in self.alarms:
            print(f"Alarm set for {alarm[0]:02}:{alarm[1]:02}")

    def check_alarms(self):
        current_time = time.localtime()
        current_hour = current_time.tm_hour
        current_minute = current_time.tm_min

        for alarm in self.alarms:
            if alarm == (current_hour, current_minute):
                print("Alarm ringing! Wake up!")

def main():
    clock = AlarmClock()
    while True:
        print("\n1. Set Alarm")
        print("2. List Alarms")
        print("3. Quit")

        choice = input("Enter your choice: ")
        if choice == '3':
            break
        elif choice == '1':
            hour = int(input("Enter hour: "))
            minute = int(input("Enter minute: "))
            clock.add_alarm(hour, minute)
        elif choice == '2':
            clock.list_alarms()
        else:
            print("Invalid choice. Please try again.")

        time.sleep(1)
        clock.check_alarms()

if __name__ == "__main__":
    main()
