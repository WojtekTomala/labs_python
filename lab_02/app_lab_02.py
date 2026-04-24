import multiprocessing
import sys

def calculate_total_of_powers(n):
    total = sum(n ** i for i in range(1, 101))
    return n, total


def main():
    try:
        start = int(input("Starting value: "))
        end = int(input("End value: "))
    except ValueError:
        print("Error: provided numbers are not valid.")
        sys.exit(1)

    if start < 0 or end < start:
        print("Error: provided numbers range is no valid. Starting value must be greater than 0. End value must be greater than or equal to start value.")
        sys.exit(1)

    numbers_range = range(start, end + 1)

    # Setting cores_count based on used cpu.
    cores_count = multiprocessing.cpu_count()
    print(f"\nCores & processes: {cores_count}")

    with multiprocessing.Pool(processes=cores_count) as pool:
        # pool.map() divides the range to smaller parts to divide it between processes
        results = pool.map(calculate_total_of_powers, numbers_range)

    print("\n--- Results ---")
    for n, total in results:
        # Shorten values based on digit length:
        n_length = len(str(total))
        if n_length <= 50:
            print(f"Number {n}: {total}")
        else:
            start_str = str(total)[:10]
            end_str = str(total)[-10:]
            print(f"Number {n}: {start_str}...{end_str} (Full number length: {n_length})")


if __name__ == '__main__':
    main()