# A1W1A1 - Calculate distance for a athletics track
# Description: see README.md in this folder
# Deadline: 2027-01-08 23:59 (CET)

# Inputs
# should extract number from input
raw = input("Input the number of laps:")

# Processing
# L A P S : 0 7
# 0 1 2 3 4 5 6
laps = int(raw[6:])
distance_meters = laps * 400
distance_km = distance_meters * 0.001

# Outputs
print(f"Kilometers: {distance_km}, Meters: {distance_meters}")
print(f"Kilometers: {distance_km:.3f}, Meters: {distance_meters}")
