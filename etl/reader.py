from pathlib import Path
import csv


def read_data(source_path: Path) -> list[dict]:
    print(f"[reader] Читаю данные из {source_path}")

    rows: list[dict] = []

    if not source_path.exists():
        print(f"[reader] Файл {source_path} не найден, возвращаю пустой список")
        return rows

    with source_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:

            rows.append(
                {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "amount": int(row["amount"]),
                }
            )

    print(f"[reader] Прочитано строк (без заголовка): {len(rows)}")
    return rows
