from django.test import TestCase
from filterdesigner.models import Number, RCLowPass
# Create your tests here.
class NumberTestCase(TestCase):
    def test_positive_base_positive_exponent(self):
        o_TestNumber    = Number(s_Input="10.4k")
        f_Expected      = 10400
        self.assertEqual(o_TestNumber.f_Value, f_Expected)
    def test_positive_base_negative_exponent(self):
        o_TestNumber    = Number(s_Input="5.43m")
        f_Expected      = 0.00543
        self.assertEqual(o_TestNumber.f_Value, f_Expected)
    def test_negative_base_positive_exponent(self):
        o_TestNumber    = Number(s_Input="-4.19G")
        f_Expected      = -4190000000
        self.assertEqual(o_TestNumber.f_Value, f_Expected)
    def test_negative_base_negative_exponent(self):
        o_TestNumber    = Number(s_Input="-11.27p")
        f_Expected      = -0.00000000001127
        self.assertEqual(o_TestNumber.f_Value, f_Expected)
    def test_unitless_string(self):
        o_TestNumber    = Number(s_Input="103.56")
        f_Expected      = 103.56
        self.assertEqual(o_TestNumber.f_Value, f_Expected)
    def test_invalid_prefix(self):
        try:
            Number(s_Input='5424.524r')
        except Exception as e:
            self.assertEqual(type(e), ValueError)

class RCLowPassTestCase(TestCase):
    def test_correct_construciton_resistance(self):
        o_TestFilter    = RCLowPass(s_Resistance="310.3k", s_Capacitance="34.6u")
        f_Expected      = 310300
        self.assertEqual(o_TestFilter.f_Resistance, f_Expected)

    def test_correct_construciton_capacitance(self):
        o_TestFilter    = RCLowPass(s_Resistance="435M", s_Capacitance='1.5m')
        f_Expected      = 0.0015
        self.assertEqual(o_TestFilter.f_Capacitance, f_Expected)

    def test_correct_cutoff_frequency(self):
        o_TestFilter    = RCLowPass(s_Resistance="433", s_Capacitance="42.9u")
        f_Expected      = 8.57
        self.assertEqual(o_TestFilter.f_CutoffFrequency, f_Expected)

    def test_correct_time_constant(self):
        o_TestFilter    = RCLowPass(s_Resistance="56M", s_Capacitance="15n")
        f_Expected      = 0.84
        self.assertEqual(o_TestFilter.f_TimeConstant, f_Expected)
        