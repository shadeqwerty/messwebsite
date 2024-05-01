from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def do_a_super_thing():
    compute = 0
    for i in range(10000):
        compute += i
    return compute

@login_required
def index(request):
    h = do_a_super_thing()
    return HttpResponse(f"Hello,{h} world. You're at the polls index.")