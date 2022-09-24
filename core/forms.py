from django import forms

class ContatoForm(forms.Form):
     nome = forms.CharField(label = 'Nome', max_length=100, min_length=1)
     email = forms.CharField(label = 'Email', max_length=100, min_length=1)
     assunto = forms.CharField(label = 'Assunto', max_length=100, min_length=1)
     mensagem = forms.CharField(label = 'Mensagem', widget=forms.Textarea(), min_length=1)