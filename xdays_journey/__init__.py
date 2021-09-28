from datetime import date

PYCONJP_2021_DAY1 = date(2021, 10, 15)


def あと何日(the_day=PYCONJP_2021_DAY1):
    return the_day - date.today()
