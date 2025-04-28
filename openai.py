import undetected_chromedriver as uc

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tempfile
import random
class OpenaiDriver:
    def __init__(self):
        self.driver = self.open_chrome()
        self.driver.get("https://www.chatgpt.com")
    def open_chrome(self):
        # Set up Chrome options
        chrome_options = uc.ChromeOptions() 

        # Appearance
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")

        # Stealth
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-default-apps") 
        # Run Chrome in headless mode 

        # Use a custom user-agent
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                                    "Chrome/119.0.0.0 Safari/537.36")

        # Load Chrome with a user profile (to open with an account)
        # Replace below path with your actual user profile path
        temp_profile_dir = tempfile.mkdtemp()
        chrome_options.add_argument(f"--user-data-dir={temp_profile_dir}")
        chrome_options.add_argument(r"--profile-directory=Default")
        chrome_options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Path to Chrome binary
        # Set up the Chrome WebDriver
        driver = uc.Chrome( options=chrome_options,version_main=135)
        return driver
    def query_openai(self, query): 
        driver = self.driver 
        time.sleep(random.uniform(0.5, 1.5))  # Random sleep between 0.5 and 1.5 seconds
        try:
            # Locate the div with id "prompt-text-area" and click on the p tag inside it

            
            # Wait until the element with id 'prompt-text-area' is present
            div_element = WebDriverWait(driver, 100).until(
                EC.presence_of_element_located((By.ID, "prompt-textarea"))
            )
            time.sleep(random.uniform(0.5, 1.5))  # Random sleep between 0.5 and 1.5 seconds
            p_tag = div_element.find_element("tag name", "p")
            p_tag.click()
            p_tag.send_keys(query)
            # Locate the button with id "composer-submit-button" and click it
            submit_button = WebDriverWait(driver, 100).until(
                EC.element_to_be_clickable((By.ID, "composer-submit-button"))
            )
            submit_button.click()
            # time.sleep(random.uniform(7.5, 10))  # Random sleep between 0.5 and 1.5 seconds
            h6_elements = driver.find_elements(By.CSS_SELECTOR, "h6.sr-only")
 
            last_h6 = h6_elements[-1]

            # 3. Find its next sibling using JavaScript
            
            while True:
                next_sibling_text = driver.execute_script(
                    "return arguments[0].nextElementSibling ? arguments[0].nextElementSibling.textContent : null;",
                    last_h6
                )
                if next_sibling_text:
                    break
            return next_sibling_text
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

if __name__ == "__main__":
    openai_driver = OpenaiDriver()
    queries = [ 
        "Explain the theory of relativity.",
        "What are the benefits of exercise?",
        "How does photosynthesis work?",
        "What is the meaning of life?",
        "Tell me a joke.",
        "What is the weather like today?",
        "Who won the last World Series?",
        "What is the largest mammal on Earth?",
        "How do you make a cake?"
    ]
    for query in queries:
        response = openai_driver.query_openai(query)
        if response:
            print(f"Query: {query}\nResponse: {response}\n")
        else:
            print(f"Failed to get a response for query: {query}")
    openai_driver.driver.quit()