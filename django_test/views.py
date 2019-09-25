from django.http import JsonResponse
import git
import os

# g = git.cmd.Git(git_dir)
# g.pull()

def testing(req):
    print(req)
    return JsonResponse({'first': 'Rishabh', 'last': 'Jain', 'age': 24, 'path': os.listdir('')})
