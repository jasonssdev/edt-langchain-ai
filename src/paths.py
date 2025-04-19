from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Directories root
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
DB_DIR = DATA_DIR / "db"

# Specific files root
FILE_PDF_PATH = RAW_DIR / "file.pdf"
PRODUCTS_PDF_PATH = RAW_DIR / "products.pdf"
PRODUCTS_CSV_PATH = RAW_DIR / "products.csv"
PROJECT_TXT_PATH = RAW_DIR / "project.txt"
CONSULTORIO_PDF_PATH = RAW_DIR / "consultorio.pdf"
CHROMA_DB_PATH = DB_DIR / "chroma.db"