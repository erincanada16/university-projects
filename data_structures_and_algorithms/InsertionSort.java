	/**
		InsertionSort.java --by @ErinCanadat

		InsertionSort is like a hand of cards! Say you start from the very left (or 0 index of ArrayBased List) and think hmmmm is the next card
		greater than or less then my first card?? Since we are sorting it from highest to lowest, if the second card greater than you swap!
		Add another card into you already sorted piece and compare with each card until you find its spot! This is insertion sort.
		**/


public class InsertionSort {

	public static  void sort(ArrayBasedList<Product> plist) {
		// temporary value of current card (or Amazon rating in the long run)
     	Product value;
     	//For every index in your plist starting at 1.. this is the part that adds another card to your sorted piece
        for (int i = 1; i < plist.size(); i++) {
        	//For every card in your smaller hand you compare the additional card you just added to the mostly sorted hand!
            for(int j = i ; j > 0 ; j--){
            	//Check to see if it is greater than the current index
                if(plist.get(j-1).compareTo(plist.get(j)) < 0){
                	//if it is, swap to its correct place!
                    value = plist.get(j);
                    plist.set(j,plist.get(j-1));
                    plist.set(j-1, value);
                }
            }
        }

    }
	
}