import json
from django.http import HttpResponse


def greeting_response(request):
    greeting = {
        "Hello from post platform": "Welcome",
        "api-path": [
            '.../api/posts',
            '.../api/comments'
        ]
    }
    dump = json.dumps(greeting)
    return HttpResponse(dump, content_type='application/json')
