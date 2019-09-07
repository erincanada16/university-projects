/**
	ArrayBasedList.java --by @ErinCanada
**/

import java.util.AbstractList;

public class ArrayBasedList<E> extends AbstractList<E> {
	
	//instance members
	private E [] plist;
	private int count;

	
	//Constructor(s)
	public ArrayBasedList(){
		//New ArrayBasedList of size 100
		this.plist = (E[]) new Object[100];
		this.count = 0;
	}


	//Instance methods
	public void resize (){
		//Length of Plist assigned to num, new list is created of double the size
		int num = this.plist.length;
		num = num*2;
		E [] newplist = (E[]) new Object[num];

		//Items old list is copied to new list
		for(int i = 0; i < this.plist.length; i++){
			newplist[i] = this.plist[i];
		}
		//plist maintained
		this.plist = newplist;

	}

	@Override
	public E get(int index) {
		
		//try{
			//Space is availble, but no value is contained
			if(index >= count || index < 0){
				// System.out.println("NULL");
			}else{
				//Gets element at specified index
				return plist[index];
			}
		// }catch(IndexOutOfBoundsException error){
			// System.out.println("Index Out of Bounds");
		// }
		
		return null;
	}

	@Override
	public int size() {
		return count;
	}
	
	@Override
	public boolean add(E e) {
		// Resize
		if (count == plist.length){
			resize();
		}
		//Overload
		this.add(this.count, e);

		return true;
	}
	
	@Override
	public void add(int index, E element) {

		try{
			// Resize List
			if (count == plist.length){
				resize();
			}

			//Shift elements to the right of index
			for(int i = count-1; i >= index; i--){
				plist[i+1] = plist[i];
			} 
			
			//Add element to specified index
			plist[index] = element;
			this.count++;

		}catch(IndexOutOfBoundsException error){
			System.out.println("Index Out of Bounds");
		}

	}
	
	@Override
	public E set(int index, E element) {
		try{
			//Resized list
			if(index >= plist.length){
				resize();
			}
			//Sets new element to index
			plist[index] = element;

		}catch(IndexOutOfBoundsException error){
			System.out.println("Index Out of Bounds");
		}

		return null;
		
	}
	
	@Override
	public E remove(int index) {
	
		try{
			//Shifts every element from index to end over to left
			for(int i = index; i < plist.length-1; i++){
				plist[i] = plist[i+1];
			}
			//Decrements count since removing item from list
			count--;
			return null;

		}catch(IndexOutOfBoundsException error){
			System.out.println("Index Out of Bounds");
		}
		return null;
	}


}
