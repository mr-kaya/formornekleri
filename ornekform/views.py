from django.shortcuts import render, redirect #redirect ifadesi şuan için tek html sayfasında çalışmak için yapılmıştır.
from django.http import HttpResponseRedirect,HttpResponse
from ornekform.models import OrnekFormDatabase



def index(request):
    databaseGosterListe = OrnekFormDatabase.objects.all() #HTML'de veritabanına girilen girdileri liste halinde göstermek için kullanılır.

    return render(request,"ornekform/index.html", {"databaseGosterListe":databaseGosterListe}) #Redirect kullanmamın amacını from kısmında belirttim.

def ornekform(request):
    if request.method == "POST": #html ifadesinde çağırılan kısmın method ifadesi POST ise;
        name = request.POST.get("name") #html ifadesindeki <input> 'lardaki name alanlarına bakar.
        email = request.POST.get("email")
        service = request.POST.get("service")
        budget = request.POST.get("budget")
        message = request.POST.get("message")

        newOrnekForm = OrnekFormDatabase(name=name, email=email, service=service, budget=budget, message=message)
        newOrnekForm.save()

        return redirect("/ornekform")
        