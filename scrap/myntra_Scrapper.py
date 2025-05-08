from bs4 import BeautifulSoup

with open("Myntra.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "lxml")

reviews = soup.find_all("div", class_="user-review-userReviewWrapper")

with open("myntra_reviews.txt", "w", encoding="utf-8") as f:
    for review in reviews:
        name = review.select_one(".user-review-left span")
        rating = review.select_one(".user-review-starRating")
        comment = review.select_one(".user-review-reviewTextWrapper")

        f.write(f"Name: {name.get_text(strip=True) if name else 'N/A'}\n")
        f.write(f"Rating: {rating.get_text(strip=True) if rating else 'N/A'}\n")
        f.write(f"Comment: {comment.get_text(strip=True) if comment else 'N/A'}\n")
        f.write("-" * 40 + "\n")

print("Saved to myntra_reviews.txt")