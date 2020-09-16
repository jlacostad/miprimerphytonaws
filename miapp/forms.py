from django import forms
from django.core import validators

class FormArticle(forms.Form):

    title = forms.CharField (
        label = "Título",
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Mete el título',
                'class': 'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'El título es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9 ñ]*$', 'El título está mal formado', 'invalid title')
        ]
    )

    content = forms.CharField(
        label = "Contenido",
        widget=forms.Textarea,
        validators = [
            validators.MinLengthValidator(4, 'El contenido es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9 ñ]*$', 'El título está mal formado', 'invalid title'),
            validators.MaxLengthValidator(20, 'El contenido es demasiado largo'),
        ]
    )
    content.widget.attrs.update({
        'placeholder': 'Mete el contenido',
        'class': 'titulo_form_article',
        'id': 'contenido_form'
    })

    public_options = [
        (1, 'Si'),
        (0, 'No')

    ]

    public_options = [
        (1,'Si'),
        (0, 'No')
    ]

    public = forms.TypedChoiceField(
        label = "¿Publicado?",
        choices = public_options        
    )
