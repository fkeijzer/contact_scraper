from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config import *
import time

class BundelingScraperSession:
    def __init__(self):
        # Setup Chrome options
        chrome_options = Options()
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # Use your regular Chrome profile
        chrome_options.add_argument('--user-data-dir=/Users/flipkeijzer/Library/Application Support/Google/Chrome')
        chrome_options.add_argument('--profile-directory=Default')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-popup-blocking')
        
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        self.wait = WebDriverWait(self.driver, 20)  # 20 seconds timeout

    def wait_and_find_element(self, by, value):
        """Helper method to wait for and find an element"""
        element = self.wait.until(
            EC.presence_of_element_located((by, value))
        )
        self.wait.until(
            EC.element_to_be_clickable((by, value))
        )
        return element

    def login(self):
        try:
            print("Opening login page...")
            self.driver.get(LOGIN_URL)
            
            # Wait for manual login
            print("\nPlease log in manually:")
            print("1. Select the correct client")
            print("2. Enter your username and password")
            print("3. Click the login button")
            print("4. Wait until you reach the dashboard")
            print("\nPress Enter when you're logged in and ready to continue...")
            input()
            
            # Verify we're on the dashboard
            try:
                dashboard_element = self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.dashboard'))
                )
                print("✅ Successfully reached dashboard!")
                return True
            except Exception as e:
                print(f"❌ Could not verify dashboard. Error: {str(e)}")
                self.driver.save_screenshot("dashboard_error.png")
                print("Screenshot saved as dashboard_error.png")
                return False

        except Exception as e:
            print(f"❌ Error during login: {str(e)}")
            return False

    def scrape_users(self):
        """Scrape user information from the dashboard"""
        try:
            print("\nStarting to scrape users...")
            # Here we'll add the scraping logic
            print("Scraping functionality to be implemented...")
            return True
        except Exception as e:
            print(f"❌ Error during scraping: {str(e)}")
            self.driver.save_screenshot("scraping_error.png")
            print("Screenshot saved as scraping_error.png")
            return False

    def close(self):
        """Clean up the browser"""
        if self.driver:
            self.driver.quit()

def main():
    scraper = BundelingScraperSession()
    try:
        if scraper.login():
            print("Login successful! Starting scraping process...")
            if scraper.scrape_users():
                print("✅ Scraping completed successfully!")
            else:
                print("❌ Scraping failed!")
        else:
            print("❌ Login failed!")
    finally:
        input("\nPress Enter to close the browser...")
        scraper.close()

if __name__ == "__main__":
    main()
