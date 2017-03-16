import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'team_project_pictaroo.settings')

import django
django.setup()
from pictaroo.models import Category, Image
import random

def populate ():
        path = os.path.dirname(os.path.abspath(__file__))+'/populate'

        funny_images = []
        for im in os.listdir(path+'/funny/'):
            #print path+'/funny/'+im
            #print im.split('.')[0]
            funny_images.append({
                "title": im.split('.')[0],
                "image": path+'/funny/'+im,
                "views": random.randint(0, 150),
                })

        politics_images = []
        for im in os.listdir(path+'/politics/'):
            #print path+'/politics/'+im
            #print im.split('.')[0]
            politics_images.append({
                "title": im.split('.')[0],
                "image": path+'/politics/'+im,
                "views": random.randint(0, 150),
                })

        food_images = []
        for im in os.listdir(path+'/food/'):
            #print path+'/food/'+im
            #print im.split('.')[0]
            food_images.append({
                "title": im.split('.')[0],
                "image": path+'/food/'+im,
                "views": random.randint(0, 150),
                })

        cat_images = []
        for im in os.listdir(path+'/cats/'):
            #print path+'/cats/'+im
            #print im.split('.')[0]
            cat_images.append({
                "title": im.split('.')[0],
                "image": path+'/cats/'+im,
                "views": random.randint(0, 150),
                })

        cats = { "Funny":{"images": funny_images , "views": 20, "likes": 15},
                 "Politics": {"images": politics_images, "views": 20, "likes": 15},
                 "Food": {"images": food_images, "views": 20, "likes": 15},
                 "Cat": {"images": cat_images, "views": 20, "likes": 15}
        }

        for cat, cat_data in cats.items():
            print cat

            c = add_cat(cat, cat_data["views"], cat_data["likes"])
            for p in cat_data["images"]:
                add_image(c, p["title"], p["image"], p["views"])

        #print out the categories we have added
        for c in Category.objects.all():
            for p in Image.objects.filter(category=c):
                print("- {0} - {1}".format(str(c), str(p)))

import urllib2
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

def add_image(cat, title, image, views=0):
    I = Image.objects.get_or_create(category=cat, title=title)[0]

    img_temp = NamedTemporaryFile(delete=True)
    img_temp.write(urllib2.urlopen('file://'+image).read())
    img_temp.flush()
    I.image.save(title, File(img_temp), save=True)

    print I.image.url

    I.views = views
    I.save()
    return I

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

 #Start Execution here!
if __name__ == '__main__':
    print("Start Pictaroo population script...")
    populate()