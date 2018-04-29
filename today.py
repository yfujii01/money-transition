import datetime


def get_today():
    now = datetime.datetime.now()
    t = now.strftime("%Y-%m-%d")
    return t


if __name__ == '__main__':
    get_today()
