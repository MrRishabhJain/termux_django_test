from django.http import JsonResponse


def testing(req):
    print(req)
    return JsonResponse({'first': 'Manoj', 'last': 'Ganadhini'})