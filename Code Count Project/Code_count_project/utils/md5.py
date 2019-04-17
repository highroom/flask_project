import hashlib
import settings


def md5(arg):
    hash = hashlib.md5(settings.Config.SALT)
    hash.update(bytes(arg, encoding='utf-8'))
    ret = hash.hexdigest()
    return ret
