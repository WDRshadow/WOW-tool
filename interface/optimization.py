import openmdao.api as om

'''SETTING UP MODEL/INTERFACE'''


class FWOptimise(om.ExternalCodeComp):
    def _init_(self):
        # Intputs to be passed to FAST from python
        '''add inputs here: Column Radius, Height, Mass, Tower Height, Column Seperation'''
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
        self.input_file =  # OpenFast input file here
        self.output_file = 'openFAST_output.dat'

        # This calls an external python scfipt containing the Python-FAST interface
        self.options['command'] = ('FAST_Python_interface.py {} {}').format(
            self.input_file, self.output_file)

    def run(self, inputs, outputs):
        Col_R = inputs['Col_R']
        H = inputs['H']
        m = inputs['m']
        Tow_H = ['Tow_H']
        Col_Sep = ['Col_Sep']

        with open(self.input_file, 'w') as input_file:
            input_file.write('%.16f\n%.16f\n%.16f\n%.16f\n%.16f\n' % (Col_R, H, m, Tow_H, Col_Sep))

        super().run(inputs, outputs)

        with open(self.output_file, 'r') as output_file:
            output_file.read()

'''OPTIMISER'''

prob = om.Problem
prob.model = model

#
model.add_subsytem('semi_sub',FWOptimise(),promotes_inputs=['Col_R','H','m','Tow_H','Col_Sep'])

# Adding the design variables
model.add_design_var('Col_R' ,upper = ,lower = )
model.add_design_var('H' ,upper = ,lower = )
model.add_design_var('m' ,upper = ,lower = )
model.add_design_var('Tow_H' ,upper = ,lower = )
model.add_design_var('Col_Sep' ,upper = ,lower = )

# Adding the objective functions
model.add_objective('B1Sway')
model.add_objective('B1Surge')
model.add_objective('B1Heave')
model.add_objective('B1Roll')
model.add_objective('B1Pitch')
model.add_objective('B1Yaw')

#Setting the optimisation algorithm to use, in this case a differential evolutionary algorithm
prob.driver = om.DifferentialEvolutionDriver()
prob.driver.option['max_gen'] = 500
prob.driver.option['F'] = 0.5
prob.driver.option['Pc'] = 0.5


prob.setup()
prob.run_driver()

# Returning variable outputs at the point optmiser completes
print(prob.get_val('semi_sub.Col_R'))
print(prob.get_val('semi_sub.H'))
print(prob.get_val('semi_sub.m'))
print(prob.get_val('semi_sub.Tow_H'))
print(prob.get_val('semi_sub.Col_Sep'))