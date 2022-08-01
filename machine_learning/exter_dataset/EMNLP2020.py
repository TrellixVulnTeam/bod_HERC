import os
import random
from machine_learning.exter_dataset.uitls.download import git_download
from machine_learning.exter_dataset.uitls.get_path import get_path


from transformers import BertTokenizer
url = "https://github.com/nguyenvo09/EMNLP2020"
dir_fs = os.path.dirname(os.path.realpath(__file__))
git_download(dir_fs, 'EMNLP2020',url)


def get_data():
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    politifact_article_mapped = get_path(dir_fs, 'retweet',"formatted_data/Politifact/article_mapped.json")
    politifact_articles_content = get_path(dir_fs, 'retweet',"formatted_data/Politifact/articles_content.json")
    politifact_queries_content = get_path(dir_fs, 'retweet',"formatted_data/Politifact/queries_content.json")
    politifact_query_article_interaction = get_path(dir_fs, 'retweet',"formatted_data/Politifact/query_article_interaction.csv")
    politifact_query_mapped = get_path(dir_fs, 'retweet',"formatted_data/Politifact/query_mapped.json")
    snopes_article_mapped = get_path(dir_fs, 'retweet',"formatted_data/Snopes/article_mapped.json")
    snopes_articles_content = get_path(dir_fs, 'retweet',"formatted_data/Snopes/articles_content.json")
    snopes_queries_content = get_path(dir_fs, 'retweet',"formatted_data/Snopes/queries_content.json")
    snopes_query_article_interaction = get_path(dir_fs, 'retweet',"formatted_data/Snopes/query_article_interaction.csv")
    snopes_query_mapped = get_path(dir_fs, 'retweet',"formatted_data/Snopes/query_mapped.json")
    path = random.choice([politifact_article_mapped,politifact_articles_content,politifact_queries_content,politifact_query_article_interaction,politifact_query_mapped ,snopes_article_mapped,snopes_articles_content,snopes_queries_content,snopes_query_article_interaction,snopes_query_mapped])
   
    # inputs = tokenizer(data["text"] , return_tensors="pt")
    