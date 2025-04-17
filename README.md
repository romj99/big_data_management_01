# Big Data Management for Data Science - Lab 01

## Environment handling with [uv](https://docs.astral.sh/uv/)

 `uv` is a new ultra-fast Python package and virtual environment manager from Astral.


### 1. [Install `uv` (macOS/Linux)](https://docs.astral.sh/uv/getting-started/installation)
```bash
pip install uv
```
or
```bash
brew install uv
```
After installing, confirm it works:

```bash
uv --version
```


### 2.  Create a virtual environment

`uv` replaces both `virtualenv` and `pip`. To create and manage an environment:

```bash
uv venv
```

This creates a `.venv/` folder in your current directory (like `python -m venv .venv` would do), but much faster.

To activate it:

```bash
source .venv/bin/activate
```


### 3. Install packages and dependencies

You can install packages with `uv` manually the same way you would with pip:

```bash
uv pip install fastapi uvicorn
```

Or even faster:

```bash
uv pip install -r requirements.txt
```

### 4. Check installed pacjages

```bash
uv pip list
```

### 5. Uninstall packages

```bash
uv pip uninstall fastapi
```

### 6. Upgrade packages

```bash
uv pip install --upgrade fastapi
```

---

## DBLP Data downloading

1. From [DBLP website](https://dblp.uni-trier.de/), download the XML raw [data](https://dblp.uni-trier.de/xml/). Mainly, the files `dblp.dtd` and `dblp.xml.gz`.
2. Extract `dblp.xml` file from `dblp.xml.gz`.
3. Clone this [repository](https://github.com/ThomHurks/dblp-to-csv) and execute the following command from the terminal to convert the `.xml` into `.csv` format to then preprocess:

```bash
python dblp-to-csv/XMLToCSV.py --annotate --neo4j dblp.xml dblp.dtd data/dblp.csv --relations author:authored_by journal:published_in
```
