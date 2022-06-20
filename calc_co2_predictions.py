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
