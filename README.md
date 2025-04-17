# Email Scrapper

## Task : Scrapping club emails using Selenium pagination

The website scraped can be accessed through this link [Road Runners Club of America](https://www.rrca.org/clubs/) 
<p float="center">
  <img src="/page1.png" width="1000" />
</p>

## Tools:
- Selenium
- Pandas
- Chrome WebDriver
- Python standard libraries
## Deploy:
To automate:
- Add to a cron job (Linux) or Task Scheduler (Windows)
- Or use a job runner like Apache Airflow, Prefect, or GitHub Actions for cloud scheduling.
## Output:
This code outputs a csv file but you can edit the `utils.py` file to output a json and parse it as an API.
```# scraper/utils.py

import pandas as pd
import os
import json

def save_to_csv(data, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"✅ Data saved to {filename}")

def save_to_json(data, json_path):
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"✅ Data also saved to {json_path}")

def return_json(data):
    """Return JSON-formatted string (for use like an API response)"""
    return json.dumps(data, indent=4)```
In your main() function, add:
```from scraper.utils import save_to_csv, save_to_json, return_json

# Save to CSV
save_to_csv(club_data, CSV_OUTPUT)

# Save to JSON file
save_to_json(club_data, "output/running_clubs.json")

# Optional: Print like API response
print(return_json(club_data))  # or return this if integrating into a Flask API
```
You can integrate with Flask or FastAPI. Example:
```# api_server.py (Optional if you want an API)
from flask import Flask, jsonify
from scraper.utils import return_json
from scraper.driver import setup_driver
from scraper.navigation import get_all_club_links
from scraper.fetcher import fetch_email_from_page

app = Flask(__name__)

@app.route("/scrape", methods=["GET"])
def scrape_and_return_json():
    driver = setup_driver()
    club_links = get_all_club_links(driver, "https://www.rrca.org/clubs/")
    driver.quit()

    data = [{"Club name": c["name"], "club_email": fetch_email_from_page(c["url"])} for c in club_links]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
```
