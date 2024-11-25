import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy variables
vehicle_count = ctrl.Antecedent(np.arange(0, 101, 1), 'vehicle_count')
waiting_time = ctrl.Antecedent(np.arange(0, 101, 1), 'waiting_time')
green_light_duration = ctrl.Consequent(np.arange(5, 61, 1), 'green_light_duration')

# Define membership functions
vehicle_count['low'] = fuzz.trimf(vehicle_count.universe, [0, 0, 50])
vehicle_count['medium'] = fuzz.trimf(vehicle_count.universe, [30, 50, 70])
vehicle_count['high'] = fuzz.trimf(vehicle_count.universe, [50, 100, 100])

waiting_time['short'] = fuzz.trimf(waiting_time.universe, [0, 0, 30])
waiting_time['medium'] = fuzz.trimf(waiting_time.universe, [20, 30, 40])
waiting_time['long'] = fuzz.trimf(waiting_time.universe, [30, 100, 100])

green_light_duration['short'] = fuzz.trimf(green_light_duration.universe, [5, 5, 15])
green_light_duration['medium'] = fuzz.trimf(green_light_duration.universe, [10, 20, 30])
green_light_duration['long'] = fuzz.trimf(green_light_duration.universe, [20, 60, 60])

# Define fuzzy rules
rule1 = ctrl.Rule(vehicle_count['low'] & waiting_time['short'], green_light_duration['short'])
rule2 = ctrl.Rule(vehicle_count['medium'] & waiting_time['medium'], green_light_duration['medium'])
rule3 = ctrl.Rule(vehicle_count['high'] & waiting_time['long'], green_light_duration['long'])

# Control system
traffic_control = ctrl.ControlSystem([rule1, rule2, rule3])
traffic_simulation = ctrl.ControlSystemSimulation(traffic_control)

# Simulate for different conditions
traffic_simulation.input['vehicle_count'] = 80
traffic_simulation.input['waiting_time'] = 35
traffic_simulation.compute()

print("Recommended Green Light Duration: " + str(traffic_simulation.output['green_light_duration']) + " seconds")
