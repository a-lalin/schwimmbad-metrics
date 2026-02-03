import json
import time
from datetime import datetime
import os
from PIL import Image
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_selenium():
    """Set up Selenium with headless Chrome for GitHub Actions"""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Headless for GitHub Actions
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    
    driver = webdriver.Chrome(options=options)
    return driver

def capture_and_process_number(driver, url, screenshot_path='screenshot.png'):
    """Navigate to Twitch, capture screenshot, and extract number"""
    try:
        # Navigate to Twitch stream
        driver.get(url)
        
        # Wait for page to load (adjust wait time as needed)
        time.sleep(15)  # Twitch streams need time to load
        
        # Take screenshot
        driver.save_screenshot(screenshot_path)
        
        # Crop to the area where the number is likely to be
        # You'll need to adjust these coordinates based on your specific stream
        img = Image.open(screenshot_path)
        
        # Coordinates for cropping (adjust based on your screenshot)
        # These are example coordinates - you'll need to find the exact ones
        left = 900   # X-coordinate of left side
        top = 400    # Y-coordinate of top side
        right = 1000 # X-coordinate of right side
        bottom = 500 # Y-coordinate of bottom side
        
        cropped_img = img.crop((left, top, right, bottom))
        
        # Preprocess image for better OCR
        # Convert to grayscale and enhance contrast
        gray_img = cropped_img.convert('L')
        
        # Save cropped image for debugging
        gray_img.save('cropped_number.png')
        
        # Use Tesseract OCR to extract text
        # Configure Tesseract for digits only
        custom_config = r'--oem 3 --psm 6 outputbase digits'
        extracted_text = pytesseract.image_to_string(gray_img, config=custom_config)
        
        # Clean extracted text to get just the number
        numbers = ''.join(filter(str.isdigit, extracted_text))
        
        return numbers if numbers else None
        
    except Exception as e:
        print(f"Error capturing number: {e}")
        return None

def save_to_json(number, filename='chart_data.json'):
    """Save number with timestamp to JSON file"""
    data = {
        'timestamp': datetime.now().isoformat(),
        'value': int(number) if number and number.isdigit() else None
    }
    
    # Load existing data if file exists
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            existing_data = json.load(f)
    else:
        existing_data = []
    
    # Append new data
    if isinstance(existing_data, list):
        existing_data.append(data)
    else:
        existing_data = [existing_data, data]
    
    # Save to file
    with open(filename, 'w') as f:
        json.dump(existing_data, f, indent=2)
    
    return data

def main():
    twitch_url = "https://www.twitch.tv/wienersportstaetten"
    
    # Setup Selenium
    driver = setup_selenium()
    
    try:
        # Capture and process the number
        number = capture_and_process_number(driver, twitch_url)
        
        if number:
            print(f"Extracted number: {number}")
            
            # Save to JSON
            saved_data = save_to_json(number)
            print(f"Saved data: {saved_data}")
        else:
            print("Could not extract number")
            
    finally:
        driver.quit()

if __name__ == "__main__":
    main()