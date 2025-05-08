from bs4 import BeautifulSoup

with open("Ajio.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "lxml")

rating_block = soup.find("div", class_="product-rating")

if rating_block:
    overall_rating = rating_block.find("span", class_="_1P7MF")
    total_customers = rating_block.find("div", class_="_3AxgC")

    distribution_items = rating_block.select("ul li span._2AskX")

    with open("ratings_summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Overall Rating: {overall_rating.get_text(strip=True) if overall_rating else 'N/A'}\n")
        f.write(f"Total Customers: {total_customers.get_text(strip=True) if total_customers else 'N/A'}\n")
        f.write("\nRating Distribution:\n")

        for item in distribution_items:
            star_value = item.select_one(".desk-rate-cnt").text.strip()
            percentage = item.select_one("span._25HcP").text.strip()
            f.write(f"{star_value}: {percentage}\n")

    print("Saved to ajio_reviews.txt")
else:
    print("Rating block not found.")