# ETL Sell Project

This project aims to build a complete ETL (Extract, Transform, Load) pipeline in Python to process and analyze sales data from multiple CSV files, simulating different sources (e.g., different stores). The processed data is then loaded into a SQLite database.

## Project Structure

- `data/` — Input CSV files (simulating different sources)
- `database/` — Generated SQLite database
- `documents/` — CSV files generated during the process
- `etl/` — ETL logic modules
  - `extract.py`
  - `transform.py`
  - `load.py`
- `main.py` — Main script to run the ETL pipeline
- `requirements.txt` — Project dependencies
- `README.md` — This file

## Technologies Used

- Python 3.10+
- pandas
- sqlite3
- virtualenv (recommended)

## ETL Steps

### 1. Extraction

Reads all CSV files from the `data/` folder and concatenates them into a single pandas DataFrame.

### 2. Transformation

- Converts the `Data da Venda` column to datetime format.
- Calculates a new column `Total da Venda` by multiplying `Quantidade Vendida` and `Valor Unitário`.
- Cleans the data by removing rows with missing or invalid values.

### 3. Loading

Inserts the transformed data into the `sells` table inside the SQLite database (`database/sells.db`). The table is created automatically if it does not exist.

## How to Run

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/etl-sell.git
    cd etl-sell
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # Linux/macOS
    .venv\Scripts\activate     # Windows
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Place your CSV files inside the `data/` folder.

5. Run the ETL pipeline:

    ```bash
    python main.py
    ```

## Outputs

- Raw and transformed CSV files saved in the `documents/` folder:
  - `all_data.csv`
  - `transformed_data.csv`
- SQLite database file `database/sells.db` containing the cleaned and consolidated sales data in the `vendas` table.

## Future Improvements

- Add more robust data validation and error handling.
- Create automated unit and integration tests.
- Support other data formats or live data sources (APIs, JSON).
- Build a dashboard or interface for visualization and reporting.
