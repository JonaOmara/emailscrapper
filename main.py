# main.py

from config import BASE_URL, CSV_OUTPUT
from scraper.driver import setup_driver
from scraper.extractor import scrape_club_details
from scraper.navigation import get_club_elements, go_to_next_page
from scraper.utils import save_to_csv


def main():
    driver = setup_driver()
    driver.get(BASE_URL)

    club_data = []
    page = 1

    count = 3 # Remove this line to scrap all the pages. This only scraps first 2 pages
    while page < count: # Remove this line to scrap all pages then uncomment the one below
    # while True:
        print(f"\n📄 Processing page {page}...")
        club_elements = get_club_elements(driver)

        for i, club in enumerate(club_elements, 1):
            print(f"🔎 Processing club {i}/{len(club_elements)} on page {page}")
            club_data.append(scrape_club_details(driver, club))

        if not go_to_next_page(driver):
            print("✅ Finished all pages.")
            break

        page += 1

    save_to_csv(club_data, CSV_OUTPUT)
    driver.quit()
    print("🎉 Scraping completed.")


if __name__ == "__main__":
    main()
