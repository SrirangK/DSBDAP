from bs4 import BeautifulSoup

with open("Shopclue.html","r",encoding="utf-8") as file:
    soup=BeautifulSoup(file,"lxml")

reviews=soup.select("div.rnr_lists ul > li")



with open("shopclue.txt","w",encoding="utf-8") as f:
    for review in reviews:
        name = review.select_one(".r_by")
        rating=review.select_one(".prd_ratings span")
        comment = review.select_one(".review_desc p")

        f.write(f"name: {name.get_text(strip=True) if name else 'N/A' }\n")
        f.write(f"rating: {rating.get_text(strip=True) if rating else 'N/A'}\n")
        f.write(f"comment: {comment.get_text(strip=True) if comment else 'N/A'}\n")
        f.write("\n")

print("done")