
public class NumberToLetter {
	
	static int[] Numbers = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,
			80,90,100, 1000};
	static String[] Words = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
			"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
			"eighteen", "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
			"ninety", "hundred", "thousand"};
	
	
	public static String WordNumber(int num) 
	{
		
		String my_number_word = "";

		
		while (num != 0) {
			int biggest_num_index = find_biggest_num_index(num);
			//Check if 100 or over
			if (biggest_num_index>=27) {
				int times = num / Numbers[biggest_num_index];
				String word_times = WordNumber(times);
				num = num - times*Numbers[biggest_num_index];
				my_number_word = my_number_word + word_times + " " + Words[biggest_num_index] + " and ";
			}
			else {
				num = num - Numbers[biggest_num_index];
				my_number_word = my_number_word + Words[biggest_num_index] + " ";
			}
		}
		
		//Need to remove and at the end
		if (my_number_word.length()>4) {
			
			if (my_number_word.substring(my_number_word.length()-4).equals("and ")) {
				my_number_word = my_number_word.substring(0, my_number_word.length()-4);	
			}
		}
		
		return my_number_word.substring(0, my_number_word.length()-1);
	}

	
	public static int find_biggest_num_index(int num) {
		
		for (int i = Numbers.length - 1; i >= 0; i = i - 1) {
			int Current_Number = Numbers[i];
			if (Current_Number <= num) {
				
				return i;
			}
					
		}
		
		return 0;
	}
	
	public static int LenOfWordNumber(int num)
	{
		String WordedNum = WordNumber(num).replaceAll(" ", "");
		
		return WordedNum.length();
	}
	
	public static int LoopedLenOfWordNumber(int upto) 
	{
		int total = 0;
		for (int i = 1; i <= upto; i++) 
		{
			total = total + LenOfWordNumber(i);
		}
		return total;
	}
}
