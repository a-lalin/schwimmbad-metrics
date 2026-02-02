import requests
import os
from datetime import datetime

# ===== CONFIGURATION =====
# 1. Create these secrets in your GitHub repository settings
CLIENT_ID = os.environ.get('TWITCH_CLIENT_ID')
ACCESS_TOKEN = os.environ.get('TWITCH_ACCESS_TOKEN')
CHANNEL_NAME = "wienersportstaetten"

# 2. The file where logs will be saved (in the repository)
LOG_FILE = "stream_log.txt"

def check_stream():
    """Checks if the Twitch channel is live and returns status."""
    headers = {
        'Client-ID': CLIENT_ID,
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }
    
    try:
        # Get stream information from Twitch API
        url = f'https://api.twitch.tv/helix/streams?user_login={CHANNEL_NAME}'
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raises an error for bad status codes (4xx or 5xx)
        data = response.json()
        
        is_live = len(data['data']) > 0
        
        if is_live:
            stream_data = data['data'][0]
            status = f"LIVE - Title: {stream_data['title']}, Viewers: {stream_data['viewer_count']}, Started at: {stream_data['started_at']}"
        else:
            status = "OFFLINE"
            
        return True, status  # Success, status message
        
    except requests.exceptions.RequestException as e:
        # Handle network or API errors
        return False, f"API ERROR: {str(e)}"

def main():
    # Create timestamp for this check
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Check stream status
    success, status_message = check_stream()
    
    # Format log entry
    if success:
        log_entry = f"[{timestamp}] {status_message}\n"
    else:
        log_entry = f"[{timestamp}] ERROR - {status_message}\n"
    
    # Append result to log file
    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)
    
    # Also print to console (visible in GitHub Actions log)
    print(log_entry.strip())

if __name__ == "__main__":
    main()