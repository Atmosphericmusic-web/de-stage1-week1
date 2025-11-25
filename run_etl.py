from pathlib import Path
import json

from etl.reader import read_data
from etl.transform import transform_data
from etl.writer import write_data

def load_config(config_path: Path) -> dict:
    with config_path.open("r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    config = load_config(base_dir / "config.json")

    source = base_dir / config["source_path"]
    db_path = base_dir / config["db_path"]

    print("ETL v2 starting...")
    rows = read_data(source)
    rows = transform_data(rows)
    write_data(rows, db_path)
    print("ETL v2 finished.")
