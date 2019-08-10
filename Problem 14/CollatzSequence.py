class CollatzSequence:

    def next_number(self, num):
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1
        return int(num)

    def len_of_sequence(self, num):
        length_of_sequence = 1
        while num != 1:
            num = self.next_number(num)
            length_of_sequence += 1
        return length_of_sequence

    def array_of_sequence(self, num):
        array_of_sequence = []
        while num != 1:
            array_of_sequence.append(num)
            num = self.next_number(num)
        array_of_sequence.append(1)
        return array_of_sequence

    def largest_length_sequence(self, start_num, end_num):
        max_size = 1
        max_number = 1
        for i in range(start_num, end_num):
            length_of_sequence = self.len_of_sequence(i)
            if length_of_sequence > max_size:
                max_size = length_of_sequence
                max_number = i
        return max_number
