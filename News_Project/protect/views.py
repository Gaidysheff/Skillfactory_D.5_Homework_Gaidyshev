from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin



class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name = 'authors').exists()
        return context







    # def handle_no_permission(self):
    #     if self.raise_exception or self.request.user.is_authenticated:
    #         raise PermissionDenied(self.get_permission_denied_message())
    #     return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())


