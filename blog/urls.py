from django.urls import path

from blog.views import home_view, about_me_view, ListaEntradaView, MiListaEntradaView, NuevaEntradaView , DetalleEntradaView, EditarEntradaView, BorrarEntradaView, NuevoComentarioView

urlpatterns = [
    path("", home_view, name="home"),
    path("about_me/", about_me_view, name="about_me"),
    path("pages/", ListaEntradaView.as_view(), name="entrada-list"),
    path("pages/mine/", MiListaEntradaView.as_view(), name="entrada-list-mine"),
    path("pages/create/", NuevaEntradaView.as_view(), name="entrada-create"),
    path("pages/detail/<int:pk>", DetalleEntradaView.as_view(), name="entrada-detail"),
    path("pages/update/<int:pk>", EditarEntradaView.as_view(), name="entrada-update"),
    path("pages/delete/<int:pk>", BorrarEntradaView.as_view(), name="entrada-delete"),
    path("comments/create/", NuevoComentarioView.as_view(), name="comentario-create"),
]