import unittest
import io
import sys
from main import hasValidSequence
from main import printValidStrings

class TestMain(unittest.TestCase):
    
    def test_has_valid_sequence_true(self):
        self.assertTrue(hasValidSequence("abba"))
        
    def test_has_valid_sequence_all_same_letters(self):
        self.assertFalse(hasValidSequence("xxxx"))
        
    def test_has_valid_sequence_true_longer_sequence(self):
        self.assertTrue(hasValidSequence("afdsaflkdsjflabba"))
        
    def test_has_valid_sequence_false_longer_sequence(self):
        self.assertFalse(hasValidSequence("afdsaflkdsjflabb"))
    
    def test_has_valid_sequence_true_all_same_letters(self):
        self.assertTrue(hasValidSequence("xxxxxyyx"))
        
    def test_print_valid_strings_custom_input(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        printValidStrings("custom_input.txt")
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "rttr[mnop]qrst\nirttrj[asdfgh]zxcvbn\n[jadsfasdf]xyyx\ndaad[dsafsd]\ndaad[dsafsd]adfdad[dsafsd]\nThis file had 5 valid string(s)\n")  
   
    def test_print_valid_strings_provided_input(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        printValidStrings("provided_input.txt")
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "uxpvoytxfazjjhi[qogwhtzmwxvjwxreuz]zduoybbzxigwggwu[lamifchqqwbphhsqnf]qrjdjwtnhsjqftnqsk[bsqinwypsnnvougrs]wfmhtjkysqffllakru\nThis file had 1 valid string(s)\n")   

    # def test_check_bracket_contents_no_valid_sequence(self):
    #     content = ['mnop']
    #     self.assertTrue(checkBracketContents(content))

    # def test_check_bracket_contents_valid_sequence(self):
    #     content = ['abba']
    #     self.assertFalse(checkBracketContents(content))
        
    # def test_check_bracket_contents_multiple_brackets_valid_sequence(self):
    #     content = ['asdf', 'abba']
    #     self.assertFalse(checkBracketContents(content))

    # def test_check_bracket_contents_multiple_brackets_no_valid_sequence(self):
    #     content = ['asdf', 'abca']
    #     self.assertTrue(checkBracketContents(content))
    
    # def test_check_bracket_contents_no_brackets(self):
    #     content = []
    #     self.assertTrue(checkBracketContents(content))
    
if __name__ == '__main__':
    unittest.main()