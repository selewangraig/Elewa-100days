import math

# Constants
pi = 22/7
cone_radius = 4.9
scoop1_radius = 5.6
scoop2_radius = 7.0

# Calculate cone volume
cone_volume = (1/3) * pi * cone_radius**2

# Calculate cone surface area
cone_height = math.sqrt(cone_radius**2 + cone_radius**2)
cone_surface_area = pi * cone_radius * (cone_radius + cone_height)

# Calculate scoop volumes
scoop1_volume = (4/3) * pi * scoop1_radius**3
scoop2_volume = (4/3) * pi * scoop2_radius**3

# Calculate total volume and surface area
total_volume = cone_volume + scoop1_volume + scoop2_volume
total_surface_area = cone_surface_area + (4 * pi * scoop1_radius**2) + (4 * pi * scoop2_radius**2)

# Display results
print("Cone Volume:", round(cone_volume,2))
print("Cone Surface Area:", round(cone_surface_area,2))
print("Total Volume:", round(total_volume,2))
print("Total Surface Area:", round(total_surface_area,2))