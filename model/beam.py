from .section import Section



class Beam():
    '''
    Docs here
    '''

    # constructor
    def __init__(self, name: str):
        self._name = name

        self._number: int = 0

        self._section: Section | None = None
    
    def print_name(self) -> None:
        '''print the name'''
        print(self._name)

    def get_name(self) -> str:
        return self._name


if __name__ == "__main__":
    # do something

    beam_name = "Beam1"
    beam = Beam(beam_name)
    beam.print_name()
    name: str = beam.get_name()

    beam._number = 55  # bad practice - we need getter/setter
    beam._section = Section("100x200timber")
