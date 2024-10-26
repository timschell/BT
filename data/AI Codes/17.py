import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def main():
    seconds = int(input("Enter time in seconds: "))
    countdown(seconds)

if __name__ == "__main__":
    main()
