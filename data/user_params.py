 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}

        param_name1 = Button(description='random_seed', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.random_seed = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name2 = Button(description='alpha_diffusion_coefficient', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.alpha_diffusion_coefficient = FloatText(
          value=100000,
          step=10000,
          style=style, layout=widget_layout)

        param_name3 = Button(description='alpha_decay_rate', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.alpha_decay_rate = FloatText(
          value=62.5,
          step=1,
          style=style, layout=widget_layout)

        param_name4 = Button(description='beta_diffusion_coefficient', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.beta_diffusion_coefficient = FloatText(
          value=100000,
          step=10000,
          style=style, layout=widget_layout)

        param_name5 = Button(description='beta_decay_rate', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.beta_decay_rate = FloatText(
          value=62.5,
          step=1,
          style=style, layout=widget_layout)

        param_name6 = Button(description='a_cell_persistence_time', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.a_cell_persistence_time = FloatText(
          value=5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name7 = Button(description='a_cell_migration_speed', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.a_cell_migration_speed = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name8 = Button(description='a_cell_migration_bias', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.a_cell_migration_bias = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name9 = Button(description='a_cell_divide_time', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.a_cell_divide_time = FloatText(
          value=0.0003,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name10 = Button(description='a_cell_apoptosis_rate', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.a_cell_apoptosis_rate = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        param_name11 = Button(description='a_cell_alpha_uptake_rate', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.a_cell_alpha_uptake_rate = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name12 = Button(description='a_cell_alpha_secretion_rate', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.a_cell_alpha_secretion_rate = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name13 = Button(description='a_cell_alpha_saturation_density', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'lightgreen'

        self.a_cell_alpha_saturation_density = FloatText(
          value=5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name14 = Button(description='a_cell_beta_uptake_rate', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'tan'

        self.a_cell_beta_uptake_rate = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name15 = Button(description='a_cell_beta_secretion_rate', disabled=True, layout=name_button_layout)
        param_name15.style.button_color = 'lightgreen'

        self.a_cell_beta_secretion_rate = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name16 = Button(description='a_cell_beta_saturation_density', disabled=True, layout=name_button_layout)
        param_name16.style.button_color = 'tan'

        self.a_cell_beta_saturation_density = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name17 = Button(description='a_cell_motility_scale', disabled=True, layout=name_button_layout)
        param_name17.style.button_color = 'lightgreen'

        self.a_cell_motility_scale = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name18 = Button(description='b_cell_persistence_time', disabled=True, layout=name_button_layout)
        param_name18.style.button_color = 'tan'

        self.b_cell_persistence_time = FloatText(
          value=5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name19 = Button(description='b_cell_migration_speed', disabled=True, layout=name_button_layout)
        param_name19.style.button_color = 'lightgreen'

        self.b_cell_migration_speed = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name20 = Button(description='b_cell_migration_bias', disabled=True, layout=name_button_layout)
        param_name20.style.button_color = 'tan'

        self.b_cell_migration_bias = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name21 = Button(description='b_cell_divide_time', disabled=True, layout=name_button_layout)
        param_name21.style.button_color = 'lightgreen'

        self.b_cell_divide_time = FloatText(
          value=0.0003,
          step=1e-05,
          style=style, layout=widget_layout)

        param_name22 = Button(description='b_cell_apoptosis_rate', disabled=True, layout=name_button_layout)
        param_name22.style.button_color = 'tan'

        self.b_cell_apoptosis_rate = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        param_name23 = Button(description='b_cell_alpha_uptake_rate', disabled=True, layout=name_button_layout)
        param_name23.style.button_color = 'lightgreen'

        self.b_cell_alpha_uptake_rate = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name24 = Button(description='b_cell_alpha_secretion_rate', disabled=True, layout=name_button_layout)
        param_name24.style.button_color = 'tan'

        self.b_cell_alpha_secretion_rate = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name25 = Button(description='b_cell_alpha_saturation_density', disabled=True, layout=name_button_layout)
        param_name25.style.button_color = 'lightgreen'

        self.b_cell_alpha_saturation_density = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name26 = Button(description='b_cell_beta_uptake_rate', disabled=True, layout=name_button_layout)
        param_name26.style.button_color = 'tan'

        self.b_cell_beta_uptake_rate = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name27 = Button(description='b_cell_beta_secretion_rate', disabled=True, layout=name_button_layout)
        param_name27.style.button_color = 'lightgreen'

        self.b_cell_beta_secretion_rate = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name28 = Button(description='b_cell_beta_saturation_density', disabled=True, layout=name_button_layout)
        param_name28.style.button_color = 'tan'

        self.b_cell_beta_saturation_density = FloatText(
          value=5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name29 = Button(description='b_cell_apoptosis_scale', disabled=True, layout=name_button_layout)
        param_name29.style.button_color = 'lightgreen'

        self.b_cell_apoptosis_scale = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name30 = Button(description='b_cell_motility_scale', disabled=True, layout=name_button_layout)
        param_name30.style.button_color = 'tan'

        self.b_cell_motility_scale = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name31 = Button(description='cell_frac_A', disabled=True, layout=name_button_layout)
        param_name31.style.button_color = 'lightgreen'

        self.cell_frac_A = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name32 = Button(description='cell_spacing', disabled=True, layout=name_button_layout)
        param_name32.style.button_color = 'tan'

        self.cell_spacing = FloatText(
          value=0.95,
          step=0.1,
          style=style, layout=widget_layout)

        param_name33 = Button(description='a_number_of_cells', disabled=True, layout=name_button_layout)
        param_name33.style.button_color = 'lightgreen'

        self.a_number_of_cells = FloatText(
          value=938,
          step=10,
          style=style, layout=widget_layout)

        param_name34 = Button(description='b_number_of_cells', disabled=True, layout=name_button_layout)
        param_name34.style.button_color = 'tan'

        self.b_number_of_cells = FloatText(
          value=312,
          step=10,
          style=style, layout=widget_layout)

        param_name35 = Button(description='cell_x_min', disabled=True, layout=name_button_layout)
        param_name35.style.button_color = 'lightgreen'

        self.cell_x_min = FloatText(
          value=-250,
          step=10,
          style=style, layout=widget_layout)

        param_name36 = Button(description='cell_x_max', disabled=True, layout=name_button_layout)
        param_name36.style.button_color = 'tan'

        self.cell_x_max = FloatText(
          value=250,
          step=10,
          style=style, layout=widget_layout)

        param_name37 = Button(description='cell_y_min', disabled=True, layout=name_button_layout)
        param_name37.style.button_color = 'lightgreen'

        self.cell_y_min = FloatText(
          value=-250,
          step=10,
          style=style, layout=widget_layout)

        param_name38 = Button(description='cell_y_max', disabled=True, layout=name_button_layout)
        param_name38.style.button_color = 'tan'

        self.cell_y_max = FloatText(
          value=250,
          step=10,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='um^2/min', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='um^2/min', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'
        units_button7 = Button(description='um/min', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'
        units_button11 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'tan'
        units_button13 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'
        units_button14 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'
        units_button15 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'lightgreen'
        units_button16 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'tan'
        units_button17 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button17.style.button_color = 'lightgreen'
        units_button18 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button18.style.button_color = 'tan'
        units_button19 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button19.style.button_color = 'lightgreen'
        units_button20 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button20.style.button_color = 'tan'
        units_button21 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button21.style.button_color = 'lightgreen'
        units_button22 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button22.style.button_color = 'tan'
        units_button23 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button23.style.button_color = 'lightgreen'
        units_button24 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button24.style.button_color = 'tan'
        units_button25 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button25.style.button_color = 'lightgreen'
        units_button26 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button26.style.button_color = 'tan'
        units_button27 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button27.style.button_color = 'lightgreen'
        units_button28 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button28.style.button_color = 'tan'
        units_button29 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button29.style.button_color = 'lightgreen'
        units_button30 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button30.style.button_color = 'tan'
        units_button31 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button31.style.button_color = 'lightgreen'
        units_button32 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button32.style.button_color = 'tan'
        units_button33 = Button(description='number', disabled=True, layout=units_button_layout) 
        units_button33.style.button_color = 'lightgreen'
        units_button34 = Button(description='number', disabled=True, layout=units_button_layout) 
        units_button34.style.button_color = 'tan'
        units_button35 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button35.style.button_color = 'lightgreen'
        units_button36 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button36.style.button_color = 'tan'
        units_button37 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button37.style.button_color = 'lightgreen'
        units_button38 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button38.style.button_color = 'tan'

        desc_button1 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'
        desc_button15 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button15.style.button_color = 'lightgreen'
        desc_button16 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button16.style.button_color = 'tan'
        desc_button17 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button17.style.button_color = 'lightgreen'
        desc_button18 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button18.style.button_color = 'tan'
        desc_button19 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button19.style.button_color = 'lightgreen'
        desc_button20 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button20.style.button_color = 'tan'
        desc_button21 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button21.style.button_color = 'lightgreen'
        desc_button22 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button22.style.button_color = 'tan'
        desc_button23 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button23.style.button_color = 'lightgreen'
        desc_button24 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button24.style.button_color = 'tan'
        desc_button25 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button25.style.button_color = 'lightgreen'
        desc_button26 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button26.style.button_color = 'tan'
        desc_button27 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button27.style.button_color = 'lightgreen'
        desc_button28 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button28.style.button_color = 'tan'
        desc_button29 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button29.style.button_color = 'lightgreen'
        desc_button30 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button30.style.button_color = 'tan'
        desc_button31 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button31.style.button_color = 'lightgreen'
        desc_button32 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button32.style.button_color = 'tan'
        desc_button33 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button33.style.button_color = 'lightgreen'
        desc_button34 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button34.style.button_color = 'tan'
        desc_button35 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button35.style.button_color = 'lightgreen'
        desc_button36 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button36.style.button_color = 'tan'
        desc_button37 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button37.style.button_color = 'lightgreen'
        desc_button38 = Button(description='', disabled=True, layout=desc_button_layout) 
        desc_button38.style.button_color = 'tan'

        row1 = [param_name1, self.random_seed, units_button1, desc_button1] 
        row2 = [param_name2, self.alpha_diffusion_coefficient, units_button2, desc_button2] 
        row3 = [param_name3, self.alpha_decay_rate, units_button3, desc_button3] 
        row4 = [param_name4, self.beta_diffusion_coefficient, units_button4, desc_button4] 
        row5 = [param_name5, self.beta_decay_rate, units_button5, desc_button5] 
        row6 = [param_name6, self.a_cell_persistence_time, units_button6, desc_button6] 
        row7 = [param_name7, self.a_cell_migration_speed, units_button7, desc_button7] 
        row8 = [param_name8, self.a_cell_migration_bias, units_button8, desc_button8] 
        row9 = [param_name9, self.a_cell_divide_time, units_button9, desc_button9] 
        row10 = [param_name10, self.a_cell_apoptosis_rate, units_button10, desc_button10] 
        row11 = [param_name11, self.a_cell_alpha_uptake_rate, units_button11, desc_button11] 
        row12 = [param_name12, self.a_cell_alpha_secretion_rate, units_button12, desc_button12] 
        row13 = [param_name13, self.a_cell_alpha_saturation_density, units_button13, desc_button13] 
        row14 = [param_name14, self.a_cell_beta_uptake_rate, units_button14, desc_button14] 
        row15 = [param_name15, self.a_cell_beta_secretion_rate, units_button15, desc_button15] 
        row16 = [param_name16, self.a_cell_beta_saturation_density, units_button16, desc_button16] 
        row17 = [param_name17, self.a_cell_motility_scale, units_button17, desc_button17] 
        row18 = [param_name18, self.b_cell_persistence_time, units_button18, desc_button18] 
        row19 = [param_name19, self.b_cell_migration_speed, units_button19, desc_button19] 
        row20 = [param_name20, self.b_cell_migration_bias, units_button20, desc_button20] 
        row21 = [param_name21, self.b_cell_divide_time, units_button21, desc_button21] 
        row22 = [param_name22, self.b_cell_apoptosis_rate, units_button22, desc_button22] 
        row23 = [param_name23, self.b_cell_alpha_uptake_rate, units_button23, desc_button23] 
        row24 = [param_name24, self.b_cell_alpha_secretion_rate, units_button24, desc_button24] 
        row25 = [param_name25, self.b_cell_alpha_saturation_density, units_button25, desc_button25] 
        row26 = [param_name26, self.b_cell_beta_uptake_rate, units_button26, desc_button26] 
        row27 = [param_name27, self.b_cell_beta_secretion_rate, units_button27, desc_button27] 
        row28 = [param_name28, self.b_cell_beta_saturation_density, units_button28, desc_button28] 
        row29 = [param_name29, self.b_cell_apoptosis_scale, units_button29, desc_button29] 
        row30 = [param_name30, self.b_cell_motility_scale, units_button30, desc_button30] 
        row31 = [param_name31, self.cell_frac_A, units_button31, desc_button31] 
        row32 = [param_name32, self.cell_spacing, units_button32, desc_button32] 
        row33 = [param_name33, self.a_number_of_cells, units_button33, desc_button33] 
        row34 = [param_name34, self.b_number_of_cells, units_button34, desc_button34] 
        row35 = [param_name35, self.cell_x_min, units_button35, desc_button35] 
        row36 = [param_name36, self.cell_x_max, units_button36, desc_button36] 
        row37 = [param_name37, self.cell_y_min, units_button37, desc_button37] 
        row38 = [param_name38, self.cell_y_max, units_button38, desc_button38] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)
        box19 = Box(children=row19, layout=box_layout)
        box20 = Box(children=row20, layout=box_layout)
        box21 = Box(children=row21, layout=box_layout)
        box22 = Box(children=row22, layout=box_layout)
        box23 = Box(children=row23, layout=box_layout)
        box24 = Box(children=row24, layout=box_layout)
        box25 = Box(children=row25, layout=box_layout)
        box26 = Box(children=row26, layout=box_layout)
        box27 = Box(children=row27, layout=box_layout)
        box28 = Box(children=row28, layout=box_layout)
        box29 = Box(children=row29, layout=box_layout)
        box30 = Box(children=row30, layout=box_layout)
        box31 = Box(children=row31, layout=box_layout)
        box32 = Box(children=row32, layout=box_layout)
        box33 = Box(children=row33, layout=box_layout)
        box34 = Box(children=row34, layout=box_layout)
        box35 = Box(children=row35, layout=box_layout)
        box36 = Box(children=row36, layout=box_layout)
        box37 = Box(children=row37, layout=box_layout)
        box38 = Box(children=row38, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          box9,
          box10,
          box11,
          box12,
          box13,
          box14,
          box15,
          box16,
          box17,
          box18,
          box19,
          box20,
          box21,
          box22,
          box23,
          box24,
          box25,
          box26,
          box27,
          box28,
          box29,
          box30,
          box31,
          box32,
          box33,
          box34,
          box35,
          box36,
          box37,
          box38,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML
        self.random_seed.value = int(uep.find('.//random_seed').text)
        self.alpha_diffusion_coefficient.value = float(uep.find('.//alpha_diffusion_coefficient').text)
        self.alpha_decay_rate.value = float(uep.find('.//alpha_decay_rate').text)
        self.beta_diffusion_coefficient.value = float(uep.find('.//beta_diffusion_coefficient').text)
        self.beta_decay_rate.value = float(uep.find('.//beta_decay_rate').text)
        self.a_cell_persistence_time.value = float(uep.find('.//a_cell_persistence_time').text)
        self.a_cell_migration_speed.value = float(uep.find('.//a_cell_migration_speed').text)
        self.a_cell_migration_bias.value = float(uep.find('.//a_cell_migration_bias').text)
        self.a_cell_divide_time.value = float(uep.find('.//a_cell_divide_time').text)
        self.a_cell_apoptosis_rate.value = float(uep.find('.//a_cell_apoptosis_rate').text)
        self.a_cell_alpha_uptake_rate.value = float(uep.find('.//a_cell_alpha_uptake_rate').text)
        self.a_cell_alpha_secretion_rate.value = float(uep.find('.//a_cell_alpha_secretion_rate').text)
        self.a_cell_alpha_saturation_density.value = float(uep.find('.//a_cell_alpha_saturation_density').text)
        self.a_cell_beta_uptake_rate.value = float(uep.find('.//a_cell_beta_uptake_rate').text)
        self.a_cell_beta_secretion_rate.value = float(uep.find('.//a_cell_beta_secretion_rate').text)
        self.a_cell_beta_saturation_density.value = float(uep.find('.//a_cell_beta_saturation_density').text)
        self.a_cell_motility_scale.value = float(uep.find('.//a_cell_motility_scale').text)
        self.b_cell_persistence_time.value = float(uep.find('.//b_cell_persistence_time').text)
        self.b_cell_migration_speed.value = float(uep.find('.//b_cell_migration_speed').text)
        self.b_cell_migration_bias.value = float(uep.find('.//b_cell_migration_bias').text)
        self.b_cell_divide_time.value = float(uep.find('.//b_cell_divide_time').text)
        self.b_cell_apoptosis_rate.value = float(uep.find('.//b_cell_apoptosis_rate').text)
        self.b_cell_alpha_uptake_rate.value = float(uep.find('.//b_cell_alpha_uptake_rate').text)
        self.b_cell_alpha_secretion_rate.value = float(uep.find('.//b_cell_alpha_secretion_rate').text)
        self.b_cell_alpha_saturation_density.value = float(uep.find('.//b_cell_alpha_saturation_density').text)
        self.b_cell_beta_uptake_rate.value = float(uep.find('.//b_cell_beta_uptake_rate').text)
        self.b_cell_beta_secretion_rate.value = float(uep.find('.//b_cell_beta_secretion_rate').text)
        self.b_cell_beta_saturation_density.value = float(uep.find('.//b_cell_beta_saturation_density').text)
        self.b_cell_apoptosis_scale.value = float(uep.find('.//b_cell_apoptosis_scale').text)
        self.b_cell_motility_scale.value = float(uep.find('.//b_cell_motility_scale').text)
        self.cell_frac_A.value = float(uep.find('.//cell_frac_A').text)
        self.cell_spacing.value = float(uep.find('.//cell_spacing').text)
        self.a_number_of_cells.value = float(uep.find('.//a_number_of_cells').text)
        self.b_number_of_cells.value = float(uep.find('.//b_number_of_cells').text)
        self.cell_x_min.value = float(uep.find('.//cell_x_min').text)
        self.cell_x_max.value = float(uep.find('.//cell_x_max').text)
        self.cell_y_min.value = float(uep.find('.//cell_y_min').text)
        self.cell_y_max.value = float(uep.find('.//cell_y_max').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML 
        uep.find('.//random_seed').text = str(self.random_seed.value)
        uep.find('.//alpha_diffusion_coefficient').text = str(self.alpha_diffusion_coefficient.value)
        uep.find('.//alpha_decay_rate').text = str(self.alpha_decay_rate.value)
        uep.find('.//beta_diffusion_coefficient').text = str(self.beta_diffusion_coefficient.value)
        uep.find('.//beta_decay_rate').text = str(self.beta_decay_rate.value)
        uep.find('.//a_cell_persistence_time').text = str(self.a_cell_persistence_time.value)
        uep.find('.//a_cell_migration_speed').text = str(self.a_cell_migration_speed.value)
        uep.find('.//a_cell_migration_bias').text = str(self.a_cell_migration_bias.value)
        uep.find('.//a_cell_divide_time').text = str(self.a_cell_divide_time.value)
        uep.find('.//a_cell_apoptosis_rate').text = str(self.a_cell_apoptosis_rate.value)
        uep.find('.//a_cell_alpha_uptake_rate').text = str(self.a_cell_alpha_uptake_rate.value)
        uep.find('.//a_cell_alpha_secretion_rate').text = str(self.a_cell_alpha_secretion_rate.value)
        uep.find('.//a_cell_alpha_saturation_density').text = str(self.a_cell_alpha_saturation_density.value)
        uep.find('.//a_cell_beta_uptake_rate').text = str(self.a_cell_beta_uptake_rate.value)
        uep.find('.//a_cell_beta_secretion_rate').text = str(self.a_cell_beta_secretion_rate.value)
        uep.find('.//a_cell_beta_saturation_density').text = str(self.a_cell_beta_saturation_density.value)
        uep.find('.//a_cell_motility_scale').text = str(self.a_cell_motility_scale.value)
        uep.find('.//b_cell_persistence_time').text = str(self.b_cell_persistence_time.value)
        uep.find('.//b_cell_migration_speed').text = str(self.b_cell_migration_speed.value)
        uep.find('.//b_cell_migration_bias').text = str(self.b_cell_migration_bias.value)
        uep.find('.//b_cell_divide_time').text = str(self.b_cell_divide_time.value)
        uep.find('.//b_cell_apoptosis_rate').text = str(self.b_cell_apoptosis_rate.value)
        uep.find('.//b_cell_alpha_uptake_rate').text = str(self.b_cell_alpha_uptake_rate.value)
        uep.find('.//b_cell_alpha_secretion_rate').text = str(self.b_cell_alpha_secretion_rate.value)
        uep.find('.//b_cell_alpha_saturation_density').text = str(self.b_cell_alpha_saturation_density.value)
        uep.find('.//b_cell_beta_uptake_rate').text = str(self.b_cell_beta_uptake_rate.value)
        uep.find('.//b_cell_beta_secretion_rate').text = str(self.b_cell_beta_secretion_rate.value)
        uep.find('.//b_cell_beta_saturation_density').text = str(self.b_cell_beta_saturation_density.value)
        uep.find('.//b_cell_apoptosis_scale').text = str(self.b_cell_apoptosis_scale.value)
        uep.find('.//b_cell_motility_scale').text = str(self.b_cell_motility_scale.value)
        uep.find('.//cell_frac_A').text = str(self.cell_frac_A.value)
        uep.find('.//cell_spacing').text = str(self.cell_spacing.value)
        uep.find('.//a_number_of_cells').text = str(self.a_number_of_cells.value)
        uep.find('.//b_number_of_cells').text = str(self.b_number_of_cells.value)
        uep.find('.//cell_x_min').text = str(self.cell_x_min.value)
        uep.find('.//cell_x_max').text = str(self.cell_x_max.value)
        uep.find('.//cell_y_min').text = str(self.cell_y_min.value)
        uep.find('.//cell_y_max').text = str(self.cell_y_max.value)
