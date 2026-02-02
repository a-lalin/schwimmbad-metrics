# generate_chart_variables.py
import os
import json
from datetime import datetime, timedelta

def create_chart_with_variables():
    """Generate chart that can use GitHub Actions variables"""
    now = datetime.now()
    data_points = []
    
    # Get data from last hour
    for i in range(60):
        check_time = now - timedelta(minutes=i)
        date_str = check_time.strftime('%Y-%m-%d')
        hour_str = f"{check_time.hour:02d}-00.json"
        log_file = f"logs/{date_str}/{hour_str}"
        
        if os.path.exists(log_file):
            try:
                with open(log_file, 'r') as f:
                    data = json.load(f)
                
                target_time = check_time.strftime('%Y-%m-%d %H:%M:00')
                for entry in data:
                    if entry.get('timestamp') == target_time:
                        data_points.append((
                            check_time.strftime('%H:%M'),
                            entry.get('random_number', 0)
                        ))
                        break
            except:
                pass
    
    # Sort by time (oldest first)
    data_points.sort(key=lambda x: x[0])
    
    # Format for GitHub Actions output
    timestamps = [f'"{t}"' for t, _ in data_points[-10:]]  # Last 10 points
    values = [v for _, v in data_points[-10:]]
    
    # Create outputs for GitHub Actions
    print(f"::set-output name=timestamps::{','.join(timestamps)}")
    print(f"::set-output name=values::{','.join(map(str, values))}")
    
    # Also write to file for reference
    chart_data = {
        "last_updated": now.isoformat(),
        "timestamps": [t.replace('"', '') for t in timestamps],
        "values": values
    }
    
    with open('chart_data.json', 'w') as f:
        json.dump(chart_data, f, indent=2)

if __name__ == "__main__":
    create_chart_with_variables()