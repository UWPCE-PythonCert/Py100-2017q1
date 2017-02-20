# Classes practice, based on "What are Objects and Classes" lesson from Treehouse.

class Vehicle():
    def __init__(self, **kwargs):
        self.size = kwargs.get('size', 'medium')
        self.wheels = kwargs.get('wheels', 4)
        self.horn_sound = kwargs.get('horn_sound', 'honk')
        self.seats = kwargs.get('seats', 5)
        self.seat_rows = kwargs.get('seat_rows', 2)
        self.gps = kwargs.get('gps', False)
        self.aux_port = kwargs.get('aux_port', False)
        self.cd_player = kwargs.get('cd_player', True)
        self.electric = kwargs.get('electric', False)

    def honk_horn(self):
        print(self.horn_sound.upper())

tesla = Vehicle(gps=True, aux_port=True, cd_player=False, electric=True)

tesla.honk_horn()