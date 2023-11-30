import schedule
import time

def task():
    print("Task executed at", time.strftime("%Y-%m-%d %H:%M:%S"))

def schedule_task_at_specific_time():
    scheduled_time = "2023-12-01 12:00:00"  # Change this to the desired time
    schedule.every().day.at(scheduled_time).do(task)

def schedule_task_at_interval():
    interval_in_minutes = 5  # Change this to the desired interval
    schedule.every(interval_in_minutes).minutes.do(task)

if __name__ == "__main__":
    # Schedule tasks
    schedule_task_at_specific_time()
    schedule_task_at_interval()

    # Run the scheduler
    while True:
        schedule.run_pending()
        time.sleep(1)
