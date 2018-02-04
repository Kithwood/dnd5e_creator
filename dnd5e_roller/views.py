from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dnd5e_roller.models import Attributes

@login_required
def index(request):
    attr = Attributes.objects.filter(user=request.user)
    if attr.count()  > 0:
        context = { 'attribs': attr[0] }
        return render(request, 'dnd5e_roller/attributes.html', context)
    else:    
        context= {}
        return render(request, 'dnd5e_roller/index.html', context)
    
def attributes(request):
    attribs = Attributes()
    attribs.user = request.user
    attribs.roll()
    attribs.save()
    # requires to be saved to db before can pass with context
    context={ 'attribs': attribs }
    return render(request, "dnd5e_roller/attributes.html", context)