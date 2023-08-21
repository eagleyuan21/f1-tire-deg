import fastf1
from matplotlib import pyplot as plt
import fastf1.plotting

fastf1.plotting.setup_mpl()

session = fastf1.get_session(2023, 'Belgium', 'Q')

session.load()
print(session.weather_data)