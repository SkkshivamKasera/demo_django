from django.shortcuts import render, redirect, HttpResponse
from vege.models import Receipe

def receipes(request):
    if request.method == "POST":
        data = request.POST

        receipe = data.get("receipe")
        desc = data.get("desc")
        image = request.FILES.get("image")

        Receipe.objects.create(
            receipe=receipe,
            desc=desc,
            image=image
        )

        return redirect("/")
    
    allReceipes = Receipe.objects.all()

    contex = {
        "receipes": allReceipes
    }

    return render(request, "receipes.html", contex)


def delete_receipe(request, id):
    querySet = Receipe.objects.get(id=id)
    querySet.delete()
    return redirect("/")