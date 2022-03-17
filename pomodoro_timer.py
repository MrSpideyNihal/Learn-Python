"""Pomodoro timer."""
import time

def start_pomodoro(duration):
    """Start a Pomodoro timer for the specified duration."""
    while True:
        print(f"Working... ({duration} seconds remaining)")
        time.sleep(duration)
        print(f"Break! (5 minutes)"
        time.sleep(300)

if __name__ == "__main__":
    start_pomodoro(60)
