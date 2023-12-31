# import the library
from pyloadflow import PowerSystem

# define a system
ps = PowerSystem(n=3)

# define the buses
ps.add_slack_bus(V=1.05)
ps.add_pq_bus(P=4, Q=2.5)
ps.add_pv_bus(P=2, V=1.04)

# connect them
ps.connect_buses_by_IEEE_id(1, 2, z=0.02 + 0.04j)
ps.connect_buses_by_IEEE_id(2, 3, z=0.0125 + 0.025j)
ps.connect_buses_by_IEEE_id(3, 1, z=0.01 + 0.03j)

# run
ps.run()

# Voilà!
print(ps.bus_voltage_pu)
print(ps.bus_apparent_power_pu)
