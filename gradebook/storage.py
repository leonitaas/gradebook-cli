import json
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "gradebook.json"
LOG_PATH = BASE_DIR / "logs" / "app.log"

LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_data():
    try:
        with open(DATA_PATH, "r") as f:
            return json.load(f)

    except FileNotFoundError:
        logging.info("No data file found. Starting fresh.")
        return {"students": [], "courses": [], "enrollments": []}

    except json.JSONDecodeError:
        logging.error("Corrupted JSON file.")
        print("Corrupted data file. Resetting...")
        return {"students": [], "courses": [], "enrollments": []}


def save_data(data):
    try:
        with open(DATA_PATH, "w") as f:
            json.dump(data, f, indent=4)

        logging.info("Data saved successfully.")

    except Exception as e:
        logging.error(f"Error saving data: {e}")