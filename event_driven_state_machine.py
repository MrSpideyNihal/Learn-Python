"""Event-driven finite state machine."""
import enum
class States(enum.Enum):
    START = 1
    RUNNING = 2
    STOPPED = 3
def run_fsm():
    """Run the event-driven finite state machine."""
    current_state = States.START
    while True:
        if current_state == States.RUNNING:
            print("Running")
            # simulate some work
            time.sleep(1)
            current_state = States.STOPPED
        elif current_state == States.STOPPED:
            print("Stopped")
            # wait for restart signal
            time.sleep(2)
            current_state = States.RUNNING
if __name__ == "__main__":
    run_fsm()
