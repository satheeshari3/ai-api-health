import requests
import time
from models.health_log import HealthLog
from extensions import db
from utils.logger import logger


def check_api_health(endpoint):

    start = time.time()

    try:
        response = requests.get(endpoint.url, timeout=5)
        status = response.status_code
        logger.info(f"Checked {endpoint.url} - status {status}")

    except Exception as e:
        logger.error(f"Health check failed for {endpoint.url}: {e}")
        status = 500

    response_time = time.time() - start

    log = HealthLog(
        endpoint_id=endpoint.id,
        status=status,
        response_time=response_time
    )

    db.session.add(log)
    db.session.commit()

    return log