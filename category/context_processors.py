from .models import Category

def menu_links(request):
    """Context processor to add categories links to the template context."""
    links = Category.objects.all()
    return dict(links=links)
