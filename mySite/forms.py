from django.forms import Form, CharField, TextInput, Textarea


class CommentForm(Form):
    """ Комментарий """
    message = CharField(
        max_length=1000,
        widget=Textarea(attrs={
            'id': 'message',
            'rows': "3",
            'class': 'message-input',
            'placeholder': 'Ваше сообщение'
        })
    )
    username = CharField(
        max_length=50,
        widget=TextInput(attrs={
            'id': 'username',
            'class': 'username-input',
            'placeholder': 'Ваше имя'
        })
    )
