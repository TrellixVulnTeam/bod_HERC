import enum
import os
from tkinter.messagebox import YES
import flickr_api
from pkg_resources import UnknownExtra

flickr_api.set_keys(api_key = api_key, api_secret = api_secret)    
class trinary_knowledge (enum):
    YES = 1
    Unknown = 0
    No = -1

def licenses(photo):
    license = {
        "licence URL":"",
        "all_rights_reserved":trinary_knowledge.Unknown,
        "Attribution":trinary_knowledge.Unknown,
        "Share_alike ":trinary_knowledge.Unknown,
        "Non_commercial":trinary_knowledge.Unknown,
        "No_derivative_works":trinary_knowledge.Unknown,
        "No_Rights_Reserved":trinary_knowledge.Unknown,
        "ethical license":trinary_knowledge.Unknown,
    }

def get_photo_by_tag(tag):
    w = Walker(Photo.search, tags=tag)
    for photo in w:
        print(photo)

def get_photo_by_user_Email(email):
    user = flickr_api.Person.findByEmail(email)
    photos = user.getPhotos()
    for photo in photos:
        comments = photo.getComments()
        print(photo)

def wait():
    pass
def get_photo_by_User_name(user_name):
    user = flickr_api.Person.findByUserName(user_name)
    photos = user.getPhotos()
    for photo in photos:
        image_pass(photo)
def image_pass(photo):
        exif_ = {}
        favorite_ = {}
        interest_ = {}
        tag_ = []
        people_ = []
        comment_ = []
        for exif in photo.getExif ():
            exif_[exif.label] = exif.raw
        for favorite in photo.getFavorites ():
            favorite_[favorite.username] = favorite.id
        # for interest in photo.getInteresting():
        #     print(dir(interest))
        #     # interest_.append({"text":interest.title,"id":interest.id})
        for people in photo.getPeople():
            people_.append({"username":people.username,"id":people.id})
        for tag in photo.getTags():
            tag_.append({"text":tag.text,"id":tag.id})
        for comment in photo.getComments():
            comment_.append({
                "id":comment.id,
                "text":comment.text,
                "author":{"id":comment.author.id,"username":comment.author.username}
            })
        size_label = photo._getLargestSizeLabel()
        print({
            "where":"Flicker",
            "type":"image",
            "exif_":exif_,
            "favorite_":favorite_,
            "interest_":interest_,
            "tag_":tag_,
            "people_":people_,
            "comment_":comment_,
            "photo":photo.id,
            "url":photo.getPhotoFile(size_label),
            "id":photo.id,
        })
get_photo_by_User_name("tomquirkphoto")