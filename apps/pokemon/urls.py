from django.urls.conf import path
from .views import PokemonDetailsAPIView

urlpatterns = [
    path(r'<str:name>/', PokemonDetailsAPIView.as_view())
]