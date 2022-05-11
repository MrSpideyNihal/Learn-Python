"""Simple Alarm Clock."""
import datetime

def set_alarm(alarm_time):
    """Set an alarm for the specified time."""
    now = datetime.datetime.now()
    delay = (datetime.datetime.strptime(alarm_time, "%H:%M") - now).total_seconds()
    if delay > 0:
        import time
        print(f"Alarm set for {alarm_time}. Waiting...")
        time.sleep(delay)
        print("Wake up! It's alarm time.")

if __name__ == "__main__":
    while True:
        now = datetime.datetime.now()
        if now.hour == 8 and now.minute == 30:
            set_alarm("08:30")
        else:
            print(f"Current time: {now.hour}:{now.minute}")
            time.sleep(60)
