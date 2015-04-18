from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from models import posts
from models import datapack
from models import finaldata
from forms import dataform
from forms import finaldataform
#from django.template.context_processors import csrf
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def index(request):
    return render_to_response('index.html')

def form(request):
    return render_to_response('form.html')

def thanks(request):
    return render_to_response('thanks.html')

#def finalform3(request):
#    return render_to_response('finalform3.html')

def finalform4(request):
    return render_to_response('finalform4.html')

def bootstraptest(request):
    return render_to_response('bootstraptest.html')

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
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            school = form.cleaned_data['school']
            row = datapack(fname=fname,lname=lname,school=school)
            row.save()
            # redirect to a new URL:

            return HttpResponseRedirect('/thanks/', b)
        else:
            return HttpResponseNotFound('<h1>Error</h1>')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = dataform()

    #return render('submit_form')
    return render(request,'newform.html', {'form': form})

def finalform3(request): # TODO: *MUST REMOVE OTHER FINALFORM VIEW*
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        #form = {}
        form = finaldataform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            global b
            b = {}
            b.update(csrf(request))

            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            mname = form.cleaned_data['mname']
            dob = form.cleaned_data['dob']
            birthp = form.cleaned_data['birthp']
            gender = form.cleaned_data['gender']
            genderhide = form.cleaned_data['genderhide']  # possibly for the 'other' text input box that appears
            soc = form.cleaned_data['soc']
            school = form.cleaned_data['school']
            maddress = form.cleaned_data['maddress']
            maddress2 = form.cleaned_data['maddress2']
            maddresscity = form.cleaned_data['maddresscity']
            maddressstate = form.cleaned_data['maddressstate']
            saddress = form.cleaned_data['saddress']
            saddress2 = form.cleaned_data['saddress2']
            saddresscity = form.cleaned_data['saddresscity']
            saddressstate = form.cleaned_data['saddressstate']
            hphone = form.cleaned_data['hphone']
            unlisted = form.cleaned_data['unlisted']
            father = form.cleaned_data['father']
            mother = form.cleaned_data['mother']
            guardian = form.cleaned_data['guardian']
            fathername = form.cleaned_data['fathername']
            fatherwnum = form.cleaned_data['fatherwnum']
            fathercnum = form.cleaned_data['fathercnum']
            mothername = form.cleaned_data['mothername']
            motherwnum = form.cleaned_data['motherwnum']
            mothercnum = form.cleaned_data['mothercnum']

            row = finaldata(
                fname = fname,
                lname = lname,
                mname = mname,
                dob = dob,
                birthp = birthp,
                gender = gender,
                genderhide = genderhide,
                soc = soc,
                school = school,
                maddress = maddress,
                maddress2 = maddress2,
                maddresscity = maddresscity,
                maddressstate = maddressstate,
                saddress = saddress,
                saddress2 = saddress2,
                saddresscity = saddresscity,
                saddressstate = saddressstate,
                hphone = hphone,
                unlisted = unlisted,
                father = father,
                mother = mother,
                guardian = guardian,
                fathername = fathername,
                fatherwnum = fatherwnum,
                fathercnum = fathercnum,
                mothername = mothername,
                motherwnum = motherwnum,
                mothercnum = mothercnum
            )
            row.save()
            # redirect to a new URL:

            return HttpResponseRedirect('/thanks/', b)
        else:
            return HttpResponseNotFound(form.errors)


    # if a GET (or any other method) we'll create a blank form
    else:
        form = finaldataform()

    #return render('submit_form')
    return render(request,'finalform3.html', {'form': form})

