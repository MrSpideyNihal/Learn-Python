"""Performance regression detector."""
import time
def detect_regression():
    """Detect performance regressions by comparing execution times."""
    start_time = time.time()
    # simulate some work
    time.sleep(1)
    end_time = time.time()
    baseline_execution_time = end_time - start_time
    for _ in range(10):
        start_time = time.time()
        # simulate some work
        time.sleep(1)
        end_time = time.time()
        execution_time = end_time - start_time
        if abs(execution_time - baseline_execution_time) > 0.5:
            print("Performance regression detected")
if __name__ == "__main__":
    detect_regression()
