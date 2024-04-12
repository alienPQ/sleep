# -*- coding: utf-8 -*-
#
# twoneurons.py
#
# This file is part of NEST.
#
# Copyright (C) 2004 The NEST Initiative
#
# NEST is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# NEST is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NEST.  If not, see <http://www.gnu.org/licenses/>.

"""
Two neuron example
------------------

This script simulates two connected pre- and postsynaptic neurons.
The presynaptic neuron receives a constant external current,
and the membrane potential of both neurons are recorded.

See Also
~~~~~~~~

:doc:`one_neuron`

"""

###############################################################################
# First, we import all necessary modules for simulation, analysis and plotting.
# Additionally, we set the verbosity to suppress info messages and reset
# the kernel.

import matplotlib.pyplot as plt
import nest
import nest.voltage_trace

nest.set_verbosity("M_WARNING")
nest.ResetKernel()

###############################################################################
# Second, we create the two neurons and the recording device.

neuron_1 = nest.Create("iaf_psc_alpha")
neuron_2 = nest.Create("iaf_psc_alpha")
neuron_3 = nest.Create("iaf_psc_alpha")
voltmeter = nest.Create("voltmeter")

###############################################################################
# Third, we set the external current of neuron 1.

neuron_1.I_e = 6.0
#neuron_2.I_e = 6.0

###############################################################################
# Fourth, we connect neuron 1 to neuron 2.
# Then, we connect a voltmeter to the two neurons.
# To learn more about the previous steps, please check out the
# :doc:`one neuron example <one_neuron>`.

weight12 = 20.0
delay12 = 1.0
weight23 = 20.0
delay23 = 1.0
weight31 = -10.0
delay31 = 1.0

nest.Connect(neuron_1, neuron_2, syn_spec={"weight": weight12, "delay": delay12})
nest.Connect(neuron_2, neuron_3, syn_spec={"weight": weight23, "delay": delay23})
nest.Connect(neuron_3, neuron_1, syn_spec={"weight": weight31, "delay": delay31})

nest.Connect(voltmeter, neuron_1)
nest.Connect(voltmeter, neuron_2)
nest.Connect(voltmeter, neuron_3)

###############################################################################
# Now we simulate the network using ``Simulate``, which takes the
# desired simulation time in milliseconds.

nest.Simulate(1000.0)

###############################################################################
# Finally, we plot the neurons' membrane potential as a function of
# time.

nest.voltage_trace.from_device(voltmeter)
plt.show()
