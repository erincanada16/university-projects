/**
BucketSort.java  --by @ErinCanada
BucketSort has buckets that are split up into intervals based on the max value in the array.  The value corresponding to the correct interval will be placed into the 
bucket and then once every element in the ArrayBasedList has been added to a bucket, each individual bucket will be sorted and then each sorted bucket will be merged into correct order.
In this case it is from highest to lowest average rate.

**/

import java.util.Arrays;

public class BucketSort {

	public static void sort(ArrayBasedList<Product> plist) {
        //Finding maximum value for bucket interval
        int max = 0;
        for(int i = 0; i < plist.size(); i++){
        	if (plist.get(i).compareTo(plist.get(max)) >= 0){
        		max = i;
        	}

        } 
        double maxValue = plist.get(max).getAvgRate() + 1.0;

        //Creating main bucket
       ArrayBasedList<ArrayBasedList<Product>> bucket = new ArrayBasedList<ArrayBasedList<Product>>();
        for(int i = 0; i < maxValue; i++){
        	//New list for range of values
        	bucket.add(i, new ArrayBasedList<Product>());

        }
        
        for(int i = 0; i < plist.size(); i++ ){
        	int bin = (int)(plist.get(i).getAvgRate());
			//Adding each value to correct bin of each bucket
			bucket.get(bin).add(plist.get(i));
			
        }

        //Sorting lists within each bucket
        for(int i = 0; i < bucket.size(); i++){
        	InsertionSort.sort(bucket.get(i));
        }
        //Merging each bucket back to list
        int index = plist.size()-1;
        for(int i = 0; i < plist.size(); i++){
        	for(int j = 0; j < bucket.get(i).size(); j++){
        		plist.set(index, bucket.get(i).get(j));
        		index--;
        	}
        }

    }

}