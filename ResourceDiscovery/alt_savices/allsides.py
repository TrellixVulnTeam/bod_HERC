import os
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from regex import P
import requests
from time import sleep
import enlighten


def community_vote(ratio):
    # the value of the ratio goes through this if statement and 
    if ratio > 3:
        return "Absolutely Agree"

    elif 2 < ratio <= 3:
        return "Strongly Agree"

    elif 1.5 < ratio <= 2:
        return "Agree"

    elif 1 < ratio <= 1.5:
        return "Somewhat Agree"

    elif 0.67 < ratio < 1:
        return "Somewhat Disagree"

    elif 0.5 < ratio <= 0.67:
        return "Disagree"

    elif 0.33 < ratio <= 0.5:
        return "Strongly Disagree"

    elif ratio <= .33:
        return "Absolutely Disagree"

    elif ratio == 1:
        return "Neutral"

    else:
        return "N/A"


def table(full_table):
    
    # only collects data from the first table that shows not the ones that load after the infinite scroll.
    url = 'https://www.allsides.com/media-bias/ratings?field_featured_bias_rating_value=All&field_news_source_type_tid%5B%5D=1&field_news_source_type_tid%5B%5D=2&field_news_source_type_tid%5B%5D=3&field_news_source_type_tid%5B%5D=4&field_news_source_type_tid%5B%5D=5&field_news_bias_nid_1%5B1%5D=1&field_news_bias_nid_1%5B2%5D=2&field_news_bias_nid_1%5B3%5D=3&title='
    source = requests.get(url)
    soup = BeautifulSoup(source.content, 'lxml')
    main_table = soup.select('tbody tr')
    sleep(10)
    for row in main_table:
        f = dict()
        f['News Source'] = row.select_one('.source-title').text.strip()
        f['AllSides Bias Rating'] = row.select_one(
            '.views-field-field-bias-image a')['href'].split('/')[-1].replace("-", " ")
        f['News Media Info'] = 'https://www.allsides.com' + \
            row.select_one('.source-title a')['href']
        f['Agree'] = int(row.select_one('.agree').text)
        f['Disagree'] = int(row.select_one('.disagree').text)
        f['Ratio'] = (f['Agree'] / f['Disagree'])
        f['Community Feedback'] = community_vote(f['Ratio'])
        f['Ratio'] = '{:.3f}'.format(f['Ratio'])

        source2 = requests.get(f['News Media Info'])
        soup = BeautifulSoup(source2.content, 'lxml')
        try:
            # getting the website link to news source
            locate_html_class = soup.find('div', {'class': 'dynamic-grid'})
            locate_link = locate_html_class.find('a')['href']
            f['News Source Site'] = locate_link
        except:
            pass
        try:
            # getting the creation date of the news source
            locate_html_class = soup.find('div', {'class': 'dynamic-grid'})
            locate_creation_date = locate_html_class.find_all(
                'p')[1].text.split('.')[-1].strip()
            f['Established'] = locate_creation_date
        except:
            pass
        try:
            # who the news source owned by
            locate_html_class = soup.find('div', {'class': 'dynamic-grid'})
            locate_owned_by = locate_html_class.find_all(
                'p')[2].text.split(':')[-1].strip()
            f['Owned by'] = locate_owned_by
        except:
            pass
        try:
            # What the site covers / about
            locate_html_class = soup.find('p', {'class': 'more'})
            locate_about_paragraph = locate_html_class.get_text().strip()
            f['Info Paragraph'] = locate_about_paragraph
        except:
            pass
        sleep(10)
        try:
            locate_link = soup.find('a', {'alt': 'Wikipedia'})['href']
            if locate_link:
                f['Wikipedia Page'] = locate_link
        except:
            pass
        try:
            locate_link = soup.find('a', {'alt': 'Facebook'})['href']
            if locate_link:
                f['Facebook Page'] = locate_link
        except:
            pass
        try:
            locate_link = soup.find('a', {'alt': 'Twitter'})['href']
            if locate_link:
                f['Twitter Page'] = locate_link
        except:
            pass
        try:
            locate_link = soup.find('a', {'class': 'dev'})['href']
            if locate_link:
                f['website'] = locate_link
        except:
            pass
        try:
            locate_html_class = soup.find(
                'div', {'class': 'latest_news_source'})
            locate_link = locate_html_class.find('p').text
            f['type'] = locate_link
        except:
            pass
        yield (f)
        sleep(10)
    return full_table


def get_all_sides():
    full_table = []  # empty list
    for i in table(full_table):
        if 'Wikipedia Page' in i.keys() and i['Wikipedia Page'] is not None:
            wikipedia = urlparse(i['Wikipedia Page'])
            titles = os.path.split(wikipedia.path)[-1].replace("/", "")
            ccc = {
                "action": "query",
                "prop": "pageprops",
                "titles": titles,
                "format": "json",
            }
            wiki_url = "https://en.wikipedia.org/w/api.php"
            source2 = requests.get(wiki_url, params=ccc)
            data = source2.json()
            for c in data["query"]["pages"].keys():
                wikibase_item = data["query"]["pages"][c]["pageprops"]["wikibase_item"]
                if 'Wikidata' in i.keys():
                    i["Wikidata"].append(wikibase_item)
                else:
                    i["Wikidata"] = [wikibase_item]
            yield i
