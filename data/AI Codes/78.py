import datetime

def log_temperature(temp):
    with open('temperature_log.txt', 'a') as file:
        timestamp = datetime.datetime.now()
        file.write(f"{timestamp}: {temp}°C\n")

def main():
    print("Temperature Logger")
    while True:
        temp = input("Enter temperature (or type 'quit' to exit): ")
        if temp.lower() == 'quit':
            break
        try:
            temp = float(temp)
            log_temperature(temp)
            print("Temperature logged.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
