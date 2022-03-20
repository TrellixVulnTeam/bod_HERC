import enum
import os
from tkinter.messagebox import YES
from black import Enum
import flickr_api
from pkg_resources import UnknownExtra

from service_scrap.utility.m import P_actions_add
flickr_api.set_keys(api_key=api_key, api_secret=api_secret)


class trinary_knowledge (Enum):
    YES = 1
    Unknown = 0
    No = -1


def licenses(photo):
    license = {
        "licence_URL": "",
        "name": "",
        "all_rights_reserved": trinary_knowledge.Unknown.value,
        "attribution": trinary_knowledge.Unknown.value,
        "share_alike ": trinary_knowledge.Unknown.value,
        "non_commercial": trinary_knowledge.Unknown.value,
        "no_derivative_works": trinary_knowledge.Unknown.value,
        "no_rights_reserved": trinary_knowledge.Unknown.value,
        "ethical_license": trinary_knowledge.Unknown.value,
    }
    if 0 == photo.license:
        license["name"] = "All Rights Reserved"
        license["all_rights_reserved"] = trinary_knowledge.YES.value
        license["share_alike"] = trinary_knowledge.No.value
        license["non_commercial"] = trinary_knowledge.No.value
        license["attribution"] = trinary_knowledge.No.value
        license["no_derivative_works"] = trinary_knowledge.No.value
        license["no_rights_reserved"] = trinary_knowledge.No.value
        license["ethical_license"] = trinary_knowledge.No.value
    elif 1 == photo.license:
        license["name"] = "Attribution-NonCommercial-ShareAlike License"
        license["licence_URL"] = "https://creativecommons.org/licenses/by-nc-sa/2.0/"
        license["all_rights_reserved"] = trinary_knowledge.No.value
        license["attribution"] = trinary_knowledge.YES.value
        license["share_alike"] = trinary_knowledge.YES.value
        license["non_commercial"] = trinary_knowledge.YES.value
        license["no_derivative_works"] = trinary_knowledge.No.value
        license["no_rights_reserved"] = trinary_knowledge.No.value
        license["ethical_license"] = trinary_knowledge.No.value
    elif 2 == photo.license:
        license["name"] = "Attribution-NonCommercial License"
        license["licence_URL"] = "https://creativecommons.org/licenses/by-nc/2.0/"
        license["all_rights_reserved"] = trinary_knowledge.No.value
        license["attribution"] = trinary_knowledge.YES.value
        license["share_alike"] = trinary_knowledge.No.value
        license["non_commercial"] = trinary_knowledge.YES.value
        license["no_derivative_works"] = trinary_knowledge.No.value
        license["no_rights_reserved"] = trinary_knowledge.No.value
        license["ethical_license"] = trinary_knowledge.No.value
    elif 3 == photo.license:
        license["name"] = "Attribution-NonCommercial-NoDerivs License"
        license["licence_URL"] = "https://creativecommons.org/licenses/by-nc-nd/2.0/"
        license["all_rights_reserved"] = trinary_knowledge.No.value
        license["attribution"] = trinary_knowledge.YES.value
        license["share_alike"] = trinary_knowledge.No.value
        license["non_commercial"] = trinary_knowledge.YES.value
        license["no_derivative_works"] = trinary_knowledge.YES.value
        license["no_rights_reserved"] = trinary_knowledge.No.value
        license["ethical_license"] = trinary_knowledge.No.value
    elif 4 == photo.license:
        license["name"] = "Attribution License"
        license["all_rights_reserved"] = trinary_knowledge.No.value
        license["attribution"] = trinary_knowledge.YES.value
        license["share_alike"] = trinary_knowledge.No.value
        license["non_commercial"] = trinary_knowledge.No.value
        license["no_derivative_works"] = trinary_knowledge.No.value
        license["no_rights_reserved"] = trinary_knowledge.No.value
        license["ethical_license"] = trinary_knowledge.No.value
    elif 5 == photo.license:
        license["name"] = "Attribution-ShareAlike License"
        license["all_rights_reserved"] = trinary_knowledge.No.value
        license["share_alike"] = trinary_knowledge.YES.value
        license["attribution"] = trinary_knowledge.YES.value
        license["non_commercial"] = trinary_knowledge.No.value
        license["no_derivative_works"] = trinary_knowledge.No.value
        license["no_rights_reserved"] = trinary_knowledge.No.value
        license["ethical_license"] = trinary_knowledge.No.value
    elif 6 == photo.license:
        license["name"] = "Attribution-NoDerivs License"
        license["all_rights_reserved"] = trinary_knowledge.No.value
        license["share_alike"] = trinary_knowledge.No.value
        license["attribution"] = trinary_knowledge.YES.value
        license["non_commercial"] = trinary_knowledge.No.value
        license["no_derivative_works"] = trinary_knowledge.YES.value
        license["no_rights_reserved"] = trinary_knowledge.No.value
        license["ethical_license"] = trinary_knowledge.No.value
    elif 7 == photo.license:
        license["name"] = "No known copyright restrictions"
        license["all_rights_reserved"] = trinary_knowledge.Unknown.value
        license["share_alike"] = trinary_knowledge.Unknown.value
        license["non_commercial"] = trinary_knowledge.Unknown.value
        license["no_derivative_works"] = trinary_knowledge.Unknown.value
        license["no_rights_reserved"] = trinary_knowledge.Unknown.value
        license["ethical_license"] = trinary_knowledge.Unknown.value
        pass
    elif 8 == photo.license:
        license["name"] = "United States Government Work"
        license["all_rights_reserved"] = trinary_knowledge.Unknown.value
        license["share_alike"] = trinary_knowledge.Unknown.value
        license["non_commercial"] = trinary_knowledge.Unknown.value
        license["no_derivative_works"] = trinary_knowledge.Unknown.value
        license["no_rights_reserved"] = trinary_knowledge.Unknown.value
        license["ethical_license"] = trinary_knowledge.Unknown.value
    elif 9 == photo.license:
        license["name"] = "Public Domain Dedication (CC0)"
        license["all_rights_reserved"] = trinary_knowledge.Unknown.value
        license["share_alike"] = trinary_knowledge.YES.value
        license["non_commercial"] = trinary_knowledge.Unknown.value
        license["no_derivative_works"] = trinary_knowledge.Unknown.value
        license["no_rights_reserved"] = trinary_knowledge.Unknown.value
        license["ethical_license"] = trinary_knowledge.Unknown.value
    elif 10 == photo:
        license["name"] = "Public Domain Mark"
        license["all_rights_reserved"] = trinary_knowledge.Unknown.value
        license["share_alike"] = trinary_knowledge.YES.value
        license["non_commercial"] = trinary_knowledge.Unknown.value
        license["no_derivative_works"] = trinary_knowledge.Unknown.value
        license["no_rights_reserved"] = trinary_knowledge.Unknown.value
        license["ethical_license"] = trinary_knowledge.Unknown.value
    return license


