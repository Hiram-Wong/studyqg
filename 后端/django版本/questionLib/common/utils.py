from django.http import JsonResponse


def json_response(status, msg, data=None):
    if data is None:
        data = []
    resp = {
        'status': status,
        'msg': msg,
        'data': data
    }
    print(JsonResponse(resp))

    return JsonResponse(resp)
