import time

class LogReqMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        method = request.method
        path = request.path
        print(f'[Middleware] {method} request made to {path}')

        response = self.get_response(request)
        return response


class RequestTimeLogging:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_timer = time.time()
        end_timer = time.time()
        execution_time = end_timer-start_timer
        print(f' time taken to execute  : {execution_time:6f}s')

        response = self.get_response(request)
        return response