from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Введите пароль', min_length=8)
    repeat_password = forms.CharField(widget=forms.PasswordInput, label='Повторите пароль', min_length=8)
    age = forms.IntegerField(label='Введите свой возраст')

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise forms.ValidationError('Вы должны быть старше 18 лет.')
        return age
