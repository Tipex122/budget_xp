from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from categories.models import Category

from django.views.generic.base import TemplateView


def categories_main_page(request):
    template = get_template('categories/main_page.html')
    variables = (dict(head_title='Catégories', page_title='Bienvenue sur la page "Catégories"',
                      page_body='Endroit où vous pouvez visualiser les catégories TOTO! '
                                '<a href="/categories/About"> +++++ About +++++</a>'))
    output = template.render(variables)
    return HttpResponse(output)


def categories_page(request):
    cats = Category.objects.all()
    template = get_template('categories/categories_page.html')
    variables = Context({
        'head_title': 'Liste toutes les catégories',
        'page_title': 'Bienvenue sur la page listant toutes les Catégories !',
        'categories': cats
    })
    output = template.render(variables)
    return HttpResponse(output)


def categories_children_page(request, parent_name):
    cats = Category.objects.all()
    list_of_children = []
    for i in cats:
        if i.parent_name == parent_name:
            list_of_children.append(i)

    template = get_template('categories/categories_children_page.html')
    variables = Context({
        'categories': list_of_children
    })
    output = template.render(variables)
    return HttpResponse(output)


def categories_about(request):
    return HttpResponse("ABOUT: Site de gestion des catégories!")


class HomePage(TemplateView):
    """
    Because our needs are so simple, all we have to do is
    assign one value; template_name. The home.html file will be created
    in the next lesson.
    """
    template_name = 'categories/home.html'