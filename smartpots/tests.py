from django.test import TestCase
from .models import *
from .functions import *

# Create your tests here.
class alertModelTestCase(TestCase):
    def test_alertType_is_correct(self):
        self.assertEqual(choose_alert_type_from_status_choices(SmartPot.GOOD),Alert.Type.OUT_OF_DANGER)
        self.assertEqual(choose_alert_type_from_status_choices(SmartPot.WARNING),Alert.Type.MODERATE_DANGER)
        self.assertEqual(choose_alert_type_from_status_choices(SmartPot.DANGER),Alert.Type.HIGH_DANGER)
        
class smartPotStatusTestCase(TestCase):
    def test_smartpot_status_is_correct(self):
        self.assertEqual(evaluate_plant_status(0),SmartPot.GOOD)
        self.assertEqual(evaluate_plant_status(1),SmartPot.WARNING)
        self.assertEqual(evaluate_plant_status(2),SmartPot.DANGER)
        self.assertEqual(evaluate_plant_status(3),SmartPot.DANGER)
        