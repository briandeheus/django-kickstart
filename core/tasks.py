import logging

from celery import shared_task

log = logging.getLogger(__name__)


@shared_task()
def sample_task():
    # Printing all levels to see log filtering in action.
    log.debug("Sample task running!")
    log.info("Sample task running!")
    log.warning("Sample task running!")
    log.error("Sample task running!")
    log.fatal("Sample task running!")
