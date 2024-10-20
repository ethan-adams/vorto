import sys

class Load:
    def __init__(self, id, pickup, dropoff):
        self.id = id
        self.pickup = pickup
        self.dropoff = dropoff

class Driver:
    def __init__(self):
        self.loads = []

    def take_load(self, load):
        self.loads.append(load)

def read_problem(file_path):
    loads = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:  # Skip the header line
            parts = line.split()
            load_id = int(parts[0])
            pickup = tuple(map(float, parts[1].strip('()').split(',')))
            dropoff = tuple(map(float, parts[2].strip('()').split(',')))
            loads.append(Load(load_id, pickup, dropoff))
    return loads

def solve_vrp(loads):
    drivers = [Driver() for _ in range(5)]  # Example: 5 drivers
    assigned_loads = set()  # Track assigned load IDs

    # Distribute loads among drivers
    for i, load in enumerate(loads):
        driver_index = i % len(drivers)  # Cycle through drivers
        drivers[driver_index].take_load(load)
        assigned_loads.add(load.id)

    # Ensure that all loads have been assigned
    if len(assigned_loads) != len(loads):
        print("Warning: Not all loads were assigned to a driver.")
        for load in loads:
            if load.id not in assigned_loads:
                print(f"Load {load.id} was not assigned to a driver.")
    
    # Final output for driver assignments
    for i, driver in enumerate(drivers):
        print(f"Driver {i + 1}: {[load.id for load in driver.loads]}")

def main(file_path):
    loads = read_problem(file_path)
    solve_vrp(loads)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 vorto.py <problem_file>")
        sys.exit(1)

    problem_file = sys.argv[1]
    main(problem_file)
