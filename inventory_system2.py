import json
from datetime import datetime

# Global variable
stock_data = {}

def add_item(item, qty, logs=None):
    """Adds stock for a given item, validating input."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, int) or qty <= 0:
        print(f"Warning: Attempted to add item with invalid type or quantity: item={item}, qty={qty}")
        return

    item_key = item.strip().lower()
    stock_data[item_key] = stock_data.get(item_key, 0) + qty

    logs.append(f"{datetime.now()}: Added {qty} of {item_key.capitalize()}")

def remove_item(item, qty):
    """Removes stock for a given item."""
    if not isinstance(item, str) or not isinstance(qty, int) or qty <= 0:
        print(f"Warning: Attempted to remove item with invalid type or quantity: item={item}, qty={qty}")
        return

    item_key = item.strip().lower()

    try:
        if stock_data[item_key] >= qty:
            stock_data[item_key] -= qty
            if stock_data[item_key] <= 0:
                del stock_data[item_key]
        else:
            print(f"Warning: Only {stock_data[item_key]} of {item_key.capitalize()} available, cannot remove {qty}.")
    except KeyError:
        print(f"Warning: Cannot remove {item_key.capitalize()}, item is not in stock.")

def get_qty(item):
    """Returns the quantity of an item."""
    if not isinstance(item, str):
        return 0
    return stock_data.get(item.strip().lower(), 0)

def load_data(file="inventory.json"):
    """Loads inventory data from a JSON file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.loads(f.read())
        print(f"Data loaded successfully from {file}.")
    except FileNotFoundError:
        print(f"Warning: File {file} not found. Starting with empty inventory.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {file}. File might be corrupted.")

def save_data(file="inventory.json"):
    """Saves current inventory data to a JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            f.write(json.dumps(stock_data, indent=4))
        print(f"Data saved successfully to {file}.")
    except Exception as e:
        print(f"Critical Error: Could not save data: {e}")

def print_data():
    """Prints a report of all items and their quantities."""
    print("\n--- Items Report ---")
    if not stock_data:
        print("Inventory is empty.")
    for item, qty in stock_data.items():
        print(f"{item.capitalize():<10} -> {qty}")
    print("--------------------")

def check_low_items(threshold=5):
    """Returns a list of items below the stock threshold."""
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i.capitalize())
    return result

def main():
    run_logs = []

    add_item("apple", 10, run_logs)
    add_item("banana", 7, run_logs)
    add_item("carrot", 4, run_logs)

    add_item(123, 10, run_logs)
    add_item("orange", 0, run_logs)
    add_item("banana", -2, run_logs)

    remove_item("apple", 3)
    remove_item("orange", 1)

    print(f"\nApple stock: {get_qty('apple')}")
    print(f"Carrot stock: {get_qty('carrot')}")
    print(f"Low items (threshold 5): {check_low_items(5)}")

    save_data()
    
    load_data() 
    
    print_data()

    print("\n--- Run Logs ---")
    for log in run_logs:
        print(log)
    print("----------------")

if __name__ == "__main__":
    main()
