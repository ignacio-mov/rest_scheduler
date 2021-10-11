import os

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

TIMEZONE = os.environ['TIMEZONE']
DB_PATH = os.environ['SCHEDULER_DB']
LOG_LEVEL = os.environ['LOG_LEVEL']


class Config:
    """App configuration."""
    SCHEDULER_JOBSTORES = {"default": SQLAlchemyJobStore(url=DB_PATH)}
    SCHEDULER_TIMEZONE = TIMEZONE
    SCHEDULER_API_ENABLED = True
    SCHEDULER_JOB_DEFAULTS = {'misfire_grace_time': 15*60}
