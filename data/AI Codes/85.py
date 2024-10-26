import time

def stopwatch():
    input("Press Enter to start the stopwatch...")
    start_time = time.time()
    lap_times = []
    
    while True:
        command = input("Enter 'lap' to record a lap time, 'stop' to stop, or 'quit' to quit: ")
        if command == 'lap':
            lap_time = time.time() - start_time
            lap_times.append(lap_time)
            print(f"Lap {len(lap_times)}: {lap_time:.2f} seconds")
        elif command == 'stop':
            end_time = time.time()
            total_time = end_time - start_time
            print(f"Total time: {total_time:.2f} seconds")
            break
        elif command == 'quit':
            break

def main():
    stopwatch()

if __name__ == "__main__":
    main()
