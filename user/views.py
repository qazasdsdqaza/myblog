from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/user_detail.html'
    slug_field = "username"
    slug_url_kwarg = "username"


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """ User can modify their personal information """
    model = User
    fields = ["nickname", "picture",
              "introduction", "job_title", "location",
              "person_url", "weibo", "zhihu", "github",
              "Linkedin"]
    template_name = 'users/user_form.html'
    success_message = _("更新成功")

    def get_success_url(self):
        """ Redirect to user's page After update success  """
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self, queryset=None):
        return self.request.user
