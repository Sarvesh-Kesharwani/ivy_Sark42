# def if_exp(cond, if_true, if_false):
#   return if_true() if cond else if_false()


def if_else(cond, body_fn, orelse_fn, vars):
    # back-compatibility
    if not callable(cond):
        cond = bool(cond)
    if isinstance(cond, bool):
        v = cond
        cond = lambda *_: v
    cond = cond(*vars)
    if cond:
        return body_fn(*vars)
    else:
        return orelse_fn(*vars)


def while_loop(test_fn, body_fn, vars):
    result = vars
    while test_fn(*result):
        result = body_fn(*result)
        if not isinstance(result, tuple):
            result = (result,)
    return result
