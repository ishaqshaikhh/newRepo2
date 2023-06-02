from django.shortcuts import render
from app.models import *
# Create your views here.
def index(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def submit(request):
    region = Region.objects.all()
    states = State.objects.all()
    divisions = Division.objects.all()
    districts = District.objects.all()
    return render(request, "submit.html",{"divisions":divisions,"districts":districts})

def view(request):
    return render(request, "view.html")


def submitted(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        resp = request.POST.get('zimmedari')
        division_n = request.POST.get('division')
        district_n = request.POST.get('district')
        print(type(division_n))
        alaqa = request.POST.get('alaqa')
        taqseem = request.POST.get('taqseem')
        wusool = request.POST.get('wusool')

        sim = request.POST.get('sim')
        sis = request.POST.get('sis')
        tim = request.POST.get('tim')
        tis = request.POST.get('tis')
        mea = request.POST.get('mea')
        yqmm = request.POST.get('yqmm')
        yqms = request.POST.get('yqms')
        iaim = request.POST.get('iaim')
        iais = request.POST.get('iais')
        hiram = request.POST.get('hiram')
        hiras = request.POST.get('hiras')

        # p1 = Report(division=division_n, district=district_n)
        # p1.save()
        Report(zimmedari=resp, zimmedar_name=name,alaqa=alaqa, taqseem=taqseem, wusool=wusool, islaheaamal_ijtima_maqam=iaim,islaheaamal_ijtima_shuraqa=iais,tahajjud_ijtima_maqam=tim,tahajjud_ijtima_shuraqa=tis,sehri_ijtima_maqam=sim,sehri_ijtima_shuraqa=sis,mehboob_e_attar=mea,yaumequfle_madinah_maqam=yqmm,yaumequfle_madinah_shuraqa=yqms,haftawar_ijtima_main_raat_guzarne_wale_Shuraqa=hiras,haftawar_ijtima_main_raat_guzarne_wale_maqam=hiram).save()

    return render(request, "home.html")