"""
pip install selenium chromedriver-autoinstaller html2text

Install Chrome (if not already installed)

Linux Installation:

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt --fix-broken install
google-chrome-stable --version

"""



import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import html2text

def fetch_html_with_browser(url):
    """Fetch HTML content using a headless browser."""
    # Ensure chromedriver is installed
    chromedriver_autoinstaller.install()

    # Set up Chrome options for headless browsing
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no UI)
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    
    # Initialize WebDriver (Chrome)
    driver = webdriver.Chrome(options=chrome_options)
    
    # Fetch the URL and wait for content to load
    driver.get(url)
    
    # Wait for JavaScript to render
    time.sleep(3)  # Adjust if necessary
    
    # Get the page HTML after JavaScript has been rendered
    html_content = driver.page_source
    
    # Close the browser
    driver.quit()
    
    return html_content

def convert_html_to_markdown(html_content):
    """Convert the HTML content to Markdown."""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    markdown_content = h.handle(html_content)
    return markdown_content

def save_markdown_to_file(markdown_content, filename="output.md"):
    """Save the markdown content to a .md file."""
    with open(filename, 'w', encoding='utf-8') as md_file:
        md_file.write(markdown_content)
    print(f"Markdown file saved as {filename}")

def main(url):
    """Main function to execute the script."""
    try:
        # Step 1: Fetch HTML content from the shared link using the browser
        html_content = fetch_html_with_browser(url)
        
        # Step 2: Convert HTML content to Markdown
        markdown_content = convert_html_to_markdown(html_content)
        
        # Step 3: Save the converted Markdown to a file
        save_markdown_to_file(markdown_content)
    
    except Exception as e:
        print(f"Error: {e}")

# Example usage: Pass the shared ChatGPT link here
if __name__ == "__main__":
    shared_link = input("Enter the ChatGPT shared link: ")
    main(shared_link)
