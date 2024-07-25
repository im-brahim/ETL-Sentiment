# Airline Sentiment ETL Project

This project demonstrates an ETL (Extract, Transform, Load) process for airline sentiment data using PostgreSQL databases running in Docker containers, with data processing in Jupyter Notebooks and schema design using SQLAlchemy.

## Project Overview

- Extract: Data is sourced from a PostgreSQL database running in a Docker container.
- Transform: Data processing and analysis are performed in a Jupyter Notebook.
- Load: Processed data is loaded into a separate PostgreSQL data warehouse, also running in a Docker container.

## Prerequisites

- Docker and Docker Compose
- Python 3.7+
- Jupyter Notebook
- DBeaver (or any other PostgreSQL client)

## Setup

1. Clone this repository:

```sh
pip install -r requirements.txt

