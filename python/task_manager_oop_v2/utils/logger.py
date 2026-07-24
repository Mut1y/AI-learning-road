import logging
import os


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)


LOG_DIR = os.path.join(BASE_DIR, "logs")


os.makedirs(LOG_DIR, exist_ok=True)


LOG_FILE = os.path.join(
    LOG_DIR,
    "app.log"
)


logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILE,
    format="%(asctime)s %(levelname)s %(message)s",
    encoding="utf-8"
)


logger = logging.getLogger(__name__)