def get_photo_by_tag(tag):
    w = flickr_api.Walker(flickr_api.Photo.search, tags=tag)
    for photo in w:
        print(photo)


def get_photo_by_user_Email(email):
    l = []
    user = flickr_api.Person.findByEmail(email)
    photos = user.getPhotos()
    for photo in photos:
        l.append(image_pass(photo))
    return l


def wait():
    pass

def get_photo_by_ID(id):
    l = []
    user = flickr_api.Person.getInfo(id)
    photos = user.getPhotos()
    for photo in photos:
        l.append(image_pass(photo))
    return l


def get_photo_by_User_name(user_name):
    l = []
    user = flickr_api.Person.findByUserName(user_name)
    photos = user.getPhotos()
    for photo in photos:
        l.append(image_pass(photo))
    return l


def image_pass(photo):
    exif_ = {}
    favorite_ = {}
    interest_ = {}
    tag_ = []
    people_ = []
    comment_ = []
    for exif in photo.getExif():
        exif_[exif.label] = exif.raw
    for favorite in photo.getFavorites():
        favorite_[favorite.username] = favorite.id
    # for interest in photo.getInteresting():
    #     print(dir(interest))
    #     # interest_.append({"text":interest.title,"id":interest.id})
    for people in photo.getPeople():
        people_.append({"username": people.username, "id": people.id})
    for tag in photo.getTags():
        tag_.append({"text": tag.text, "id": tag.id})
    for comment in photo.getComments():
        comment_.append({
            "id": comment.id,
            "text": comment.text,
            "author": {"id": comment.author.id, "username": comment.author.username}
        })
    size_label = photo._getLargestSizeLabel()
    return {
        "where": "Flicker",
        "type": "image",
        "exif_": exif_,
        "favorite_": favorite_,
        "interest_": interest_,
        "tag_": tag_,
        "people_": people_,
        "comment_": comment_,
        "photo": photo.id,
        "url": photo.getPhotoFile(size_label),
        "id": photo.id,
        "licenses": licenses(photo)
    }
P_actions_add("P968",get_photo_by_user_Email)
P_actions_add("P3267",get_photo_by_ID)
get_photo_by_User_name("tomquirkphoto")
