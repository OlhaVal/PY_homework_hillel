import unittest
from homeworks import max_word,leftover_from_division,if_any_sentence_begins_with_word

class ExampleTest(unittest.TestCase):
    def test_1_01_positive_leftover_from_division_equel_0(self):
        a = 5
        b = 5
        actual_result = leftover_from_division(a, b)
        expected_result = 0
        self.assertEqual(actual_result, expected_result, f"Остача від ділення {a}/{b} не дорівнює {expected_result}")

    def test_1_02_positive_leftover_from_division_not_equel_0(self):
        a = 6
        b = 5
        actual_result = leftover_from_division(a, b)
        expected_result = 0
        self.assertNotEqual(actual_result, expected_result, f"Остача від ділення {a}/{b} дорівнює {expected_result}")

    def test_1_03_positive_leftover_from_division_(self):
        a = 15
        b = 6
        actual_result = leftover_from_division(a, b)
        expected_result = 3
        self.assertTrue(actual_result==expected_result,f"Остача від ділення {a}/{b} невірно прорахована. Очікуємо значення {expected_result}")

    def test_1_04_negative_leftover_from_division_to_0(self):
        a = 6
        b = 0
        with self.assertRaises(ZeroDivisionError):
            result = leftover_from_division(a, b)

    text = ['Tom gave up the brush with reluctance in his face but alacrity in his heart',
                               'And while the late steamer "Big Missouri" worked and sweated in the sun, the retired artist sat on a barrel in the shade close by, dangled his legs, munched his apple, and planned the slaughter of more innocents',
                               'There was no lack of material; boys happened along every little while; they came to jeer, but remained to whitewash',
                               'By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for a kite, in good repair; and when he played out, Johnny Miller bought in for a dead rat and a string to swing it with—and so on, and so on, hour after hour',
                               'And when the middle of the afternoon came, from being a poor poverty, stricken boy in the morning, Tom was literally rolling in wealth.']
    find_text_1 = "By the time"
    find_text_2 = " he time"
    find_text_3 = ""
    find_text_4 = 123

    def test_2_01_positive_some_sentence_begins_with_word(self):
        text = self.text
        find_text = self.find_text_1
        self.assertTrue(if_any_sentence_begins_with_word(text, find_text))

    def test_2_02_negative_none_of_sentence_begins_with_finding_words(self):
        text = self.text
        find_text = self.find_text_2
        self.assertFalse(if_any_sentence_begins_with_word(text, find_text))

    def test_2_03_positive_if_finding_words_is_empty(self):
        text = self.text
        find_text = self.find_text_3
        self.assertTrue(if_any_sentence_begins_with_word(text, find_text))

    def test_2_04_negative_if_finding_words_is_empty(self):
        text = self.text
        find_text = self.find_text_4
        with self.assertRaises(TypeError):
            result = if_any_sentence_begins_with_word(text, find_text)

    list_word_1 = ["Olga", "Valeyka", "QA"]
    list_word_2 = ["Olga", "Olga"]
    list_word_3 = []
    list_word_4 = "Olga"

    def test_3_01_positive_in_list_one_long_word(self):
        list_word = self.list_word_1
        long_word = "Valeyka"
        self.assertTrue(max_word(list_word)==long_word)

    def test_3_02_positive_all_words_have_the_same_longer(self):
        list_word = self.list_word_2
        expected_result = "Olga"
        self.assertEqual(max_word(list_word), expected_result)

    def test_3_03_negative_if_list_of_words_is_empty(self):
        list_word = self.list_word_3
        with self.assertRaises(ValueError):
            max_word(list_word)

    def test_3_04_positive_if_list_of_words_is_str(self):
        list_word = self.list_word_4
        self.assertTrue(max_word(list_word))

if __name__ == "__main__":
    unittest.main(verbosity=2)