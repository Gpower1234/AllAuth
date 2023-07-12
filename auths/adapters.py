
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def get_login_url(self, request, **kwargs):
        if kwargs['provider'] == 'google':
            return 'account/google_login.html'
        elif kwargs['provider'] == 'facebook':
            return 'account/facebook_login.html'
        else:
            return super().get_login_url(request, **kwargs)

'''
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter

class CustomGoogleAdapter(GoogleOAuth2Adapter):
    login_template = 'custom_auth/google_login.html'

class CustomFacebookAdapter(FacebookOAuth2Adapter):
    login_template = 'custom_auth/facebook_login.html'



from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def get_connect_redirect_url(self, request, socialaccount):
        # Customize the redirect URL after successfully connecting the social account
        return '/custom-redirect-url'
    
    def get_login_redirect_url(self, request):
        # Customize the redirect URL after successful login
        return '/custom-login-redirect-url'
    
    def get_login_url(self, request, **kwargs):
        # Override the template name for Google and Facebooklogin pages
        if Kwargs['provider'] == 'google':
            return 'socialaccount/google_login.html'
        elif Kwargs['provider'] == 'facebook':
            return 'socialaccount/facebook_login.html'
        else:
            return super().get_login_url(request, **kwargs)
'''