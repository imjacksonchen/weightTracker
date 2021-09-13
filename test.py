import unittest
import datetime

from weightTrack import WeightNote


class TestWeightNote(unittest.TestCase):
    ### Testing getter methods ###

    def test_shouldGetWeight(self):
        testWeight = WeightNote(100, "Ate breakfast")
        self.assertEqual(testWeight.getWeight(), 100, "Should be 100")

    # Note: Impossible to check time with current time; instead
    #       use library called freezetime to mock a date and time
    """  
    def test_shouldGetTime(self):
        testWeight = WeightNote(100, "Ate breakfast")
        self.assertEqual(testWeight.getTime(),
                         datetime.datetime.now(),
                         "Should be same time as creation") 
    """

    def test_shouldGetNote(self):
        testWeight = WeightNote(100, "Ate breakfast")
        self.assertEqual(testWeight.getNote(),
                         "Ate breakfast",
                         "Should be 'Ate breakfast'")

    ### Testing setter methods ###

    def test_shouldSetWeight(self):
        testWeight = WeightNote(100, "Ate breakfast")
        testWeight.setWeight(150)
        self.assertEqual(testWeight.getWeight(), 150, "Should be 100")

    # Note: Impossible to check time with current time; instead
    #       use library called freezetime to mock a date and time
    """  
    def test_shouldSetTime(self):
        testWeight = WeightNote(100, "Ate breakfast")
        self.assertEqual(testWeight.getTime(),
                         datetime.datetime.now(),
                         "Should be same time as creation") 
    """

    def test_shouldSetNote(self):
        testWeight = WeightNote(100, "Ate breakfast")
        testWeight.setNote("Ate lunch")
        self.assertEqual(testWeight.getNote(),
                         "Ate lunch",
                         "Should be 'Ate lunch'")


# main
if __name__ == "__main__":
    unittest.main()
