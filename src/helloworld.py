def hello():
    return "v1.0.0 world"


def world():
    return hello()


print(world())
