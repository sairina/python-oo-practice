"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100

    """

    def __init__(self, start):
        "Starts counting up by one at start number"
        self.start = start
        self.original = start

    def __repr__(self):
        """Show representation"""
        return f"<SerialGenerator start = {self.original}, next = {self.start}>"
    
    def generate(self):
        "Adds one to start"

        initial_start = self.start

        if initial_start == self.start:
            self.start += 1
            return initial_start
        else:
            self.start += 1
            return self.start

    def reset(self):
        "Resets start to initial number"
        self.start = self.original

