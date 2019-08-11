import MathFunctions

class Permutation():
    def find_permutations(self, string):
        math_object = MathFunctions.MathFunction()
        array_permutations = []
        len_of_string = len(string)
        if len_of_string >= 3:
            for char_start in string:
                end_string = string.replace(char_start, "")
                end_string_permutations = self.find_permutations(end_string)
                for i in range(0, math_object.factorial(len(end_string))):
                    array_permutations.append(char_start + end_string_permutations[i])

        if len_of_string == 2:
            array_permutations.append(string[0] + string[1])
            array_permutations.append(string[1] + string[0])

        if len_of_string == 1:
            array_permutations.append(string)
        return sorted(array_permutations)

    def lexicographic_permutation(self, string, position):
        lexicographic_permutations = self.find_permutations(string)
        return lexicographic_permutations[position - 1]