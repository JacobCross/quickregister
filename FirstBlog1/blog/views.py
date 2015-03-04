from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from models import posts
from models import datapack
from forms import dataform
#from django.template.context_processors import csrf
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
#def home(request):
#    posts1 = posts.objects.all()[:10]
#    return render_to_response('index.html', {'posts' : posts1})

def form(request):
    return render_to_response('form.html')

def thanks(request):
    return render_to_response('thanks.html')

#def newform(request):
    #return render_to_response('newform.html')

def newform(request):
    #c = {}
    #c.update(csrf(request))

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        #form = {}
        form = dataform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            global b
            b = {}
            b.update(csrf(request))

            #b = RequestContext(request, form)
            #fname = form.cleaned_data['f_name']
            #lname = form.cleaned_data['l_name']
            #schoola = form.cleaned_data['school']
            #row = dataform(f_name=fname, lsname=lname, school=schoola)
            f_name = form.cleaned_data['fname']
            l_name = form.cleaned_data['lname']
            _school = form.cleaned_data['school']
            row = datapack(fname=f_name,lname=l_name,school=_school)
            row.save()
            # redirect to a new URL:

            # TODO: Figure out how to correctly redirect to a 'thanks' page (Not currently working).

            return HttpResponseRedirect('thanks/', b)
        else:
            return HttpResponseNotFound('<h1>Error</h1>')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = dataform()

    #return render('submit_form')
    return render(request,'newform.html', {'form': form})


