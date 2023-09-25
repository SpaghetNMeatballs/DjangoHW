from django.views import generic
from django.utils import timezone
from .models import UserExtended


# Create your views here.

class IndexView(generic.ListView):
    template_name = "user\\index.html"
    context_object_name = "latest_user_list"

    def get_queryset(self):
        return UserExtended.objects.filter(join_date__lte=timezone.now())


class DetailView(generic.DetailView):
    model = UserExtended
    template_name = "user\\detail.html"

    def get_queryset(self):
        return UserExtended.objects.filter(join_date__lte=timezone.now())