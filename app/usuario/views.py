from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse


from .forms import UserRegisterForm, UpdatePasswordForm
from .models import User

# Create your views here.

class UserRegisterView(FormView):
    template_name = 'usuario/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    def form_valid(self, form):
        
        usuario = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres=form.cleaned_data['nombres'],
            apellidos=form.cleaned_data['apellidos'],
            genero=form.cleaned_data['genero'],
            #--ESTA ES LA FORMA DE MANDAR LA IMAGEN DE PERFIL
            picture=form.data['picture']
           
           
        )

        return super(UserRegisterView, self).form_valid(form)
        


class UpdatePasswordView(FormView):
    template_name = 'usuario/update.html'
    form_class = UpdatePasswordForm
    success_url = '/'
    #success_url = reverse_lazy('users_app:user-login')
    #login_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            username=usuario.username,
            password=form.cleaned_data['password1']
        )
        
        if user:
           
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()
            print("AUTENTICADO")

        #logout(self.request)
        return super(UpdatePasswordView, self).form_valid(form)