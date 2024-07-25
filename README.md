# Airline Sentiment ETL Project

This project demonstrates an ETL (Extract, Transform, Load) process for airline sentiment data using PostgreSQL databases running in Docker containers, with data processing in Jupyter Notebooks and schema design using SQLAlchemy.

## Project Overview

- **Extract**: Data is sourced from a PostgreSQL database running in a Docker container.
- **Transform**: Data processing and analysis are performed in a Jupyter Notebook.
- **Load**: Processed data is loaded into a separate PostgreSQL data warehouse, also running in a Docker container.

## Prerequisites

- Docker and Docker Compose
- Python 3.7+
- Jupyter Notebook
- DBeaver (or any other PostgreSQL client)

## Setup

1. **Clone this repository**:

    ```sh
    git clone https://github.com/im-brahim/ETL-Sentiment.git
    cd ETL-Sentiment
    ```

2. **Create a virtual environment**:

    ```sh
    python -m venv airline_sentiment_env
    source airline_sentiment_env/bin/activate  # On Windows use `airline_sentiment_env\Scripts\activate`
    ```

3. **Install the required Python packages**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Docker containers**:

    Ensure Docker and Docker Compose are installed on your system. Then, start the containers:

    ```sh
    docker-compose up -d
    ```

4. **Connect to the PostgreSQL database using DBeaver**:

    - Download and install [DBeaver](https://dbeaver.io/).
    - Open DBeaver and create a new database connection.
    
    - Use the following connection details For Database:
      - **Host**: `localhost`
      - **Port**: `5432`
      - **Database**: `airline_sentiment_db`
      - **Username**: `dbuser`
      - **Password**: `db`

    - Use the following connection details For DW:
      - **Host**: `localhost`
      - **Port**: `5433`
      - **Database**: `airline_sentiment_dw`
      - **Username**: `dwuser`
      - **Password**: `dw`

5. **Run data processing in Jupyter Notebook**:

    - Start Jupyter Notebook:

      ```sh
      jupyter notebook
      ```

    - Open the notebook file in your browser and run the cells to process and analyze the data.

## Contributing

Feel free to submit issues or pull requests if you have any improvements or bug fixes.


## Acknowledgments

This project was completed in two days with the help of AI cloude and ChatGPT :).