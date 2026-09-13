import json
from pathlib import Path

import requests


START_DATE = "01/01/2023"
END_DATE = "13/09/2026"

BASE_URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs"

SERIES = {
    "selic_meta": 432,
    "usd_brl": 10813,
}

OUTPUT_DIR = Path("data/bronze/bcb")


def fetch_series(series_id):
    url = f"{BASE_URL}.{series_id}/dados"

    params = {
        "formato": "json",
        "dataInicial": START_DATE,
        "dataFinal": END_DATE,
    }

    response = requests.get(
        url,
        params=params,
        timeout=30,
    )

    response.raise_for_status()

    return response.json()


def save_series(name, data):
    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_path = OUTPUT_DIR / f"{name}.json"

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=2,
        )

    print(f"Saved: {output_path}")
    print(f"Rows: {len(data)}")


def main():
    print("Fetching BCB data...")

    for name, series_id in SERIES.items():
        data = fetch_series(series_id)
        save_series(name, data)


if __name__ == "__main__":
    main()
