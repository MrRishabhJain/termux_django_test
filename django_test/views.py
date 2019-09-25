from django.http import JsonResponse
import git


def pull(req):
    g = git.cmd.Git('/data/data/com.termux/files/home/django_test/django_test')
    x = g.pull()
    return JsonResponse({'resp': str(x)})



def testing(req):
    print(req)
    return JsonResponse({'first': 'Rishabh', 'last': 'Jain', 'age': 24})
