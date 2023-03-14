import openmdao.api as om

'''SETTING UP MODEL/INTERFACE'''


class FWOptimise(om.ExternalCodeComp):
    def _init_(self):
        # Intputs to be passed to FAST from python
        """add inputs here: Column Radius, Height, Mass, Tower Height, Column Seperation"""
        self.add_input('Col_R', val=0.0)
        self.add_input('H', val=0.0)
        self.add_input('m', val=0.0)
        self.add_input('Tow_H', val=0.0)
        self.add_input('Col_Sep', val=0.0)

        # Outputs, to be extracted from the FAST output file
        '''add outputs here: Sway, Surge, Heave, Roll, Pitch, Yaw'''
        self.add_output('B1Sway', val=0.0)  # PtfmSway
        self.add_output('B1Surge', val=0.0)  # PtfmSurge
        self.add_output('B1Heave', val=0.0)  # PtfmHeave
        self.add_output('B1Roll', val=0.0)  # PtfmRoll
        self.add_output('B1Pitch', val=0.0)  # PtfmPitch
        self.add_output('B1Yaw', val=0.0)  # PtfmYaw

        # Specifying pre-existing input & output files
        self.input_file = ''  # OpenFast input file here
        self.output_file = 'openFAST_output.dat'

        # This calls an external python scfipt containing the Python-FAST interface
        self.options['command'] = ('FAST_Python_interface.py {} {}').format(
            self.input_file, self.output_file)

    def run(self, inputs, outputs):
        Col_R = inputs['Col_R']
        H = inputs['H']
        m = inputs['m']
        Tow_H = inputs['Tow_H']
        Col_Sep = inputs['Col_Sep']

        with open(self.input_file, 'w') as input_file:
            input_file.write('%.16f\n%.16f\n%.16f\n%.16f\n%.16f\n' % (Col_R, H, m, Tow_H, Col_Sep))

        super().run(inputs, outputs)

        with open(self.output_file, 'r') as output_file:
            output_file.read()
