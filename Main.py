"""
This python script will generate 
"""
import string
import PyUnit.convert as unit




class Beam:
    def __init__(self, length, LengthUnit, boundary_conditions=['Fixed','Fixed']):
        if boundary_conditions[0].lower() == "fixed":
            start_string = (f"//|\n"
                            f"//|\n"
                            f"//|\n")
        elif boundary_conditions[0].lower() == ""


        print(f"{'-'*length} \n"
              f"{boundary_conditions[0]}"
              f""
              f""
              f""
              f""
              f""
              f"{'-' *100}\n"
              f"-{' '*40}Creating your beam.{' '*39}-\n"
              f"{'-' *100}\n")
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
    boundary = ['fixed','fixed']
    #instantiate a beam.
    problem1 = Beam(bar_length, bar_units,boundary)
    #display Beam attributes
    problem1.definition()
    #modify Beam attributes
    problem1.length = 50
    problem1.LengthUnit = "ft"
    problem1.boundary_conditions = ["pinned", "fixed"]
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