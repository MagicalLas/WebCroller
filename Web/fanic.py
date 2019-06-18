from sanic import Sanic
from sanic.response import json
from lazy.effect import pure, lazy
from lazy.ef_app import EfApp

app = Sanic()


def route(url, f):
    async def F(*params, **kParames):
        _params = [pure(i) for i in params]
        _kParams = dict()
        for i in kParames:
            _kParams[i] = pure(kParames[i])
        x = f(*_params, **_kParams).execute
        return x
    app.route(url)(F)


@lazy
def EffectApp():
    route('/', f)
    app.run(host="0.0.0.0", port=8000)
    return
