# Package Scheduler.
from apscheduler.schedulers.blocking import BlockingScheduler

# Main cronjob function.
from app import cronjob

# Create an instance of scheduler and add function.
scheduler = BlockingScheduler()
scheduler.add_job(cronjob, "interval", seconds=30)

scheduler.start()
