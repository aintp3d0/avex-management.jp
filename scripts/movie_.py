from .base_ import base
from .eqmp_ import eqmp


def movie():
    title, url = base.avex_movie()
    for i in range(len(title)):
        m = eqmp(False, title[i])
        print(' + ', url[i])
        print(m)
