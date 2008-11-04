from django.conf import settings

def site_info(request):
    """
    Adds site-specific meta information to the context
    
    To employ, add site_info reference to your project settings 
    TEMPLATE_CONTEXT_PROCESSORS.
    
    """
    
    SITE_NAME = getattr(settings, 'SITE_NAME', None)
    SITE_DOMAIN = getattr(settings, 'SITE_DOMAIN', None)
    SITE_URL = getattr(settings, 'SITE_URL', None)
    
    return {
        'SITE_NAME': SITE_NAME,
        'SITE_DOMAIN': SITE_DOMAIN,
        'SITE_URL': SITE_URL,
    }

