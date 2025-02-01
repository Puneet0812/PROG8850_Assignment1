import os
import time
import subprocess

# MySQL Configuration
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""  # Leave empty if no password is set
DB_NAME = "prog8850_assignment"

# Generate a unique filename
timestamp = time.strftime("%Y%m%d-%H%M%S")
backup_file = f"backup_{DB_NAME}_{timestamp}.sql"

# Command to create a backup
backup_command = f"mysqldump -h {DB_HOST} -u {DB_USER} -p{DB_PASSWORD} {DB_NAME} > {backup_file}"

try:
    subprocess.run(backup_command, shell=True, check=True)
    print(f"Backup successful! File saved as {backup_file}")
except Exception as e:
    print(f"Backup failed: {e}")
