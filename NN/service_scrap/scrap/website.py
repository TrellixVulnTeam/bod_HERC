from bs4 import BeautifulSoup
import requests
import markdown


def website(url, id=None):
    exter_cat = []
    for i in range(20):
        try:
            r = requests.get(url)
            if r.status_code == 200:
                soup = BeautifulSoup(r.content, 'html.parser')
                for s in soup.select('script'):
                    s.extract()
                if soup.has_attr('some_attribute'):
                    lang = soup.html["lang"]
                else:
                    lang = "unknown"
                return str(soup), "html", lang, exter_cat
        except:
            pass
    return None, None, None, exter_cat


def website_bs(url, id=None):
    exter_cat = []
    data, mime, lang, exter_cat = website(url)
    if data is not None:
        soup = BeautifulSoup(data, 'html.parser')
        for link in soup.select('article'):
            return str(link), mime, lang, exter_cat
    return data, mime, lang, exter_cat


def website_markdown(url, id=None):
    exter_cat = []
    data, mime, lang, exter_cat = website(url)
    if data is not None:
        return markdown.markdown(data), "markdown", lang, exter_cat
    return data, "markdown", lang, exter_cat
