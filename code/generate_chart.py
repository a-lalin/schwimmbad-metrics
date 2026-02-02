# Import necessary libraries
import os
import json
from datetime import datetime, timedelta
import argparse

def generate_chart(output_dir=None):
    """Generate a Mermaid chart showing the last hour's data"""
    
    # Get current time
    now = datetime.now()
    
    # Calculate previous hour
    previous_hour = now - timedelta(hours=1)
    
    # Get the project root directory (one level up from code folder)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    
    # Create paths for previous hour's data in parallel logs folder
    log_dir = os.path.join(parent_dir, "logs", previous_hour.strftime('%Y-%m-%d'))
    log_file = os.path.join(log_dir, f"{previous_hour.hour:02d}-00.json")
    
    # Initialize data structures
    timestamps = []
    people_counts = []
    
    # Try to read the previous hour's data
    if os.path.exists(log_file):
        try:
            with open(log_file, 'r') as f:
                data = json.load(f)
            
            # Sort data by timestamp to ensure correct order
            data.sort(key=lambda x: x['timestamp'])
            
            # Extract timestamps and values
            for entry in data:
                # Parse timestamp and format as HH:MM
                timestamp = datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:00')
                timestamps.append(timestamp.strftime('%H:%M'))
                people_counts.append(entry['people_amount'])
                
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error reading data file: {e}")
            # If there's an error, fall back to single zero
            timestamps = ["00:00"]
            people_counts = [0]
    
    # If no data was found, use single zero
    if not timestamps:
        timestamps = ["00:00"]
        people_counts = [0]
    
    # Use provided output_dir or default to parallel graphs folder
    if output_dir is None:
        output_dir = os.path.join(parent_dir, "graphs")
    elif not os.path.isabs(output_dir):
        # If relative path provided, make it relative to project root
        output_dir = os.path.join(parent_dir, output_dir)
    
    # Create graphs directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Create the Mermaid chart
    mermaid_content = f'''```mermaid
---
config: 
  xyChart: 
    width: 900 
    height: 600 
    showDataLabel: true
    showTitle: false
  themeVariables: 
    xyChart:
      backgroundColor: "#999999"
      titleColor: "#ff0000"
      xAxisLineColor: "#ff0000"
      yAxisLineColor: "#ff0000"
---
xychart-beta
  title "Stadthallenbad"
  x-axis {json.dumps(timestamps)}
  y-axis "People"
  line {json.dumps(people_counts)}
```'''
    
    # Write to file
    output_file = os.path.join(output_dir, "metric_last_hour.md")
    with open(output_file, 'w') as f:
        f.write(mermaid_content)
    
    print(f"Chart generated: {output_file}")
    print(f"Output directory: {os.path.abspath(output_dir)}")
    print(f"Data points: {len(timestamps)}")
    
    # Print preview
    if timestamps != ["00:00"] or people_counts != [0]:
        print(f"Time range: {timestamps[0]} - {timestamps[-1]}")
        print(f"People range: {min(people_counts) if people_counts else 0} - {max(people_counts) if people_counts else 0}")
    else:
        print("No data available for the previous hour - using single zero point")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Mermaid chart from data")
    parser.add_argument("--output-dir", "-o", help="Output directory for the graph")
    args = parser.parse_args()
    
    generate_chart(args.output_dir)