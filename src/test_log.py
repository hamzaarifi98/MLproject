import logging
import os
from datetime import datetime

# Step 1: Setup log directory
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Step 2: Create a log file path
log_file_name = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
log_file_path = os.path.join(log_dir, log_file_name)

# Print for confirmation
print(f"Expected log file path: {log_file_path}")

# Step 3: Setup logging (force=True ensures it applies)
logging.basicConfig(
    filename=log_file_path,
    filemode='w',  # Overwrite each time
    format='[%(asctime)s] [%(levelname)s] - %(message)s',
    level=logging.INFO,
    force=True
)

# Step 4: Write a log
logging.info("✅ Hello, logging is working!")

# Step 5: Verify log file
if os.path.exists(log_file_path):
    print("✅ Log file created.")
    with open(log_file_path) as f:
        print("\n📄 Contents of log file:")
        print(f.read())
else:
    print("❌ Log file NOT created.")
