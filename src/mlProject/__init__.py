import os
import logging
import sys

logging_str = "[%(asctime)s - %(levelname)s - %(module)s - %(message)s]"

log_dir = "logs"

logs_filepath = os.path.join(log_dir,"running_logs")
os.makedirs(log_dir,exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(filename=logs_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("this is the first logger in the ligging file")