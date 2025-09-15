import os
from django import template
from django.templatetags.static import static
from django.conf import settings

register = template.Library()

@register.simple_tag
def webp_static(path):
    """
    Returns the WebP version of a static image if it exists,
    otherwise returns the original static path.
    Usage in template: {% webp_static 'images/banner.jpg' %}
    """
    original_path = os.path.join(settings.BASE_DIR, "static", path)
    webp_path = os.path.splitext(original_path)[0] + ".webp"

    if os.path.exists(webp_path):
        # Return webp static URL
        return static(os.path.splitext(path)[0] + ".webp")
    else:
        # Fallback to original
        return static(path)
