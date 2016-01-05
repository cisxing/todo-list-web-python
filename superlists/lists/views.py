from django.shortcuts import render
# Create your views here.
def home_page(request):
        return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text',''),
    })
    #we could say that
    #if request.method == 'POST':
    #return HttpResponse(request.POST[item_text])
    #but then we break other things
