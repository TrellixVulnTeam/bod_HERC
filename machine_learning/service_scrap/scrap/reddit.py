import pathlib
from urllib.parse import urlparse
from matplotlib.font_manager import json_load
import machine_learning.service_scrap.service
import random
import asyncpraw
import json
file = open("./serrice_settings.json")
reddit_seetings = json.loads(file.read())["reddit"]
reddit = asyncpraw.Reddit(
    client_id=reddit_seetings["client_id"],
    client_secret=reddit_seetings["client_secret"],
    user_agent=reddit_seetings["user_agent"],
)


def reddit_comment(comment):
    return "A"


def reddit_submission(submission):
    exter_cat = {}
    ppp = dir(submission)
    output = {}
    # if "comments" in ppp:
    # output["comments"] = []
    # for comment in submission.comments:
    # output["comments"].append(reddit_comment(comment))
    if "created_utc" in ppp:
        output["created_utc"] = submission.created_utc
    if "distinguished" in ppp:
        output["distinguished"] = submission.distinguished
    if "edited" in ppp:
        output["edited"] = submission.edited
    if "id" in ppp:
        output["id"] = submission.id
    if "is_self" in ppp:
        output["is_self"] = submission.is_self
    if "locked" in ppp:
        output["locked"] = submission.locked
    if "name" in ppp:
        output["name"] = submission.name
    if "num_comments" in ppp:
        output["num_comments"] = submission.num_comments
    if "over_18" in ppp:
        output["over_18"] = submission.over_18
    if "poll_data" in ppp:
        pass
    if "score" in ppp:
        output["score"] = submission.score
    if "selftext" in ppp:
        output["selftext"] = submission.selftext
    if "spoiler" in ppp:
        output["spoiler"] = submission.spoiler
    if "stickied" in ppp:
        output["stickied"] = submission.stickied
    if "subreddit" in ppp:
        exter_cat["reddit_subreddit"] = [str(submission.subreddit)]
    if "title" in ppp:
        output["title"] = submission.title
    if "upvote_ratio" in ppp:
        output["upvote_ratio"] = submission.upvote_ratio
    if "url" in ppp:
        ff = False
        o = urlparse(submission.url)
        o.path
        suffix = pathlib.Path(o.path).suffix
        for fileformat in machine_learning.service_scrap.service.image_format:
            if fileformat in submission. url:
                output["url"] = submission.url
                output["resource"] = data = machine_learning.service_scrap.service.do_someting(
                    type="image", url=output["url"])
                ff = True
            break
        for fileformat in machine_learning.service_scrap.service.video_format:
            if fileformat in submission.url:
                output["url"] = submission.url
                output["resource"] = data = machine_learning.service_scrap.service.do_someting(
                    type="video", url=output["url"])
                ff = True
            break
        for fileformat in ["html", "htm"]:
            output["url"] = submission.url
            output["resource"] = data = machine_learning.service_scrap.service.do_someting(
                type="website", url=output["url"])
            ff = True

        if not ff and len(suffix) == 0:
            output["url"] = submission.url
            output["resource"] = machine_learning.service_scrap.service.do_someting(
                type="website", url=submission.url)
    return output, exter_cat, [submission.url, "https://www.reddit.com/r/" + str(submission.subreddit)]


async def reddit_redditwebsite(toplevel):
    try:
        thing = []
        exter_cat = {}
        when = random.choice(
            ["week", "all", "day", "hour", "month", "week", "year"])
        domain = urlparse(toplevel).netloc
        for i in await reddit.domain(domain).hot():
            thing.append(i)
        if len(thing) == 0:
            return None, None, None, exter_cat, {}
        data, exter_cat, urls = reddit_submission(random.choice(thing))
        return data, "reddit_subreddit", "unknown", exter_cat, urls
    except:
        return None, None, None, None, None


def reddit_subreddit(resource):
    return None, None, None


def reddit_redditUser(resource):
    return None, None, None


def PushShift_redditwebsite(toplevel):
    return None, "reddit", None


def PushShift_subreddit(resource):
    return None, None, None


def PushShift_redditUser(resource):
    return None, None, None


def Mix_redditwebsite(toplevel):
    return None, "reddit", None


def Mix_subreddit(resource):
    return None, None, None


def Mix_redditUser(resource):
    return None, None, None
