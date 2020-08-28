from django.shortcuts import render
from django.shortcuts import redirect


def redirect_to_admin(request):
    return redirect('/admin')   