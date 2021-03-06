"""
Python script to download all articles from Zendesk in proper format.
"""

import requests
import os

import file_constants

IMAGE_FORMATS = file_constants.IMAGE_FORMATS

def main():
    make_folder("posts")
    url = file_constants.get_url_from_subdomain(os.environ["ZENDESK_SUBDOMAIN"])

    while url:
        response = requests.get(url)
        data = response.json()

        for article in data["articles"]:
            print "Processing article #" + str(article["id"])
            article_path = "posts/" + str(article["id"])
            make_folder(article_path)

            body = open(article_path + "/index.html", "a")
            body.write(article["body"])

            title = open(article_path+ "/title.html", "a")
            title.write(article["title"])

        url = data["next_page"]

def make_folder(path):
    try:
        os.stat(path)
    except:
        os.mkdir(path)

if __name__ == "__main__":
    main()
