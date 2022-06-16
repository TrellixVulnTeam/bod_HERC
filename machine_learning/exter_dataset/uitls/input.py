def input_text(text,language):
    return {
        "type":"text",
        "language":language,
        "text":text  
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

