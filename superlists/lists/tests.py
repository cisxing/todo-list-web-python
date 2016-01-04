from django.test import TestCase

# Create your tests here.
# Get into the idea of the testing loop
# We will do some exercises
class SmokeTest(TestCase):
    def test_bad_math(self):
        self.assertEqual(1+1, 3)
        
