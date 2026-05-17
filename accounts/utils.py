def is_gestor_portfolio(user):
    return user.is_authenticated and user.groups.filter(name="gestor_portfolio").exists()