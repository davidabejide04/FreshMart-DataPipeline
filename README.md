# FreshMart Data Pipeline

## Overview
This project builds a simple ETL pipeline for FreshMart:
- **Ingestion**: Load product data from CSV
- **Transformation**: Clean, compute stock value, aggregate by category
- **Storage**: Load into PostgreSQL for querying

## Files
- `/data/freshmart_products.csv` → Sample dataset
- `/notebooks/FreshMart_ETL.ipynb` → Data ingestion & transformation
- `/scripts/FreshMart_DBLoad.py` → Database schema & loading script

## Queries
- Get all Dairy products
- Get products with StockQuantity < 50
