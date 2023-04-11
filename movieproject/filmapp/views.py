from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.template import context

from .forms import  filmform
from .models import Film


# Create your views here.
#def first(request):
 #  return  HttpResponse("you are in filmapp")
#def second(request):
 #  x=Film.objects.all()
  # context={
   #   'film_list':x
   #}
   #return render(request,"second.html",context)
#def third(request):
 #  y=Film.objects.all()
  # context={'cinema':y}
   #return render(request,"third.html",context)
#def detail(request,film_id):
 #  return HttpResponse("this is movie no %s" % film_id)
#def link1(request):
 # r=Film.objects.all()
 # return render(request,'link1.html',{'pict':r})
#def particular(request,film_id):
 #  t=Film.objects.get(id=film_id)
  # return render(request,'part.html',{'pan':t})
#def link2(request):
 #  p=Film.objects.all()
  # context={'pot':p}
   #return render(request,"link2.html",context)
#def stylin(request,film_id):
 #  q=Film.objects.get(id=film_id)
  # return render(request,'stylin.html',{'stylin':q})
#def link3(request):
 #  lot=Film.objects.all()
  # context={'lotus':lot}
   #return render(request,"link3.html",context)
def stylish(request,film_id):
   g=Film.objects.get(id=film_id)
   return render(request,'stylish.html',{'stylish':g})
def link4(request):
   sun=Film.objects.all()
   context={'flower':sun}
   return render(request,"link4.html",context)
def add(request):
   if request.method=='POST':
      name=request.POST.get('name',)
      genre=request.POST.get('genre',)
      year=request.POST.get('year',)
      img=request.FILES['img']
      film=Film(name=name,genre=genre,year=year,img=img)
      film.save()
   return render(request,"add.html")
def edit(request,id):
   film=Film.objects.get(id=id)
   form=filmform(request.POST or None,request.FILES,instance=film)
   if form.is_valid():
      form.save()
      return redirect('/')
   return render(request,'edit.html',{'form':form,'film':film})
def delete(request,id):
   if request.method=='POST':
      film=Film.objects.get(id=id)
      film.delete()
      return redirect('/')
   return render(request,'delete.html')
