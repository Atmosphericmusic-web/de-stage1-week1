from pathlib import Path
import sqlite3
def write_data(rows: list[dict], db_path: Path) -> None:
    print(f"[writer] Пишу {len(rows)} строк(и) в базу {db_path}")
    if not rows:
        print("[writer] Нет данных для записи, выхожу")
        return
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    try:
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                amount INTEGER NOT NULL,
                amount_double INTEGER NOT NULL
            )
            """
        )
        cur.executemany(
            """
            INSERT OR REPLACE INTO sales (id, name, amount, amount_double)
            VALUES (:id, :name, :amount, :amount_double)
            """,
            rows,
        )
        conn.commit()
        print("[writer] Запись завершена, commit выполнен.")
    finally:
        conn.close()
        print("[writer] Соединение с базой закрыто.")
