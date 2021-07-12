from django.shortcuts import render
from haystack.query import SearchQuerySet
import simplejson as json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

def results(request):
    query = request.GET.get('search')
    sqs = SearchQuerySet().filter(title=query)
    paginator = Paginator(sqs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'query':query,
        'results':page_obj,  
    }
    return render(request, 'search/search-results.html', context)

@csrf_exempt
def autocomplete(request):
    sqs = SearchQuerySet().filter(content_auto=request.POST.get('query', ''))[:10]
    html = make_json_html(sqs)
    the_data = {
        "success": True,
        "html": html,
    }
    return JsonResponse(the_data)

def make_json_html(sqs):
    html = ""
    for result in sqs:
        html += "<li>\n\t<a href=\"" + result.object.get_absolute_url() + "\" class=\"search-results-item\">\n\t\n\t<div class=\"content\">\n\t<p class=\"title\">" + result.object.title + "</p>\n\t\n\t</div>\n\t</a>\n</li>\n"
    return html