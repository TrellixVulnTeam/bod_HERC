
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
SPARQL_all_ddd = """
SELECT ?type_of_Wikidata_property ?type_of_Wikidata_propertyLabel WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  ?type_of_Wikidata_property wdt:P31 wd:Q107649491.
}
"""
SPARQL_all_fff = """
SELECT ?type_of_Wikidata_property ?type_of_Wikidata_propertyLabel ?formatter_URL WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  ?type_of_Wikidata_property wdt:P31 wd:%s.
  ?type_of_Wikidata_property wdt:P1630 ?formatter_URL.
}
"""
SPARQL_all_cccc = """
SELECT ?item ?resource ?formatter_URL WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  ?item wdt:%s ?resource. 
}
"""
