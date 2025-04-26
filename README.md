# Big Data Management for Data Science - Lab 01

Description of the project.

\table of contents.




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



## DataBase creation and loading

- DBLP Data downloading
- Transform it
- load it
- execute queries
- caca

1. From [DBLP website](https://dblp.uni-trier.de/), download the XML raw [data](https://dblp.uni-trier.de/xml/). Mainly, the files `dblp.dtd` and `dblp.xml.gz`.
2. Extract `dblp.xml` file from `dblp.xml.gz`.
3. Clone this [repository](https://github.com/ThomHurks/dblp-to-csv) and execute the following command from the terminal to convert the `.xml` into `.csv` format to then preprocess:

```bash
python dblp-to-csv/XMLToCSV.py --annotate --neo4j dblp.xml dblp.dtd files/dblp.csv --relations author:authored_by journal:published_in
```

## DBLP Data importing into Neo4j
```bash
./cypher-shell -u neo4j -p <password>  < load_all.cypher

```
- Does the DB need to be shut down or active?
- I've created all files and move them into import/csv inside the path of the database created by neo4j
- Where do i execute that command?