import time

print("Worker service started...")

while True:
    # In real system: listen to Redis queue and process PDFs
    print("Worker idle, waiting for jobs...")
    time.sleep(10)
