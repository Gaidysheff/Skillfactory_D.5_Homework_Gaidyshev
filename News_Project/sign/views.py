from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/')


# from django.contrib.auth.decorators import login_required, permission_required
#
# @login_required
# @permission_required('newsapp.change_post', raise_exception=True)
# def change_post(request):
#     if not request.user.has_perm('newsapp.change_post'):
#         raise PermissionDenied
#     #Код для добавления нового поста
#     return render(request)

