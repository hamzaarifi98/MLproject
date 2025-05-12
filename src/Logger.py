# logger.py
import logging
import os
from datetime import datetime

# Create log directory if it doesn't exist
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# Create log file with timestamp
log_filename = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(log_dir, log_filename)

# Configure logging
logging.basicConfig(
    filename=log_path,
    level=logging.DEBUG,
    format="[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)d] - %(message)s",
    force=True  # Ensures reconfiguration even if already set elsewhere
)

# Create a logger object to be reused
logger = logging.getLogger(__name__)

# Optional: test log
logger.info("Logger initialized.")

# Print log path for verification
print(f"✅ Logging to: {log_path}")
