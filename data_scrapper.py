import fastf1
from matplotlib import pyplot as plt
import fastf1.plotting

fastf1.plotting.setup_mpl()


year = 2020

races = []
rounds = int(list(fastf1.get_event_schedule(year)[:]['RoundNumber'])[-1])

i = rounds
while i <= rounds:
    race = fastf1.get_event(year, i).get_race()
    race.load()
    i += 1
