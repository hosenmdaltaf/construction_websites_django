from projectapp.models import Category


def get_category_context(request):
    categories = Category.objects.all()

    return {
        'categories': categories,
    }

