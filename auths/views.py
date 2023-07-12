from django.shortcuts import render
#from allauth.socialaccount.views import (google_login as allauth_google_login, facebook_login as allauth_facebook_login)
#from allauth.socialaccount.views import OAuth2Adapter, OAuth2LoginView, OAuth2CallbackView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
#from allauth.socialaccount.views import OAuth2Adapter

from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.oauth.views import OAuthLoginView, OAuthCallbackView
from allauth.socialaccount.providers.oauth.client import OAuthError

from allauth.socialaccount.providers.oauth2.views import OAuth2Adapter
from .adapters import CustomSocialAccountAdapter

# Create your views here.

def home(request):
    user = request.user
    return render(request, 'home.html', {'user': user})

def socialaccount_login(request, provider_id):
    return render(request,  'account/socialaccount/login.html', {'provider_id': provider_id})



'''
def google_login(request):
    return render(request, 'custom_auth/google_login.html')

def facebook_login(request):
    return render(request, 'custom_auth/facebook_login.html')  


def google_login(request):
    return allauth_google_login(request, template_name='custom_auth/google_login.html')

def facebook_login(request):
    return allauth_facebook_login(request, template_name='custom_auth/facebook_login.html')



class CustomFacebookLoginView(OAuthLoginView):
    adapter_class = GoogleOAuth2Adapter

class CustomGoogleCallbackView(OAuthCallbackView):
    adapter_class = GoogleOAuth2Adapter

class CustomFacebookLoginView(OAuthLoginView):
    adapter_class = FacebookOAuth2Adapter

class CustomFacebookLoginView(OAuthCallbackView):
    adapter_class = FacebookOAuth2Adapter

'''