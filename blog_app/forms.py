from django import forms
from django.contrib.auth import get_user_model
from blog_app.models import *

User = get_user_model()

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Sifre',widget=forms.PasswordInput(
        attrs={"class": "form-control"}
    ))
    password2 = forms.CharField(label='Sifrenin testiqi', widget=forms.PasswordInput(
        attrs={"class": "form-control"} 
    ))
    class Meta:
        model = User
        fields = (
            "first_name", "last_name", "email"
        )
        labels = {
            "first_name": "Ad",
            "last_name": "Soyad",
            "email": "Email"
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 == password2:
            pass
        else:
            raise forms.ValidationError("Sifre testiqlenmesi alinmadi")



# class BlogForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = ("title", "sub_title", "text",  "image")


class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("category", "title", "sub_title", "body", "image", "status",)
        labels = {
            "category": "Kateqoriya",
            "title": "Başlıq",
            "sub_title": "Məqalənin qısa mövzusu",
            "body": "Məqalə",
            "image": "Şəkil",
            "status": "Paylaşılsınmı? ",
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': 'custom-select',
                                                     'placeholder': 'Kateqoriyalar'})
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['sub_title'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'btn btn-info;'})
        self.fields['status'].widget.attrs.update({'class': 'form-check-input position-static',
                                                    'placeholder': 'Kateqoriyalar',
                                                    'id': 'customControlAutosizing'})



        

        # self.fields['status'].widget=forms.BooleanField(attrs={'placeholder': 'Adınız',
        #                                                      'class':'form-control'})

# class PasswordChangeForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['category'].widget.attrs.update({'class': 'custom-select',
#                                                      'placeholder': 'Kateqoriyalar'})
#         self.fields['title'].widget.attrs.update({'class': 'form-control'})
#         self.fields['sub_title'].widget.attrs.update({'class': 'form-control'})
#         self.fields['image'].widget.attrs.update({'class': 'btn btn-info;'})
#         self.fields['status'].widget.attrs.update({'class': 'form-check-input position-static',
#                                                     'placeholder': 'Kateqoriyalar',
#                                                     'id': 'customControlAutosizing'})    


class ContactForm(forms.Form):
    fullname = forms.CharField(label='search', required=True, 
                               widget=forms.TextInput(attrs={'placeholder': 'Adınız',
                                                             'class':'form-control',
                                                             'id':'input_name'}))
    from_emaill = forms.EmailField(label='search', required=True, 
                               widget=forms.TextInput(attrs={'placeholder': 'E-poçt',
                                                             'class':'form-control',
                                                             'id': 'input_email'}))
    message = forms.CharField(label='search', required=True, 
                               widget=forms.Textarea(attrs={'placeholder': 'Sualınızı qeyd edin',
                                                            'class':'form-control', 
                                                            'id':'textarea_message' }))
