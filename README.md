# Internet Package Management API

A REST API built with **Flask** and **SQLite** to manage internet package records.

## Features

* Add Package
* View All Packages
* Update Package
* Delete Package

## Technologies Used

* Python 3
* Flask
* SQLite3

## Project Structure

```text
internet-package-api/
│
├── app.py
├── internet.db
├── README.md
└── requirements.txt
```

## Installation

Install Flask:

```bash
pip install flask
```

Run the project:

```bash
python app.py
```

Server:

```text
http://127.0.0.1:5000
```

## Database Schema

```sql
CREATE TABLE packages(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    package_name TEXT,
    price REAL
);
```

## API Endpoints

| Method | Endpoint         |
| ------ | ---------------- |
| POST   | `/packages`      |
| GET    | `/packages`      |
| PUT    | `/packages/<id>` |
| DELETE | `/packages/<id>` |

## Sample Request

```json
{
    "customer_name": "Maheen",
    "package_name": "Super 40 Mbps",
    "price": 2500
}
```

## Requirements

```text
Flask==3.1.0
```
