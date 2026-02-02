# Import necessary libraries
import os           # For file and directory operations
import json         # For JSON file reading/writing
import random       # For generating random numbers
import sys          # For exit codes
from datetime import datetime as dt  # For getting current date/time

def collect_data():
    """Simulate data collection by returning a random number between 0 and 100"""
    return random.randint(0, 100)

def main():
    """Main function that adds current minute's data to JSON file"""
    
    # Get current date and time
    now = dt.now()
    
    # Create directory path using YYYY-MM-DD format
    log_dir = f"logs/{now.strftime('%Y-%m-%d')}"
    
    # Create file path using current hour: HH-00.json
    log_file = f"{log_dir}/{now.hour:02d}-00.json"
    
    # Create timestamp for current minute (seconds always set to 00)
    timestamp = now.strftime('%Y-%m-%d %H:%M:00')
    
    # Create directory if it doesn't exist (exist_ok=True prevents errors if it already exists)
    os.makedirs(log_dir, exist_ok=True)
    
    # Try to read existing data from the JSON file
    try:
        # Open the file for reading
        with open(log_file, 'r') as f:
            # Load JSON data into a Python list
            data = json.load(f)
    except FileNotFoundError:
        # If file doesn't exist, start with an empty list
        data = []
    except json.JSONDecodeError:
        # If file is corrupted, start with an empty list
        data = []
    
    # Check if current minute's data already exists in the file
    # 'any' function returns True if ANY entry has the current timestamp
    if not any(entry.get('timestamp') == timestamp for entry in data):
        # If current minute doesn't exist, add new entry
        collect_num = collect_data()
        data.append({
            'timestamp': timestamp,          # Current minute's timestamp
            'people_amount': collect_num      # Random number between 0-100
        })
        
        # Write the updated data back to the JSON file
        with open(log_file, 'w') as f:
            # 'indent=2' makes the JSON file human-readable with proper formatting
            json.dump(data, f, indent=2)
        
        print(f"Added entry: {timestamp} ")
        print(f"People amount: {collect_num}")
        print(f"File: {log_file}")
        return True  # Return True to indicate changes were made
    
    # If we get here, the entry already existed
    print(f"Entry for {timestamp} already exists, action cancelled...")
    return False  # Return False to indicate no changes

if __name__ == "__main__":
    # Run main function and exit with appropriate code
    # Exit code 0: Changes were made (success)
    # Exit code 1: No changes made (also success, but different)
    changes_made = main()
    sys.exit(0 if changes_made else 1)