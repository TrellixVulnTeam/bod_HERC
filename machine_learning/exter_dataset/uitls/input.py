def input_text(text,language):
    return {
        "type":"text",
        "language":language,
        "text":text  
    }
def input_factCheck_evidence(value,relevancy):
    return {
        "type":"fact_check",
        "value":value,
        "relevancy":relevancy
    }

def input_url(url):
    return {
        "type":"url",
        "url":url  
    }
def input_twitter_post(id,language):
    return {
        "type":"twitter_post",
        "language":language,
        "id":id  
    }
def input_reddit_post(id,language):
    return {
        "type":"reddit_post",
        "language":language,
        "id":id  
    }


def output_classifier(data,name):
    return {
    "type":"classifier",
    "data":data,
    "name":name,
    }

def output_float(data,name):
    return {
    "type":"float",
    "data":data,
    "name":name,
    }