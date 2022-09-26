from dataclasses import fields
from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto

class ContatoForm(forms.Form):
     nome = forms.CharField(label = 'Nome', max_length=100, min_length=1)
     email = forms.CharField(label = 'Email', max_length=100, min_length=1)
     assunto = forms.CharField(label = 'Assunto', max_length=100, min_length=1)
     mensagem = forms.CharField(label = 'Mensagem', widget=forms.Textarea(), min_length=1)
     
     def send_mail(self):
          nome = self.cleaned_data['nome']
          email = self.cleaned_data['email']
          assunto = self.cleaned_data['assunto']
          mensagem = self.cleaned_data['mensagem']
          
          conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'
          mail = EmailMessage(
               subject='E-mail enviado pelo sistema django2',
               body=conteudo,
               from_email='contato@seudominio.com.br',
               to=['email@dominio.com.br'],
               headers={'Reply-To': email}
          )
          mail.send()
          
class ProdutoModelForm(forms.ModelForm):
     class Meta:
          model = Produto
          fields = ['nome', 'preco', 'estoque', 'imagem']