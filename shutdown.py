"""Signal-based graceful shutdown."""
import signal

def shutdown():
    """Raise SIGINT to exit gracefully."""
    def sigint_handler(signum, frame):
        print("Shutting down...\n")
        raise SystemExit(0)
    signal.signal(signal.SIGINT, sigint_handler)

if __name__ == "__main__":
    shutdown()
