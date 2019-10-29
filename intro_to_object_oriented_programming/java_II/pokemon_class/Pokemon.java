/* a program that contain Pokemon datas and the implementing of methods.

	@Author Erin Canada

*/

public class Pokemon {

	private String species;
	private int height;
	private int weight;
	private int experience;
	private boolean favorite;

	//getters
	public String getSpecies(){
		return this.species;
	}

	public int getHeight(){
		return this.height;
	}

	public int getWeight(){
		return this.weight;
	}

	public int getExperience(){
		return this.experience;
	}

	public boolean getFavorite(){
		return this.favorite;
	}


	//setters
	public void setSpecies(String newSpecies){
		this.species = newSpecies;
	}

	public void setHeight(int newHeight){
		this.height = newHeight;
	}

	public void setWeight(int newWeight){
		this.weight = newWeight;
	}

	public void setExperience(int newExperience){
		this.experience = newExperience;
	}

	public void setFavorite(boolean newFavorite){
		this.favorite = newFavorite;
	}


	//toString Method
	public String toString(){
		String returnValue = (this.species+"(" + this.height + "," + this.weight + ") with experience " + this.experience);

		if (favorite != true){
			returnValue = (returnValue + "-Not Starred.");
		}

		else{
			returnValue = (returnValue + "-Starred.");
		}
		return returnValue;
	}
	//constructors
	public Pokemon(String species, int height, int weight, int experience, boolean favorite) {
		this.species = species;
		this.height = height;
		this.weight = weight;
		this.experience = experience;
		this.favorite = favorite;
	}
}