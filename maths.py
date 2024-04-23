from easy_trilateration.model import Circle, Trilateration
from easy_trilateration.least_squares import easy_least_squares
from easy_trilateration.graph import create_circle, draw

if __name__ == '__main__':
    # Create dummy data
    arr = [
        Circle(100, 100, 0, 50),  # Assuming z-coordinate is 0 for all circles
        Circle(100, 50, 0, 50),
        Circle(50, 50, 0, 50),
        Circle(50, 100, 0, 50)
    ]
    
    # Wrap the circles in a Trilateration object
    trilateration_data = Trilateration(arr)

    # Perform trilateration
    result, meta = easy_least_squares(trilateration_data)

    # Visualize results
    create_circle(result, target=True)
    draw(arr)
