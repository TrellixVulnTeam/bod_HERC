import service_scrap.service
from random import random
import praw


def reddit_comment(comment):
    return "A"


def reddit_submission(submission):
    ppp = dir(submission)
    output = {}
    if "comments" in ppp:
        output["comments"] = []
        for comment in submission.comments:
            output["comments"].append(reddit_comment(comment))
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
        pass
    if "title" in ppp:
        output["title"] = submission.title
    if "upvote_ratio" in ppp:
        output["upvote_ratio"] = submission.upvote_ratio
    if "url" in ppp:
        ff = False
        for fileformat in service_scrap.service.image_format:
            if fileformat in output["url"]:
                output["url"] = submission.url
                output["resource"] = data = service_scrap.service.do_someting(
                    type="image", url=output["url"])
                ff = True
            break
        for fileformat in service_scrap.service.video_format:
            if fileformat in output["url"]:
                output["url"] = submission.url
                output["resource"] = data = service_scrap.service.do_someting(
                    type="video", url=output["url"])
                ff = True
            break
        if not ff:
            output["resource"] = data = service_scrap.service.do_someting(
                type="website", url=output["url"])


def reddit_redditwebsite(toplevel):
    thing = []
    exter_cat = []
    when = random.choice(["week"])
    for i in reddit.domain(toplevel).controversial(when):
        thing.append(i)
    for i in reddit.domain(toplevel).hot(when):
        thing.append(i)
    for i in reddit.domain(toplevel).new(when):
        thing.append(i)
    for i in reddit.domain(toplevel).rising():
        thing.append(i)
    if len(thing) == 0:
        return None, None, None, exter_cat
    return reddit_submission(random.choice(thing)), "reddit_subreddit", "unknown", exter_cat


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
