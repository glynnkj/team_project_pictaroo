import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'team_project_pictaroo.settings')

import django
django.setup()
from django.contrib.auth.models import User
from pictaroo.models import Category, Image, UserProfile, Comment
import random
import string
from django.utils import timezone

def populate ():
    # create users
    user_names = ["foo", "bar", "spam", "eggs"]
    user_profiles = []
    for user in user_names:
        u = User.objects.create_user(user, email=None, password="test")
        user_profiles.append(add_user_profile(u))

    path = os.path.dirname(os.path.abspath(__file__))+'/populate'

    funny_images = []
    for im in os.listdir(path+'/funny/'):
        #print path+'/funny/'+im
        #print im.split('.')[0]
        views = random.randint(0, 150)
        funny_images.append({
            "title": im.split('.')[0],
            "author": user_profiles[random.randint(0, len(user_profiles)-1)],
            "image": path+'/funny/'+im,
            "views": views,
            "likes": random.randint(0, views),
            })

    politics_images = []
    for im in os.listdir(path+'/politics/'):
        #print path+'/politics/'+im
        #print im.split('.')[0]
        views = random.randint(0, 150)
        politics_images.append({
            "title": im.split('.')[0],
            "author": user_profiles[random.randint(0, len(user_profiles)-1)],
            "image": path+'/politics/'+im,
            "views": views,
            "likes": random.randint(0, views),
            })

    food_images = []
    for im in os.listdir(path+'/food/'):
        #print path+'/food/'+im
        #print im.split('.')[0]
        views = random.randint(0, 150)
        food_images.append({
            "title": im.split('.')[0],
            "author": user_profiles[random.randint(0, len(user_profiles)-1)],
            "image": path+'/food/'+im,
            "views": views,
            "likes": random.randint(0, views),
            })

    cat_images = []
    for im in os.listdir(path+'/cats/'):
        #print path+'/cats/'+im
        #print im.split('.')[0]
        views = random.randint(0, 150)
        cat_images.append({
            "title": im.split('.')[0],
            "author": user_profiles[random.randint(0, len(user_profiles)-1)],
            "image": path+'/cats/'+im,
            "views": views,
            "likes": random.randint(0, views),
            })

    cats = { "Funny":{"images": funny_images},
             "Politics": {"images": politics_images},
             "Food": {"images": food_images},
             "Cat": {"images": cat_images},
    }

    for cat, cat_data in cats.items():
        print cat

        c = add_cat(cat)
        for p in cat_data["images"]:
            image = add_image(c, p["title"], p["author"], p["image"], p["views"], p["likes"])
            # add some comments to the image
            for i in range(0, random.randint(1, 2*len(user_profiles))):
                # generate random string
                comment_text = "".join( [random.choice(string.letters) for i in xrange(30)] )
                author = user_profiles[random.randint(0, len(user_profiles)-1)]
                add_comment(author, comment_text, image, random.randint(0, image.likes))

    #print out the categories we have added
    for c in Category.objects.all():
        for p in Image.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

import urllib2
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

def add_user_profile(user):
    u = UserProfile.objects.get_or_create(user=user)[0]
    return u

def add_comment(author, text, image, likes=0):
    C = Comment.objects.get_or_create(date=timezone.now(), author=author, image=image)[0]
    C.text = text
    C.likes = likes
    C.save()
    return C

def add_image(cat, title, author, image, views=0, likes=0):
    I = Image.objects.get_or_create(category=cat, title=title, author=author)[0]

    img_temp = NamedTemporaryFile(delete=True)
    img_temp.write(urllib2.urlopen('file://'+image).read())
    img_temp.flush()
    I.image.save(title, File(img_temp), save=True)

    print I.image.url
    I.views = views
    I.likes = likes
    I.save()
    return I

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

 #Start Execution here!
if __name__ == '__main__':
    print("Start Pictaroo population script...")
    populate()