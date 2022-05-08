
SPARQL_all_website = """
SELECT * WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  { ?item wdt:P856 ?official_website. }
}
"""
SPARQL_offical_blog = """
SELECT * WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  OPTIONAL { ?item wdt:P1581 ?official_blog. }
}
"""
SPARQL_all_feeds = """
SELECT * WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
    OPTIONAL {?item wdt:P1019 ?web_feed_URL.}
}
"""
