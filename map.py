from playwright.sync_api import sync_playwright
import pandas as pd
import time


def scrape_google_maps(search_query, max_results=20):
    data = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        url = f"https://www.google.com/maps/search/{search_query.replace(' ', '+')}"
        page.goto(url, wait_until="networkidle")

        time.sleep(5)

        # Scroll results panel
        results_panel = page.locator('div[role="feed"]')

        previous_count = 0

        while True:
            cards = page.locator('a[href*="/place/"]')
            count = cards.count()

            if count >= max_results or count == previous_count:
                break

            previous_count = count

            results_panel.evaluate(
                "(el) => el.scrollBy(0, el.scrollHeight)"
            )

            time.sleep(2)

        cards = page.locator('a[href*="/place/"]')
        total = min(cards.count(), max_results)

        for i in range(total):
            try:
                cards.nth(i).click()
                page.wait_for_timeout(3000)

                name = ""
                rating = ""
                address = ""

                try:
                    name = page.locator("h1").first.inner_text()
                except:
                    pass

                try:
                    rating = page.locator(
                        'div[role="main"] span[aria-hidden="true"]'
                    ).first.inner_text()
                except:
                    pass

                try:
                    address_btn = page.locator(
                        'button[data-item-id="address"]'
                    ).first
                    address = address_btn.inner_text()
                except:
                    pass

                data.append({
                    "name": name,
                    "rating": rating,
                    "address": address
                })

            except Exception as e:
                print(f"Error processing record {i}: {e}")

        browser.close()

    return pd.DataFrame(data)


if __name__ == "__main__":
    df = scrape_google_maps(
        search_query="restaurants in Chennai",
        max_results=20
    )

    print(df)
    df.to_csv("google_maps_results.csv", index=False)