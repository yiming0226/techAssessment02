import requests
from bs4 import BeautifulSoup

# Base URL for the first page (without the page number)
base_url = "https://www.wired.com/most-recent/"

# Loop through multiple pages starting from page 1 to page 10
for page_num in range(1, 501):  # Adjust the range for more pages
    # Construct the URL for the current page
    if page_num == 1:
        url = base_url  # No page parameter for the first page
    else:
        url = base_url + f"?page={page_num}"

    # Send a GET request to the current page
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all article headline elements based on the updated class
    headlines = soup.find_all("a",
                              class_="SummaryItemHedLink-civMjp ejgyuy summary-item-tracking__hed-link summary-item__hed-link")

    # If there are no headlines, break the loop (end of pagination)
    if not headlines:
        break

    # Loop through the headlines and print them with the hyperlink
    print(f"--- Page {page_num} ---")
    for headline in headlines:
        # Extract the headline text (from the h3 tag inside the anchor)
        title = headline.find("h3").get_text()

        # Extract the link (href attribute of the anchor)
        link = headline['href']

        # Construct the full URL
        full_url = f"https://www.wired.com{link}"

        # Print the title and the corresponding link
        print(f"{title}: {full_url}")
