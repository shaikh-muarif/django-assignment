class Rectangle:
    def __init__(self, length: int, width: int):
        # Initialize the length and width of the rectangle
        self.length = length
        self.width = width

    def __iter__(self):
        # Yield the length and width as dictionaries
        yield {'length': self.length}
        yield {'width': self.width}


rect = Rectangle(10, 5)

# Iterate over the Rectangle instance
for dimension in rect:
    print(dimension)
