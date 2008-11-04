from django.conf import settings

def site_info(request):
    """
    Adds site-specific meta information to the context
    
    """
    
    SITE_NAME = getattr(settings, 'SITE_NAME', None)
    SITE_DOMAIN = getattr(settings, 'SITE_DOMAIN', None)
    SITE_URL = getattr(settings, 'SITE_URL', None)
    
    return {
        'SITE_NAME': SITE_NAME,
        'SITE_DOMAIN': SITE_DOMAIN,
        'SITE_URL': SITE_URL,
    }

