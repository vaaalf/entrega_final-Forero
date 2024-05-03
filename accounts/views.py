from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Perfil
from accounts.forms import PerfilForm


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class DetallePerfil(LoginRequiredMixin, DetailView):
    model = Perfil
    template_name = "registration/perfil_detail.html"

    def get_object(self):
        # Para no tener el id en la url creamos el perfil o lo traemos directamente
        perfil = Perfil.objects.filter(user=self.request.user).first()
        if not perfil:
            perfil = Perfil(user=self.request.user)
            perfil.save()
        return perfil


class EditarPerfil(LoginRequiredMixin, UpdateView):
    form_class = PerfilForm
    success_url = reverse_lazy("profile-detail")
    template_name = "registration/form_perfil.html"

    def get_initial(self):
        return { 'email': self.request.user.email}

    def get_object(self):
        # Para no tener el id en la url creamos el perfil o lo traemos directamente
        perfil = Perfil.objects.filter(user=self.request.user).first()
        if not perfil:
            perfil = Perfil(user=self.request.user)
            perfil.save()
        return perfil

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        user = self.request.user
        user.email = email
        user.save()
        return super().form_valid(form)