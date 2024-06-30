import os
import subprocess
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='install_dependencies.log')

def run_command(command):
    try:
        subprocess.check_call(command, shell=True)
        logging.info(f"Command succeeded: {command}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {command}\nError: {e}")

# Upgrade pip, setuptools, and wheel
run_command("pip install --upgrade pip setuptools wheel")

# Clear pip cache
run_command("pip cache purge")

# Create requirements.txt
requirements = """
pandas
notebook
numpy
scikit-learn
matplotlib
python-box==6.0.2
pyYAML
ensure==1.0.2
joblib
types-PyYAML
Flask
Flask-Cors
"""

with open('requirements.txt', 'w') as f:
    f.write(requirements)
logging.info("Created requirements.txt")

# Install dependencies without cache
run_command("pip install --no-cache-dir -r requirements.txt")
