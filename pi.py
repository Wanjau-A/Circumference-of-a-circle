PI = 3.142


def main():
    radius_circle = float(input("Please enter the radius of the circle: "))
    circumference_circle = compute_circumference(radius_circle)
    print(f"Circumference: {circumference_circle:.0f}cm")

def compute_circumference(radius_circle):
    circumference = PI * radius_circle * 2
    return circumference


if __name__ == "__main__":
    main()

