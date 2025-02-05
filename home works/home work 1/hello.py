import numpy as np


def main():
    numbers = np.array([i for i in range(10) if i >= 5]) + np.array(
        [i for i in range(10) if i < 5]
    )
    print("Hello from home-work-1!")
    print(numbers.sum())


if __name__ == "__main__":
    main()
