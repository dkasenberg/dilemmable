from django import forms
# TODO: this should be replaced with the auth user form to which we can add/remove attrs
from django.contrib.auth import get_user_model

User = get_user_model()

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.label_suffix = ''
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['username'].required = True

    class Meta:
        model = User
        fields =['email', 'first_name', 'last_name', 'username']
        labels = {'email':'Email'}


# TODO: smell
# this is a little odd. creates a user and a systemadmin object
# would be better to use permissiosn on user
# class SystemAdminForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(SystemAdminForm, self).__init__(*args, **kwargs)

#         # TODO: could set require fields in model i think
#         self.fields['username'].required = True
#         self.fields['first_name'].required = True
#         self.fields['last_name'].required = True
#         self.fields['email'].required = True

#     def save(self, commit = True):
#         # TODO: what if user already exists?
#         user = super(SystemAdminForm, self).save(commit = False)
#         user.set_password(self.cleaned_data['password'])

#         if commit:
#             user.save()

#         return user

#     class Meta:
#         model = User
#         fields =['username', 'password', 'email', 'first_name', 'last_name']
