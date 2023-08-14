import fastf1
from matplotlib import pyplot as plt
import fastf1.plotting

fastf1.plotting.setup_mpl()

session = fastf1.get_session(2023, 'Belgium', 'Q')

session.load()
fast_leclerc = session.laps.pick_driver('VER').pick_fastest()
lec_car_data = fast_leclerc.get_car_data()
t = lec_car_data['Time']
vCar = lec_car_data['Speed']

# The rest is just plotting
fig, ax = plt.subplots()
ax.plot(t, vCar)
ax.set_xlabel('Time')
ax.set_ylabel('Speed [Km/h]')
ax.set_title('Verstappen Qualifying Speed')
ax.legend()
plt.show()