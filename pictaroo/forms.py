
from django import forms
from pictaroo.models import Image, Category, UserProfile

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length =128,
                           help_text="Please enter the category name.")
    view = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput, required=False)

    #An inline class to provide additional information on the form
    class Meta:
        #provide an association between the ModelForm andn a model
        model = Category
        fields = ('name',)

class ImageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text="Please enter the title of the Image.")

    #views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    image = forms.ImageField(required=True)

    #will remove this
    def image_tag(self):
        return u'<img src="%s" />'

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    class Meta:
            #Provide an association between the ModelForm and a model
            model = Image

            #what fields do we want to include in our form?
            #this way we dont need every field in the model present
            #some fields may allow NULL values, so we may not want to include them
            #Here, we are hiding the foreign key
            #we can either exclude the category field from the form
            exclude = ('category',)
            # or specify the fields to include (i.e. not include the category field)
            #fields = ('title', 'url', views)


#Chapter 14 - Creating the User Profile Form class
class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    bio = forms.Textarea()

    class Meta:
        model = UserProfile
        exclude = ('user',)