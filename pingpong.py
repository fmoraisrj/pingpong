

def ping(num):
    if num % 3 == 0:
        return "ping"
    return ""

def pong(num):
    if num % 5 == 0:
        return "pong"
    return ""

def pingpong(how_much):
    text=""

    for x in range(1, how_much):
        is_ping = ping(x)
        is_pong = pong(x)

        ans = "%s" % (str(x))

        if is_ping or is_pong:
            ans = "%s %s" % (is_ping, is_pong)

        text += "%s\n" % ans.strip()
    return text