from bs4 import BeautifulSoup
import pandas as pd
import os

d = {'title': [], 'offer-price': [], 'actual-price': [], 'link': []}

for file in os.listdir("details"):
    try:
        with open(f"details/{file}", encoding="utf-8") as f:
            html_doc = f.read()

        soup = BeautifulSoup(html_doc, 'html.parser')

        # Get Title
        t = soup.find("h2")
        if t:
            title = t.get_text(strip=True)
        else:
            title = "N/A"

        # Get Link
        l = soup.find("a", attrs={"class": "a-link-normal"}) if t else None
        if l and l.has_attr('href'):
            link = "https://amazon.in/" + l['href']
        else:
            link = "N/A"

        # Offer Price
        op = soup.find("span", attrs={"class": "a-price-whole"})
        if op:
            oprice = op.get_text(strip=True)
        else:
            oprice = "N/A"

        # Actual Price
        ap = soup.find("span", attrs={"class": "a-text-price"})
        if ap:
            app = ap.find("span", attrs={"aria-hidden": "true"})
            if app:
                aprice = app.get_text(strip=True)
                # Remove first 3 characters if string is long enough
                aprice = aprice[1:] if len(aprice) > 3 else aprice
            else:
                aprice = "N/A"
        else:
            aprice = "N/A"

        d['title'].append(title)
        d['offer-price'].append(oprice)
        d['actual-price'].append(aprice)
        d['link'].append(link)

        print(title, link)
        print(oprice)
        print(aprice)

    except Exception as e:
        print("Error processing file:", file, e)

df = pd.DataFrame(data=d)
df.to_csv("data.csv", index=False)
