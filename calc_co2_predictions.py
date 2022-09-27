from src.DigiTwin_CO2_SampleProject.main import run_predictions

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 importlib_resources.
    import importlib_resources as pkg_resources

import Resources as test_resources

with pkg_resources.path(test_resources, 'database_test.simultan') as r_path:
    project_file = str(r_path)


if __name__ == '__main__':
    run_predictions(project_file=project_file)




import numpy as np
from PySimultan import DataModel, TemplateParser


class MyWindow(object):
    def __init__(self, *args, **kwargs):
        self.gap_sensor = kwargs.get('gap_sensor')      # Sensor measuring the opening-width
        self.b = kwargs.get('b')                        # window width in m
        self.h = kwargs.get('h')                        # window height in m
        self.c_ref = kwargs.get('c_ref')                # Exchange coefficient in [m^0.5 / h * K^0.5]
        self.gap_width = kwargs.get('max_gap_width')    # max opening width in m

    def calc_volume_flow_rate(self, t_out, t_in):
        """
        Calculate the air volume flow rate over a window according to ¨ONORM 8110-3
        :param t_out: Outside temperature in °C
        :param t_in: Inside temperature in °C
        :return: volume_flow_rate over the window in m³/s
        """
        total_gap_width = self.gap_sensor.latest_measurement_value * self.gap_width
        a_eff = total_gap_width * (self.b + self.h)
        return 0.7 * self.c_ref * a_eff * np.sqrt(self.h) * np.sqrt(np.abs(t_in - t_out)) / 3600


template_file = 'my_template.yml'
# Create a template parser with a template-file:
template_parser = TemplateParser(template_filepath=template_file)
# add the MyWindow-class to the bases of the template parser. The created template-class
# 'Window' will then inherit from MyWindow:
template_parser.bases['Window'] = MyWindow
template_parser.create_template_classes()
# load the data model:
data_model = DataModel(project_path=project_file,
                       user_name='SomeUser',
                       password='UserPwd')
# Get the typed data model:
typed_data = data_model.get_typed_data(template_parser=template_parser)
# Get a 'Window'-instance from the data model:
loaded_window = template_parser.template_classes['Window'].cls_instances[0]
# Call the inherited method 'calc_volume_flow_rate':
loaded_window.calc_volume_flow_rate(-10, 20)
