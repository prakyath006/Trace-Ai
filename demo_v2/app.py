from utils import calculate_average

def run_app():
    data = [10, 20, 30]
    avg = calculate_average(data)
    print(f"Average: {avg}")
    
    # Bug here: Empty list passed
    empty_data = []
    print("Attempting to calculate average for empty data...")
    avg_empty = calculate_average(empty_data)
    print(f"Empty Average: {avg_empty}")

if __name__ == "__main__":
    run_app()
