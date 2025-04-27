# Big Data Management for Data Science - Lab 01

This project is a hands-on exploration of **graph databases** using **Neo4j**.  
It focuses on modeling, loading, evolving, and querying large-scale research article data, inspired by the DBLP dataset.  
The main objectives are:

- **Modeling** research papers, authors, conferences, journals, keywords, and reviews as a **property graph**.
- **Loading** real-world or synthetic data into Neo4j using Cypher and bulk loading techniques.
- **Evolving** the database model by introducing changes such as reviewer feedback and author affiliations.
- **Querying** the graph using Cypher queries to extract insights like citation counts, author communities, h-indexes, and impact factors.
- **Applying Graph Algorithms** (PageRank, Community Detection, etc.) using the Neo4j Graph Data Science library to analyze graph structures.

The project emphasizes clean data modeling, scalable graph instantiation, and meaningful domain-specific graph analysis.


## Table of Contents
- [Environment Setup with uv](#environment-setup-with-uv)
- [DBLP Raw Data Transformation](#dblp-raw-data-transformation)
- [Database Creation](#final-database-creation)



## Environment handling with [uv](https://docs.astral.sh/uv/)

 `uv` is a new ultra-fast Python package and virtual environment manager from Astral.


0. [Install `uv` (macOS/Linux)](https://docs.astral.sh/uv/getting-started/installation)

    ```bash
    brew install uv
    ```
    After installing, confirm it works:

    ```bash
    uv --version
    ```


1.  Initiate the uv project (only at the start of the project) or sync it:
    - If there is no `pyproject.toml` and `uv.lock`, you should start a new environment:

        `uv` replaces both `virtualenv` and `pip`. To create and manage an environment:

        ```bash
        uv init
        ```

        To activate it:

        ```bash
        source .venv/bin/activate
        ```
    
    - If uv project is already created:

        ```bash
        uv sync
        ```
        This command will create a `.venv` and install all required dependencies shown in `pyproject.toml`



2. To install new dependencies or packages:

    ```bash
    uv add <package-name>==<version>
    ```
    This command will automatically add the new requirement into `pyproject.toml` and `uv.lock` and sync your dependencies (install it).

3. Remove packages

    ```bash
    uv remove <package-name>
    ```
    This command will automatically remove the requirement from `pyproject.toml` and `uv.lock` and sync your dependencies (uninstall it).



## DBLP Raw data transformation creation and loading
0. At the same level of this repository, create a folder called `data`. Inside `data`, create another folder called `files`.
1. From [DBLP website](https://dblp.uni-trier.de/), download the XML raw [data](https://dblp.uni-trier.de/xml/) in `data` folder. Only the files `dblp.dtd` and `dblp.xml.gz`.
2. Extract `dblp.xml` file from `dblp.xml.gz`.
3. Clone this [repository](https://github.com/ThomHurks/dblp-to-csv) and execute the following command from the terminal to convert the `.xml` into `.csv` format to then preprocess:

```bash
python dblp-to-csv/XMLToCSV.py --annotate --neo4j dblp.xml dblp.dtd files/dblp.csv --relations author:authored_by journal:published_in
```

## Database Creation
To create and load the final database:

1. Make sure the environment is activated (source .venv/bin/activate).
2. For creating the final databse, execute and follow the instructions inside `main.ipynb`.
