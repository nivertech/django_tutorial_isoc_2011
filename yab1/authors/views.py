from django.http import HttpResponse
from django.shortcuts import render_to_response
from yab1.authors.models import Author

def author_list(request):
    authors = Author.objects.all()
    return render_to_response(
        "author_list.html",
        {"authors": authors}
    )

def author_detail(request, author_id):
    #author = get_object_or_404(Author, id=author_id)
    author = Author.objects.get(id = author_id)
    return render_to_response(
        "author_detail.html",
        {"author": author}        
    )

# commented out - generate raw HTML without templates
"""
def author_list(request):
    authors = Author.objects.all()
    html = "<ol>\n"
    for author in authors:
        html += ("<li>%s</li>\n" % author)
    html += "</ol>\n" 
    return HttpResponse(html)
"""

