# 🧠 EDT LangChain AI

This project is a modular LangChain-based application that reads documents (PDFs), splits them into chunks, and stores their embeddings in a Chroma vector database. It also prepares the setup for interacting with OpenAI APIs using structured prompts and agents.

---

## 🚀 Features

- ✅ Loads and processes PDF documents
- ✅ Splits text using `TokenTextSplitter` or other strategies
- ✅ Stores embeddings in ChromaDB
- ✅ Modular structure with centralized path and configuration management
- ✅ Uses `langchain`, `langchain-openai`, and `langchain-chroma`
- ✅ Ready for LangGraph integration

---

## 🧱 Project Structure

```
edt-langchain-ai/
├── data/                    # Raw data and vector storage
│   └── db/                 # Chroma persistent storage
│   └── raw/                # Input PDFs
├── notebooks/              # (Optional) Jupyter notebooks for exploration
├── src/                    # Source code
│   ├── config.py           # App configuration and settings
│   ├── paths.py            # Centralized file path management
│   ├── main.py             # Main application entrypoint
│   ├── chromadb_manager.py # Chroma vectorstore wrapper
│   └── building_process/   # (Optional) Preprocessing or setup scripts
├── .env.example            # Example environment variables
├── environment.yml         # Conda environment definition
├── pyproject.toml          # Project metadata for pip install -e .
└── README.md               # You're here!
```

---

## 🛠️ Setup

### 1. Clone the repo

```bash
git clone git@github.com:jasonssdev/edt-langchain-ai.git
cd edt-langchain-ai
```

### 2. Create and activate environment

```bash
conda env create -f environment.yml
conda activate ai-py3.12
```

### 3. Install in editable mode

```bash
pip install -e .
```

---

## 📄 Usage

Run the app from the project root:

```bash
python -m src.main
```

Or use VS Code with the preconfigured `launch.json` (`F5` to run with debugger).

---

## 🔪 Notes

- The database in `data/db/chroma.db/` is **not tracked** in Git. It is generated when the app runs.
- Add your PDFs to `data/raw/` and set the desired path in `paths.py`.

---

## 📦 Dependencies

- [LangChain](https://www.langchain.com/)
- [OpenAI](https://platform.openai.com/)
- [ChromaDB](https://docs.trychroma.com/)
- [LangChain Chroma](https://python.langchain.com/docs/integrations/vectorstores/chroma)

---

## 🧑‍💻 Author

Made with ❤️ by [@jasonssdev](https://github.com/jasonssdev)

---

## 📄 License

[Apache 2.0](./LICENSE)

