class LogReqMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        method = request.method
        path = request.path
        print(f'[Middleware] {method} request made to {path}')

        response = self.get_response(request)
        return response
