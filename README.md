# sPYce
Pseudo-SPICE Python Simulator

## Classes
### MetricScale
#### Abstract
I made this because I am constantly messing up my metric conversions, and I'm hoping that I can simply create a class structure so that I can be more confident with my circuit evaluation

Further, by automating tests on the class, I can ensure that this class method is reliable to be used by all circuit models, ensure consistency and uniformness across all the classes that I may implement

#### Usage
This class is made as a universal data structure to be used by these circuit models instead of ints or floats (although these are really just over glorified ints and floats)

If you have a value with a metric prefix, the class can be called with:

`Value  = MetricScale("10k")`

To access that value, you would call Value.f_Value:

`print(Value.i_Value)`

`$ 10000.0`

If a prefix is being specified, make sure it is a valid one, and is listed below:

`Valid Prefixes: T, G, M, k, h, d, c, m, u, n, p`

If you don't have a number with a metrix prefix, you can still call

`Value  = MetricScale(12.345)`

And you can still access the value by:

`print(Value.i_Value)`

`$ 12.345`

This class will automatically detect sig-figs and round accordingly upon creation.

### RCLowPassFilter
#### Abstract

A simple class which models the following circuit:

![alt text](https://github.com/RohitKochhar/python-circuit-models/blob/main/images/RCLowPass.png?raw=true)

#### Usage
##### Creation:

To create a lowpass filter with R=10kOhms and C=318nF

`RCLowPassFilter    = RCLowpassFilter(o_Resistance="10k", o_Capacitance="318n")`

Where:
    - o_Resistance and o_Capacitance are mandatory input fields that can be either a string specifying a float and metric scale pre-fix or simply a unitary float

Once created, the following properties of the circuit are accessible:
- Time Constant:        `RCLowPassFilter.f_Tau`
- Cut-off Frequency:    `RCLowPassFilter.f_CutOffFrequency`
- Damping co-efficient: `RCLowPassFilter.f_DampingCoefficient`
- Resonant Frequency:   `RCLowPassFilter.f_ResonantFrequency`