import logging 
import os
from datetime import datetime

# 1. Create a filename based on current time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Create a path to the FOLDER only, not the file
# logs_path = os.path.join(os.getcwd(), "logs",LOG_FILE) -> have to create folder first and then file
logs_path = os.path.join(os.getcwd(), "logs") 
os.makedirs(logs_path, exist_ok=True)

# 3. Create the full path (folder + filename)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")