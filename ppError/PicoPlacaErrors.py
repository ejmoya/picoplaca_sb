
class PicoPlacaError(ValueError):
    """
    Pico placa exception:
    This throws when the license plate number not abailability for run in the day provided.
    """
    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}


# try:
#     raise PicoPlacaError("Value must be within 1 and 10.")
# except PicoPlacaError as e:
#     print("CustomValueError Exception!", e.strerror)
