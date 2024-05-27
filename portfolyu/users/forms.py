from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from users.models import Profil


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password1','password2')
        label = {
            'first_name':"Ism",
            'last_name':"Sharif",
            'email':"Elektron manzil",
            'username':"login"
        }


    def __init__(self,*args,**kwargs):
        super(ModelForm,self).__init__(*args,**kwargs)
        for key,field in self.fields.items():
            field.widget.attrs.update({"class":"input input--text"})

class CustomProfilCreationForm(ModelForm):
    class Meta:
        model = Profil
        fields = ('name','email','info','bio','social_git_hub','social_facebook','social_youtube','social_instagram','image')
    def __init__(self,*args,**kwargs):
        super(ModelForm,self).__init__(*args,**kwargs)
        for key,field in self.fields.items():
            field.widget.attrs.update({"class":"input input--text"})
