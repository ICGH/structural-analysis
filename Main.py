"""
This python script will generate 
"""
import string




class Beam:
    def __init__(self, length, LengthUnit, boundary_conditions=['Fixed','Fixed']):
        if boundary_conditions[0].lower() == "fixed_left" and boundary_conditions[1].lower() == "fixed_left":
            with open('Data/fixed_left', 'r') as f:
                start_index = 'simple_support,simple_support,<start>'
                end_index = 'simple_support,simple_support,<end>'
                f.seek(start_index)
                beam_string = f.read(end_index-start_index)
                print(beam_string)
        elif boundary_conditions[0].lower() == "pinned":
            with open('data/pinned', 'r') as f:
                beam_string = f.read()



        print(beam_string)
        self._length = length
        self._LengthUnit = LengthUnit
        self._BCend1 = boundary_conditions[0]
        self._BCend2 = boundary_conditions[1]





    def definition(self):
        print(f"The current length of beam is {self._length} {self._LengthUnit} and the beam is {self._BCend1} on one end and {self._BCend2} on the other")

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        self._length = length

    @property
    def LengthUnit(self):
        return self._LengthUnit

    @LengthUnit.setter
    def LengthUnit(self, LengthUnit):
        self._LengthUnit = LengthUnit

    @property
    def boundary_conditions(self):
        return [self._BCend1, self._BCend2]

    @boundary_conditions.setter
    def boundary_conditions(self, boundary_conditions):
        self._BCend1 = boundary_conditions[0]
        self._BCend2 = boundary_conditions[1]







    class CrossSection:
        def __init__(self, shape, dimensions):
            self._shape = shape
            for dim in dimensions:
                for variable in  [f"dim_{i}" for i in string.ascii_uppercase[:len(dim)]]:
                    self._variable = dim

            self.dim_A = dimensions[0]
            self.dim_A_units = dimensions[1]

        @property
        def shape(self):
            return self.shape

        @shape.setter
        def shape(self, shape):
            if shape.upper() == "CIRCLE":
                radius = input(f"What is the radius of the {shape}? ")
                self._Dim_A = radius
                units = input(f"What is the units of the radius {radius}? ")
                self._Dim_A = radius

        @property
        def dimensions(self):
            # do something
            return self._dimensions




def main():
    #define inputs for BEAM class
    bar_length = 10
    bar_units = "in"
    boundary = ['fixed_left','fixed_left']
    #instantiate a beam.
    problem1 = Beam(bar_length, bar_units,boundary)
    #display Beam attributes
    problem1.definition()
    #modify Beam attributes
    problem1.length = 50
    problem1.LengthUnit = "ft"
    problem1.boundary_conditions = ["pinned", "fixed_left"]
    # display Beam attributes
    problem1.definition()
"""
    '''
    cross = "circle"
    dims = [5, "in"]
    problem1.CrossSection.shape(cross)
    problem1.CrossSection.dimensions(dims)
    '''
    print(f"The following shape: {problem1.CrossSection.shape} \n"
          f"with the following dimenions. {problem1.CrossSection.dimensions}")

    #problem1.CrossSection.shape = 'circle'
    #a = problem1.CrossSection.shape
"""


if __name__ == '__main__':
    main()