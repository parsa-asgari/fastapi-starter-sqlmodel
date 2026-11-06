# FastAPI Starter + SQLModel

1. To setup the project

   ```bash
   python3 -m venv venv
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

2. To setup Postgresql

   ```bash
   sudo apt install postgresql-16
   ```
3. To configure Postgres:
   ```bash
   sudo su postgres
   psql
   CREATE DATABASE mydb;
   ALTER ROLE postgres WITH PASSWORD 'postgres';
   ```
4. Run the project with:
   ```bash
   fastapi run main.py  --reload
   ```
   
