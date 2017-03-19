
from django import forms
from pictaroo.models import Image, Category, UserProfile, Comment

class CategoryForm(forms.ModelForm):

    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    slug = forms.CharField(widget=forms.HiddenInput, required=False)

    #An inline class to provide additional information on the form
    class Meta:
        #provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)


#Chapter 14 - Creating the User Profile Form class
class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    bio = forms.Textarea()

    class Meta:
        model = UserProfile
        exclude = ('user',)

class ImageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text="Please enter the title of the Image.")
    image = forms.ImageField(required=True)


    class Meta:
            #Provide an association between the ModelForm and a model
            model = Image

            #what fields do we want to include in our form?
            #this way we dont need every field in the model present
            #some fields may allow NULL values, so we may not want to include them
            #Here, we are hiding the foreign key
            #we can either exclude the category field from the form
            #exclude = ('category', 'likes', 'views')
            # or specify the fields to include (i.e. not include the category field)
            fields = ('title', 'image',)


class CommentForm(forms.ModelForm):
    author = forms.CharField(max_length =200, required=False)
    text = forms.Textarea()

    class Meta:
        model = Comment
        exclude = ('image', 'user',)
