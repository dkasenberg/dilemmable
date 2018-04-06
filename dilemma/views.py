from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib import messages
from main.models import Dilemma, DilemmaOption
from django.contrib.auth.decorators import login_required

@login_required
def new_dilemma(request):
    return render(request, 'dilemma/new.html', {})

def create_dilemma(request):
    if request.method == "POST":
        name = request.POST['dilemma_name']
        description = request.POST['dilemma_desc']
        dilemma = Dilemma(name=name, text=description)
        dilemma.save()

        i = 1
        num_options = 0
        next_str = 'dilemma_option' + str(i)
        while next_str in request.POST:
            if len(request.POST[next_str]) > 0:
                dilemma_option = DilemmaOption(dilemma = dilemma, text = request.POST[next_str]) # should I worry about order?
                dilemma_option.save()
                num_options +=1
            i += 1
            next_str = 'dilemma_option' + str(i)
        if num_options == 0:
            messages.error("Need at least one non-empty option.")

        return redirect('view', dilemma_id=dilemma.id)
    else:
        raise Http404

def view_dilemma(request, dilemma_id):
    dilemma = get_object_or_404(Dilemma, pk = dilemma_id)
    dilemma_options = DilemmaOption.objects.filter(dilemma=dilemma)

    if request.method == "POST":
        option_id = int(request.POST["dilemma_option"])
    return render(request, 'dilemma/view.html', {'dilemma': dilemma, 'dilemma_options': dilemma_options})
