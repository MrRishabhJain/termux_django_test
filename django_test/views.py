from django.http import JsonResponse


def testing(req):
    print(req)
    return JsonResponse({'first': 'Rishabh', 'last': 'Jain', 'age': 24 })
