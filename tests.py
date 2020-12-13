from passiveFilters.metricScale import MetricScale

# Metric scale object tests -------------------------------------
# Test the creation of a 10k object
print(f"Test #1: Integer Positive Base, Positive Exponent")
o_TenKObject    =   MetricScale("10k")
if o_TenKObject.f_Value != 10000:
    print(f"\tTest #1: Failed! Expected 10000 got {o_TenKObject.f_Value}")
else:
    print("Success!") 
del o_TenKObject

print(f"Test #2: Integer Negative Base, Positive Exponent")
o_TestObject    =   MetricScale("-27G")
f_Expected      = float(-27000000000)
if o_TestObject.f_Value != f_Expected:
    print(f"\tTest #1: Failed! Expected {f_Expected} got {o_TestObject.f_Value}")
else:
    print("Success!") 
del o_TestObject

print(f"Test #3: Integer Positive Base, Negative Exponent")
o_TestObject    =   MetricScale("19n")
f_Expected      = float(0.000000019)
if o_TestObject.f_Value != f_Expected:
    print("Success!") 
else:
    print("Success!") 
del o_TestObject

print(f"Test #4: Integer Negative Base, Negative Exponent")
o_TestObject    =   MetricScale("-24m")
f_Expected      = float(-0.024)
if o_TestObject.f_Value != f_Expected:
    print(f"\tTest #1: Failed! Expected {f_Expected} got {o_TestObject.f_Value}")
else:
    print("Success!") 
del o_TestObject

print(f"Test #5: float Positive Base, Positive Exponent")
o_TestObject    =   MetricScale("2.3M")
f_Expected      = float(2300000)
if o_TestObject.f_Value != f_Expected:
    print(f"\tTest #1: Failed! Expected {f_Expected} got {o_TestObject.f_Value}")
else:
    print("Success!") 
del o_TestObject

print(f"Test #6: float Negative Base, Positive Exponent")
o_TestObject    =   MetricScale("-2.1h")
f_Expected      = float(-210)
if o_TestObject.f_Value != f_Expected:
    print(f"\tTest #1: Failed! Expected {f_Expected} got {o_TestObject.f_Value}")
else:
    print("Success!") 
del o_TestObject

print(f"Test #7: float Positive Base, Negative Exponent")
o_TestObject    =   MetricScale("4.3u")
f_Expected      = float(0.0000043)
if o_TestObject.f_Value != f_Expected:
    print(f"\tTest #1: Failed! Expected {f_Expected} got {o_TestObject.f_Value}")
else:
    print("Success!") 
del o_TestObject

print(f"Test #8: Integer Negative Base, Negative Exponent")
o_TestObject    =   MetricScale("-1.00005p")
f_Expected      = float(-0.00000000000100005)
if o_TestObject.f_Value != f_Expected:
    print(f"\tTest #1: Failed! Expected {f_Expected} got {o_TestObject.f_Value}")
else:
    print("Success!") 
del o_TestObject

print(f"Test #9: Integer input, not string")
o_TestObject    =   MetricScale(1234321)
f_Expected      = float(1234321)
if o_TestObject.f_Value != f_Expected:
    print(f"\tTest #1: Failed! Expected {f_Expected} got {o_TestObject.f_Value}")
else:
    print("Success!") 
del o_TestObject

print(f"Test #10: float input, not string")
o_TestObject    =   MetricScale(105323.0)
f_Expected      = float(105323.0)
if o_TestObject.f_Value != f_Expected:
    print(f"\tTest #1: Failed! Expected {f_Expected} got {o_TestObject.f_Value}")
else:
    print("Success!") 
del o_TestObject


print(f"Test #11: negative float")
o_TestObject    =   MetricScale(-0.435240)
f_Expected      = float(-0.435240)
if o_TestObject.f_Value != f_Expected:
    print(f"\tTest #1: Failed! Expected {f_Expected} got {o_TestObject.f_Value}")
else:
    print("Success!")
del o_TestObject

print(f"Test #11: empty object")
try:
    o_TestObject = MetricScale()
except ValueError as ve:
    print("Success!")

print("##############   End of MetricScale() tests #####################")
print("\n##############     Testing RCLowPass()     ######################")
from passiveFilters.rcLowpassFilter import RCLowpassFilter

print(f"Test #1: Create a low pass filter with R=10k, c=318n")
o_TestObject            =   RCLowpassFilter(o_Resistance="10k", o_Capacitance="318n")
f_ExpectedResistance    =   10000
f_ExpectedCapacitance   =   0.000000318

if o_TestObject.o_Resistance.f_Value != f_ExpectedResistance and o_TestObject.o_Capacitance.f_Value != f_ExpectedCapacitance:
    print(f"\tFailure: Expected R={f_ExpectedResistance} and C={f_ExpectedCapacitance}, got {o_TestObject.o_Resistance.f_Value} and {o_TestObject.o_Capacitance.f_Value}")
else:
    print("Success!")

print(f"Test #2: Create a low pass filter with R=5.6M, c=4.2u")
o_TestObject            =   RCLowpassFilter(o_Resistance="5.6M", o_Capacitance="4.2u")
f_ExpectedResistance    =   5600000
f_ExpectedCapacitance   =   0.0000042

if o_TestObject.o_Resistance.f_Value != f_ExpectedResistance and o_TestObject.o_Capacitance.f_Value != f_ExpectedCapacitance:
    print(f"\tFailure: Expected R={f_ExpectedResistance} and C={f_ExpectedCapacitance}, got {o_TestObject.o_Resistance.f_Value} and {o_TestObject.o_Capacitance.f_Value}")
else:
    print("Success!")
