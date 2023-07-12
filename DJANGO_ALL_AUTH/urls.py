"""DJANGO_ALL_AUTH URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from auths import views
from django.conf import settings
from django.conf.urls.static import static
from auths.views import *

#from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns
#from auths.adapters import CustomGoogleAdapter, CustomFacebookAdapter

app_name = 'auths'

#from auths.adapters import CustomSocialAccountAdapter

#google_urlpatterns = default_urlpatterns(CustomGoogleAdapter)
#facebook_urlpatterns = default_urlpatterns(CustomFacebookAdapter)

'''
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.oauth.views import OAuthLoginView, OAuthCallbackView
#from allauth.socialaccount.views import OAuth2Adapter, OAuthLoginView, OAuth2callbackView
#from auths.views import CustomSignupView
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    #path('accounts/google/login', socialaccount_login, {'provider_id': 'google'}, name='socialaccount_login'),
    #path('accounts/facebook/login', socialaccount_login, {'provider_id': 'facebook'}, name='socialaccount_login'),
    #path('/accounts/google/login/?process=login', views.google_login, name='google_login'),
    #path('accounts/facebook/login', views.facebook_login, name='facebook_login'),
    #path('accounts/google/login', views.google_login, name='google_login'),
    #path('accounts/facebook/login', views.facebook_login, name='facebook_login'),
    #path('accounts/signup/', CustomSignupView.as_view(), name='account_signup')
    #path('accounts/facebook/login', views.CustomFacebookLoginView(), name='facebook_login'),
    #path('accounts/facebook/login/callback/', views.CustomFacebookLoginView.callback_view(), name='facebook_call_back')
    #path('accounts/google/', include(google_urlpatterns)),
    #path('accounts/facebook/', include(facebook_urlpatterns))
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
