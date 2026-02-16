from django import forms

from users.models import User

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'



class UserForm(StyleFormMixin, forms.ModelForm):
    model = User
    fields = ('email', 'first_name', 'last_name', 'phone')
    # exclude = ('is_active')

class UserRegisterForm(StyleFormMixin, forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль' , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        cd = self.cleaned_data
        print(cd)
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Ошибка! Пароли не совпадают!')
        return cd['password2']


class UserLoginForm(StyleFormMixin, forms.Form):
    email = forms.EmailField(label='email')
    password = forms.CharField(label='пароль', widget=forms.PasswordInput)


class UserUpdateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'telegram', 'avatar')