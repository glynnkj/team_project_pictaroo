import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'team_project_pictaroo.settings')

import django
django.setup()
from rango.models import Category, Image

def populate ():

        funny_images = [
            {"title": "LOLOLOL",
            "image": ,
            "views": 100},

        ]

        politics_images = [

        ]

        food_images = [

        ]

        cat_images = [

        ]

        cats = { "Funny":{"images": funny_images , "views": 20, "likes": 15},
                 "Politics": {"images": politics_images, "views": 20, "likes": 15},
                 "food_images": {"images": food_images, "views": 20, "likes": 15},
                 "cat_images": {"images": cat_images, "views": 20, "likes": 15}
        }

        for cat, cat_data in cats.items():
            c = add_cat(cat, cat_data["views"], cat_data["likes"])
            for p in cat_data["pages"]:
                add_image(c,p["title"], p["image"], p["views"])

        #print out the categories we have added
        for c in Category.objects.all():
            for p in Image.objects.filter(category=c):
                print("- {0} - {1}".format(str(c), str(p)))

def add_image(cat, title, image, views=0):
      I = Image.objects.get_or_create(category=cat, title=title)[0]
      I.image = image
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