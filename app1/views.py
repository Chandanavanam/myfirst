from django.shortcuts import render

from django.http import HttpResponse


def chandana(request):
    return HttpResponse('chandana is a good girls')

def nagaraju(request):
    return HttpResponse('dad is my friend')
