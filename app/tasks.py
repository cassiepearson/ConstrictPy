from constrictpy.analyze import analyzeJob
from constrictpy.logger import getLogger
from app import app, db
from app.models import Job
from rq import get_current_job


app.app_context().push()

logger = getLogger(__name__, logmode="info")


def analyze_job(j: Job) -> None:
    job = get_current_job()
    logger.info("Analyzing {}".format(j.name))
    analyzeJob(j)
    logger.info("Analysis completed: {}".format(j.name))
    j.complete = True
    job.complete = True
    db.session.commit()
