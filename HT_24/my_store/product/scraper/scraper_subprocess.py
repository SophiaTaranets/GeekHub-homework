import subprocess
import sys
import os


def run_scraper_in_subprocess(product_id):
    try:
        current_file_directory = os.path.dirname(os.path.abspath(__file__))
        scraper_script_path = os.path.join(current_file_directory, 'sears_api.py')

        python_executable = sys.executable
        command = [python_executable, scraper_script_path, product_id]

        subprocess.run(command, check=True, capture_output=True, text=True)

        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running scraper for product {product_id}: {e}")
        return False
