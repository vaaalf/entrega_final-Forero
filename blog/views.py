from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from blog.models import Entrada
from blog.forms import EntradaForm, ComentarioForm, BusquedaForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def home_view(request):
    return render(request, "blog/home.html")

def about_me_view(request):
    return render(request, "blog/about_me.html")

class ListaEntradaView(ListView):
    model = Entrada

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_busqueda"] = BusquedaForm(initial={"buscar":self.request.GET.get('buscar', '')})
        return context

    def get_queryset(self):
        queryset = super(ListaEntradaView, self).get_queryset().order_by("-fecha_creacion")
        buscar = self.request.GET.get('buscar', '')
        if buscar:
            queryset = queryset.filter(titulo__icontains=buscar)
        return queryset


class MiListaEntradaView(ListView):
    model = Entrada

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_my_view"] = True
        return context

    def get_queryset(self):
        queryset = super(MiListaEntradaView, self).get_queryset()
        queryset = queryset.filter(autor=self.request.user).order_by("-fecha_creacion")
        return queryset


class NuevaEntradaView(LoginRequiredMixin, CreateView):
    form_class = EntradaForm
    template_name = 'blog/form_entrada.html'
    success_url = reverse_lazy('entrada-list-mine')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class DetalleEntradaView(DetailView):
    model = Entrada
    template_name = 'blog/entrada_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        entrada = self.get_object(Entrada.objects.all())
        context["form_comentario"] = ComentarioForm(initial={'entrada': entrada})
        context["comentarios"] = entrada.comentarios_entrada.all().order_by("-fecha_creacion")
        return context
    

class EditarEntradaView(LoginRequiredMixin, UpdateView):
    model = Entrada
    form_class = EntradaForm
    template_name = 'blog/form_entrada.html'
    success_url = reverse_lazy('entrada-list-mine')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update_view"] = True
        return context

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
    def get_queryset(self):
        queryset = super(EditarEntradaView, self).get_queryset()
        queryset = queryset.filter(autor=self.request.user)
        return queryset


class BorrarEntradaView(LoginRequiredMixin, DeleteView):
    model = Entrada
    template_name = 'blog/form_entrada_delete.html'
    success_url = reverse_lazy('entrada-list-mine')

    def get_queryset(self):
        queryset = super(BorrarEntradaView, self).get_queryset()
        queryset = queryset.filter(autor=self.request.user)
        return queryset


class NuevoComentarioView(LoginRequiredMixin, CreateView):
    form_class = ComentarioForm
    template_name = 'blog/entrada_detail.html'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse("entrada-detail", kwargs={'pk': self.object.entrada.pk})