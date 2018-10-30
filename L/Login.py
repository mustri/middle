
def cachehave(user, cache):
    isLogin = cache.get(user)
    print('isLogin:', isLogin)
    if isLogin is None:
        return False
    elif isLogin is 1:
        return True
