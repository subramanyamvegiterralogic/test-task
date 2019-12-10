import csv
import requests
import xml.etree.ElementTree as et


def load_RSS():
    # url of rss feed
    url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'

    # creating HTTP response object from given url
    resp = requests.get(url)

    # Saving the XML File
    with open('top_news_feed.xml','wb') as f:
        f.write(resp.content)


def parse_XML(xml_file):
    # Create element Tree Object
    tree = et.parse(xml_file)

    # Get ROOT Element
    root = tree.getroot()

    # Create empty list for root items
    news_items = []

    # Iterate News Items
    for item in root.findall('./channel/item'):

        # Empty News Dictionary
        news = {}

        # Iterate Childs Items of Item
        for child in item:
            # special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf-8')

            # Append News Directory to news items list
            print(news)
            news_items.append(news)

        # return news items list
        return news_items


def save_to_csv(news_items, file_name):
    # specifing the fields for csv file
    fields = ['guid', 'title', 'pubDate', 'description', 'link', 'media']

    # writting to csv file
    with open(file_name, 'w') as csv_file:

        # creating csv dict writter object
        writter = csv.DictWriter(csv_file, fieldnames= fields)

        # writting headers (field Names)
        writter.writeheader()

        # Writting data rows
        writter.writerows(news_items)


def main():
    # Load RSS from web to update existing xml file
    load_RSS()

    # parse XML File
    newsitems = parse_XML('top_news_feed.xml')

    # store news items in a csv file
    save_to_csv(newsitems, 'top_news.csv')


if __name__ == '__main__':
    # Calling Main Function
    main()