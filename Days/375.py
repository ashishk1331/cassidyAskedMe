# Question 375

# Write a function that takes in an RSS feed URL, and
# returns the title of and link to the the original
# feed source. You can get other things too, if you'd like!

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def getRSS(URL):
    # fetch the title
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, features="xml")
    title = soup.title.string

    # prepare website url
    url = urlparse(URL)
    p = url.netloc.split(".")
    website = p.pop()
    website = p.pop() + "." + website

    # forge the result
    res = title + ", " + f"{url.scheme}://{website}"
    return res


def main():
    assert (
        getRSS("https://cassidoo.co/rss.xml") == "Cassidy Williams, https://cassidoo.co"
    )
    assert (
        getRSS("https://feed.syntax.fm/")
        == "Syntax - Tasty Web Development Treats, https://syntax.fm"
    )


if __name__ == "__main__":
    main()
