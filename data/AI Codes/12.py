import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()
        print("Stopwatch started.")

    def stop(self):
        self.end_time = time.time()
        print("Stopwatch stopped.")

    def elapsed_time(self):
        if self.start_time is None:
            print("Stopwatch has not been started.")
        elif self.end_time is None:
            print("Stopwatch is still running.")
        else:
            elapsed = self.end_time - self.start_time
            print(f"Elapsed time: {elapsed:.2f} seconds")

def main():
    sw = Stopwatch()
    while True:
        command = input("Enter 'start', 'stop', 'time', or 'exit': ").lower()
        if command == 'start':
            sw.start()
        elif command == 'stop':
            sw.stop()
        elif command == 'time':
            sw.elapsed_time()
        elif command == 'exit':
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
