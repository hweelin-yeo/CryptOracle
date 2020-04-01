# Package Scheduler.
from apscheduler.schedulers.blocking import BlockingScheduler

# Main cronjob function.
from app import cronjob, keepAliveJob

# Create an instance of scheduler and add function.
scheduler = BlockingScheduler()
scheduler.add_job(cronjob, "interval", hours=2)
scheduler.add_job(keepAliveJob, "interval", minutes=29)

scheduler.start()
