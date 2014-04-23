

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
        text += str(x) + " "
        text += ping(x) + " "
        text += pong(x) + "\n"

    return text