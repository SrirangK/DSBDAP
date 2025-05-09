import csv
from bs4 import BeautifulSoup

with open("Flipkart.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "lxml")

reviews = soup.find_all("div", class_="EKFha-")

with open("flipkart_reviews.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Rating", "Comment"])  # Header

    for review in reviews:
        name = review.select_one("p._2NsDsF.AwS1CA")
        rating = review.select_one(".XQDdHH.Ga3i8K")
        comment = review.select_one(".ZmyHeo div div")

        writer.writerow([
            name.get_text(strip=True) if name else 'N/A',
            rating.get_text(strip=True)[:1] if rating else 'N/A',
            comment.get_text(strip=True) if comment else 'N/A'
        ])

print("Saved to flipkart_reviews.csv")
