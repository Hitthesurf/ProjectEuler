import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;


class TestNumberToLetter {

	@Test
	void test_number_1_gives_one() {
        String expected = "one";
        String actual = NumberToLetter.WordNumber(1);
        assertEquals(expected, actual);
	}
	
	@Test
	void test_number_9_is_correct() {
        String expected = "nine";
        String actual = NumberToLetter.WordNumber(9);
        assertEquals(expected, actual);		
		
	}
	
	@Test
	void test_number_18_is_correct() {
        String expected = "eighteen";
        String actual = NumberToLetter.WordNumber(18);
        assertEquals(expected, actual);				
		
	}
	
	
	@Test 
	void test_number_21_combos_correct() {
		String expected = "twenty one";
		String actual = NumberToLetter.WordNumber(21);
		assertEquals(expected, actual);
		
	}
	
	@Test
	void test_number_25_combos_correct() {
		String expected = "twenty five";
		String actual = NumberToLetter.WordNumber(25);
		assertEquals(expected, actual);
	}
	
	@Test
	void test_number_36_combos_correct() {
		String expected = "thirty six";
		String actual = NumberToLetter.WordNumber(36);
		assertEquals(expected, actual);
	}
	
	@Test
	void test_number_99_combos_correct() {
		String expected = "ninety nine";
		String actual = NumberToLetter.WordNumber(99);
		assertEquals(expected, actual);
	}
	
	@Test
	void test_number_173_combos_correct() {
		String expected = "one hundred and seventy three";
		String actual = NumberToLetter.WordNumber(173);		
		assertEquals(expected, actual);
		
	}
	
	@Test
	void test_number_582_combos_correct() {
		String expected = "five hundred and eighty two";
		String actual = NumberToLetter.WordNumber(582);		
		assertEquals(expected, actual);
		
	}
	
	@Test
	void test_number_900_combos_correct() {
		String expected = "nine hundred";
		String actual = NumberToLetter.WordNumber(900);		
		assertEquals(expected, actual);
		
	}
	
	@Test
	void test_number_1000_combos_correct() {
		String expected = "one thousand";
		String actual = NumberToLetter.WordNumber(1000);		
		assertEquals(expected, actual);
		
	}
	
	@Test
	void test_number_3452_combos_correct() {
		String expected = "three thousand and four hundred and fifty two";
		String actual = NumberToLetter.WordNumber(3452);		
		assertEquals(expected, actual);
		
	}

	@Test
	void test_number_999999_combos_correct() {
		String expected = "nine hundred and ninety nine thousand and nine hundred and ninety nine";
		String actual = NumberToLetter.WordNumber(999999);		
		assertEquals(expected, actual);
		
	}

}

class TestLenOfNumberToLetter {
	
	@Test
	void test_number_5_return_4() {
		int expected = 4;
		int actual = NumberToLetter.LenOfWordNumber(5);
		assertEquals(expected, actual);
	}
	
	@Test
	void test_number_342_return_23() {
		int expected = 23;
		int actual = NumberToLetter.LenOfWordNumber(342);
		assertEquals(expected, actual);
	}
	
	@Test
	void test_number_115_return_20() {
		int expected = 20;
		int actual = NumberToLetter.LenOfWordNumber(115);
		assertEquals(expected, actual);
	}
	
}

class TestLoopedLenOfNumber {
	
	@Test
	void test_total_of_first_5_numbers_is_19() {
		int expected = 19;
		int actual = NumberToLetter.LoopedLenOfWordNumber(5);
		assertEquals(expected, actual);
		
	}
	
	/**
	@Test
	void test_to_solve_problem_of_first_1000_numbers() {
		int expected = 0; //Changed to zero so doesn't give away answer
		int actual = NumberToLetter.LoopedLenOfWordNumber(1000);
		assertEquals(expected, actual);		
				
	}
	*///Commented so all tests pass
}
