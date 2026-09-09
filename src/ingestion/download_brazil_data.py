from pathlib import Path
from urllib.request import urlretrieve


SOURCE_URL = (
    "https://www.gov.br/receitafederal/pt-br/assuntos/"
    "orientacao-tributaria/declaracoes-e-demonstrativos/"
    "criptoativos/arquivos/"
    "criptoativos_dados_abertos_20260826.xls"
)

OUTPUT_PATH = Path(
    "data/bronze/criptoativos_dados_abertos_20260826.xls"
)


def download_file():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    print("Downloading Receita Federal dataset...")
    urlretrieve(SOURCE_URL, OUTPUT_PATH)

    print(f"Saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    download_file()
