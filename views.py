from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .Processor_Codes.maincode import *
from django.shortcuts import render



def do_a_super_thing():
    compute = 0
    for i in range(10000):
        compute += i
    return compute

def index_old(request):
    h = do_a_super_thing()
    hmtl_synth()
    return HttpResponse(f"Hello,{h} world. You're at the polls index.")
def index(request):
    hmtl_synth()
    return render(request, 'index2.html')