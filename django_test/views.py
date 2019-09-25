from django.http import JsonResponse
import git
import os


def pull():
    g = git.cmd.Git('/data/data/com.termux/files/home/django_test/django_test/')
    x = g.pull()
    return JsonResponse({'resp': str(x)})



def testing(req):
    print(req)
    return JsonResponse({'first': 'Rishabh', 'last': 'Jain', 'age': 24, 'path': str(os.listdir(''))})
