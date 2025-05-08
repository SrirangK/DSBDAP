from bs4 import BeautifulSoup

with open("Imdb.html","r",encoding="utf-8") as file:
    soup=BeautifulSoup(file,"lxml")

reviews = soup.find_all("article",class_="sc-571af6d2-1 hzjHJm user-review-item")

with open("imdb_review.txt","w",encoding="utf8") as f:
    for review in reviews:
        name = review.select_one("a.ipc-link.ipc-link--base")
        rating = review.select_one("span.ipc-rating-star--rating")
        comment = review.select_one(".ipc-title__text")

        f.write(f"name: {name.get_text(strip=True) if name else 'N/A'}\n")
        f.write(f"rating: {rating.get_text(strip=True) if rating else 'N/A'}\n")
        f.write(f"comment: {comment.get_text(strip=True) if comment else 'N/A'}\n")

        f.write("\n")

print("done")