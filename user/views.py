from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout, password_reset_done, password_reset
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import JsonResponse

# from django.conf import settings as journificaviewsettings

# Create your views here.

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)


def signup(request):
    return render(request, 'signup.html')


def user_logout(request):
    logout(request)
    return redirect('index')

def password_reset_save(request):
    restpassword_email_send  = password_reset_done(request,template_name = "user/password_reset_done.html")
    return restpassword_email_send

def password_reset_submit(request):
    password_email = password_reset(request,template_name = "user/password_reset_form.html")
    if  password_email.status_code == 302 and request.POST.get("email", None) != None:
        emailpresent = get_user_model().objects.filter(email=request.POST.get("email", None))
        # if len(emailpresent) > 0:
        #     for emailexixst in emailpresent:
        #         s = SystemEmail(sender = journificaviewsettings.DEFAULT_FROM_EMAIL, recipient = emailexixst.email,
        #                         title = "Password reset on Dilemmable.com", mailid = '',
        #                         organization = None,
        #                         message_html = "<p><b>Password Rest</b></p>",
        #                         error = None)
        #         s.save()
        # else:
        #     s = SystemEmail(sender = journificaviewsettings.DEFAULT_FROM_EMAIL, recipient = request.POST.get("email", None),
        #                     title = "Password reset on Dilemmable.com", mailid = '',
        #                     organization = None,
        #                     message_html = "<p><b>Try password rest</b></p>",
        #                     error = "Noemail")
        #     s.save()
    return password_email

# # TODO: this is very confusing, admin form is actually user form
# @login_required
# def superuser(request):
#     dict = {}

#     if request.user.is_superuser:
#         if request.method == 'POST':
#             form = SystemAdminForm(request.POST)

#             if form.is_valid():
#                 admin = form.save(commit = False)
#                 # TODO: is_active was false by default, but then couldn't login with systemadmin account
#                 admin.is_active = True
#                 admin.save()
#                 SystemAdmin.objects.create(user = admin)
#                 dict ['message'] = 'system admin created.'
#         else:
#             form = SystemAdminForm()

#         dict ['form'] = form

#     return render(request, 'superuser.html', dict)


@login_required
def password_change_done(request):
    messages.info(request, 'Password change successful!')

    return redirect('index')
