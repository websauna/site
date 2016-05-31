from websauna.system.http import Request


def my_view(request: Request):
    print(request.user)
    request.user.full