import subprocess
import os
import sys
import logging

def regenerate_requirements():
    # Set up logging
    logging.basicConfig(filename='pipreqs_errors.log', level=logging.ERROR)
    
    try:
        # Specify the encoding explicitly to avoid decoding errors
        result = subprocess.run(['pipreqs', '.', '--ignore', '.venv', '--force'], capture_output=True, text=True)
        if result.returncode != 0:
            logging.error(result.stderr)
            print("Error occurred. Check pipreqs_errors.log for details.")
            sys.exit(result.returncode)
        subprocess.run(['git', 'add', 'requirements.txt'])
    except UnicodeDecodeError as e:
        logging.error(f"UnicodeDecodeError: {e}")
        print("UnicodeDecodeError occurred. Check pipreqs_errors.log for details.")
        sys.exit(1)

if __name__ == "__main__":
    regenerate_requirements()