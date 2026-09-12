import pandas as pd
from pathlib import Path


BRONZE_PATH = Path(
    "data/bronze/criptoativos_dados_abertos_20260826.xls"
)

SILVER_PATH = Path(
    "data/silver/receita_stablecoin_activity.csv"
)

MONTHS = {
    "Janeiro": 1,
    "Fevereiro": 2,
    "Março": 3,
    "Abril": 4,
    "Maio": 5,
    "Junho": 6,
    "Julho": 7,
    "Agosto": 8,
    "Setembro": 9,
    "Outubro": 10,
    "Novembro": 11,
    "Dezembro": 12,
}


def load_data():
    return pd.read_excel(
        BRONZE_PATH,
        sheet_name="Relatorio4",
        header=14,
    )


def parse_month(value):
    month_name, year = value.split(" de ")
    month = MONTHS[month_name]

    return pd.Timestamp(
        year=int(year),
        month=month,
        day=1,
    )


def transform_data(df):
    transformed = df.rename(
        columns={
            "CRIPTOATIVO": "asset",
            "MÊS/ANO": "month",
            "Nº DE OPERAÇÕES": "operation_count",
            "VALOR TOTAL DAS OPERAÇÕES": "total_value_brl",
            "VALOR MÉDIO POR OPERAÇÃO": "average_value_brl",
        }
    )

    transformed["month"] = transformed["month"].map(parse_month)

    transformed["operation_count"] = (
        transformed["operation_count"].astype(int)
    )

    transformed["total_value_brl"] = (
        transformed["total_value_brl"].astype(float)
    )

    transformed["average_value_brl"] = (
        transformed["average_value_brl"].astype(float)
    )

    return transformed[
        [
            "asset",
            "month",
            "operation_count",
            "total_value_brl",
            "average_value_brl",
        ]
    ]


def save_data(df):
    SILVER_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_csv(
        SILVER_PATH,
        index=False,
    )

    print(f"Saved to: {SILVER_PATH}")
    print(f"Rows: {len(df)}")


def main():
    print("Transforming Receita Federal data...")

    bronze = load_data()
    silver = transform_data(bronze)

    save_data(silver)


if __name__ == "__main__":
    main()
