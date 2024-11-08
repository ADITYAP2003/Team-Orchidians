import random

# Function to generate random vehicle counts and simulate traffic light control
def control_traffic():
    # Random vehicle count for each road (cross-sectional 4-way intersection)
    road_1 = random.randint(5, 100)  # Random count between 5 and 100 vehicles
    road_2 = random.randint(5, 100)
    road_3 = random.randint(5, 100)
    road_4 = random.randint(5, 100)

    # Store vehicle counts in a dictionary for reference
    vehicle_counts = {'Road 1': road_1, 'Road 2': road_2, 'Road 3': road_3, 'Road 4': road_4}

    # Calculate average vehicle count
    average_count = sum(vehicle_counts.values()) / 4

    # Define thresholds (30% higher or lower than average)
    upper_threshold = average_count * 1.30
    lower_threshold = average_count * 0.70

    print("Vehicle Counts: ", vehicle_counts)
    print(f"Average Vehicle Count: {average_count:.2f}")
    print(f"Upper Threshold: {upper_threshold:.2f}")
    print(f"Lower Threshold: {lower_threshold:.2f}\n")

    # Check which road exceeds the upper threshold and extend green signal duration
    for road, count in vehicle_counts.items():
        if count >= upper_threshold:
            print(f"{road} has exceeded the upper threshold with {count} vehicles. Turning signal GREEN for longer.")
        else:
            print(f"{road} is within normal range with {count} vehicles.")

# Simulate traffic control
control_traffic()
