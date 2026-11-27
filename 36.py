import csv
from pathlib import Path

# 1. pathlib.Path: Modern file and directory operations
base_dir = Path(".")
current_file = Path("36.py")
print("File name:", current_file.name)
print("File suffix:", current_file.suffix)
print("File stem:", current_file.stem)
print("Absolute path:", current_file.resolve())

print()

# 2. csv.DictWriter: Export structured data to CSV
csv_file = Path("sample_products.csv")
products = [
    {"id": 1, "title": "Wireless Mouse", "price": 499.0, "in_stock": True},
    {"id": 2, "title": "Mechanical Keyboard", "price": 2499.0, "in_stock": True},
    {"id": 3, "title": "USB-C Hub", "price": 1299.0, "in_stock": False},
]

with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
    fieldnames = ["id", "title", "price", "in_stock"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(products)

print(f"Created {csv_file} successfully.")

print()

# 3. csv.DictReader: Read and process CSV rows
print("Reading back products from CSV:")
with open(csv_file, mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        stock_status = "Available" if row["in_stock"] == "True" else "Out of stock"
        print(f"  #{row['id']} {row['title']} - Rs.{float(row['price']):.2f} [{stock_status}]")

# Cleanup sample CSV file
if csv_file.exists():
    csv_file.unlink()
    print("\nTemporary CSV file cleaned up.")
