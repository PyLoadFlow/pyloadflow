import numpy as np
from scipy.sparse import lil_matrix


class Allocator:
    """Mixin of PowerSystem to allocate the numpy/scipy arrays"""

    complex_dtype = np.complex128
    float_dtype = np.float64
    indexing_dtype = np.uint32

    def __init__(self, n: int):
        """
        Args:
            n (int): number of buses from the system
        """
        self.allocate_electric_params(n)

    def allocate_electric_params(self, n):
        """Creates the numpy/scipy arrays that will be used for all calculations (doesn't inititialices them)"""
        self.number_of_buses = n

        # allocate voltages with inicial values of 1
        self.bus_voltage_pu = np.empty(n, dtype=Allocator.complex_dtype)

        # allocate powers with inicial values of 0
        self.bus_programed_apparent_power = np.empty(n, dtype=Allocator.complex_dtype)

        # allocate admittances with inicial values of 0
        self.line_series_admittance_pu = lil_matrix((n, n), dtype=Allocator.complex_dtype)

        # V = E + jU
        self.bus_real_voltage_pu = self.bus_voltage_pu.real
        self.bus_imaginary_voltage_pu = self.bus_voltage_pu.imag

        # S = P + jQ
        self.bus_programed_real_power = self.bus_programed_apparent_power.real
        self.bus_programed_reactive_power = self.bus_programed_apparent_power.imag

        # Y = G + jβ
        self.line_series_conductance_pu = self.line_series_admittance_pu.real
        self.line_series_susceptance_pu = self.line_series_admittance_pu.imag
