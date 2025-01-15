class RequestLoggingMiddleware:
    """
    Middleware para registrar el path y método HTTP de cada solicitud.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Capturar el path y el método HTTP
        path = request.path
        method = request.method

        # Registrar la información
        print(f"Path solicitado: {path} | Método HTTP: {method}")
        if str(path).startswith("/apis/"):
            request.path_info = "/apis/"


        # Continuar con la cadena de middleware
        response = self.get_response(request)
        return response