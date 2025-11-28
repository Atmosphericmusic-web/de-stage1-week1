def transform_data(rows: list[dict]) -> list[dict]:
    
    print("[transform] Преобразую данные")

    transformed = []
    for row in rows:
        new_row = dict(row)
        new_row["amount_double"] = row["amount"] * 2
        transformed.append(new_row)

    print(f"[transform] Обработано строк: {len(transformed)}")
    return transformed
