# OOP Lab 1 — Data Processing with Classes

## Lab Overview
This lab demonstrates **Object-Oriented Programming (OOP)** principles in Python through a small data analysis project.  
You’ll learn how to design and use classes to structure your code logically and efficiently.  

The main goal of the lab is to:
- Load data from a CSV file using a reusable class.
- Represent tabular data with a class that supports filtering and aggregation.
- Practice OOP concepts such as **encapsulation**, **composition**, and **abstraction**.

---

##  Project Structure
oop_lab_1/
│
├── README.md # Project documentation (this file)
├── Cities.csv # Dataset containing city information
└── data_processing.py # Main source code for data loading and analysis


---

## Design Overview

### Class: `DataLoader`
**Purpose:**  
Handles reading CSV data files and returning their contents in a structured format (list of dictionaries).

**Attributes:**
- `base_path` — The directory path where data files are located.

**Key Methods:**
- `__init__(self, base_path=None)`  
  Initializes the data loader with a base path. If none is provided, it defaults to the current directory.
  
- `load_csv(self, filename)`  
  Opens and reads the specified CSV file, returning a list of dictionaries where each dictionary represents a row.

---

### Class: `Table`
**Purpose:**  
Encapsulates a dataset (list of dictionaries) and provides methods for filtering and aggregating data.

**Attributes:**
- `name` — Name of the table (e.g., `"cities"`).  
- `table` — The list of dictionaries containing the data.

**Key Methods:**
- `filter(self, condition)`  
  Returns a new `Table` object containing only the rows that meet a specified condition (a lambda function).

- `aggregate(self, aggregation_function, aggregation_key)`  
  Applies an aggregation function (like `sum`, `max`, or a custom lambda) to the values of a given column.

---

## How to Run and Test the Code

### Prepare the dataset
    Ensure that `Cities.csv` is in the same directory as `data_processing.py`.  

### Run code
Open a terminal or VScode in the project folder and execute:
    python data_processing.py

### Expected Output
    The script will:
    Print the average temperature of all cities.
    List all cities in Germany.
    Show cities in Spain with temperature above 12°C.
    Display the number of unique countries.
    Compute average temperature in Germany and maximum temperature in Italy.

