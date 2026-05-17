from .utils import is_gestor_portfolio

def gestor_portfolio(request):
    return {"is_gestor": is_gestor_portfolio(request.user)}