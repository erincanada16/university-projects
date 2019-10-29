/* a program contains an ArrayList containing objects of type Pokemon 
	and implements default constructor and methods that will add pokemon 
	to the Pokedex, returns a string representation of the Pokedex, returns 
	average height, weight, and experience of all Pokemon.   Then it will
	returns the species of the Pokemon with largest height and smallest weight
	as well as returning experience greater than level passed as the input.

	@Author Erin Canada

*/

//importing methods
import java.util.ArrayList;


public class Pokedex {
	//data member
	private ArrayList<Pokemon> pokemon;

	//pokemon is null

	//constructor
	public Pokedex(){
		
		this.pokemon = new ArrayList<Pokemon>();
	}
	//method: add pokemon to ArrayList<Pokemon>
	public void addPokemon(Pokemon pokemon) {
		
		this.pokemon.add(pokemon);
	}

	
	//creating toString method to return a string of Pokedex
	public String toString(){
		
		String returnString = "";

		for(Pokemon pokemon: this.pokemon) {
			
			returnString = returnString + pokemon.toString() + "\n";
		}

		return returnString;
	}

	//return average height of all Pokemon in the Pokedex
	public double averageHeight(){
		
		double totalHeights = 0;

		for(Pokemon pokemon: this.pokemon) {

			totalHeights = totalHeights + pokemon.getHeight();
		}

		double resultHeight = totalHeights/this.pokemon.size();

		return resultHeight;

	}

	//return average weight of all Pokemon in the Pokedex
	public double averageWeight(){
	
		double totalWeights = 0;

		for(Pokemon pokemon: this.pokemon) {

			totalWeights = totalWeights + pokemon.getWeight();
		}

		double resultWeight = totalWeights/this.pokemon.size();

		return resultWeight;
	}

	//return average experience of all Pokemon in the Pokedex
	public double averageExperience(){
	
		double totalExperience = 0;

		for(Pokemon pokemon: this.pokemon) {

			totalExperience = totalExperience + pokemon.getExperience();
		}

		double resultExperience = totalExperience/this.pokemon.size();

		return resultExperience;
	}

	//return species of Pokemon with largest height
	public String tallest (){
		int maxHeight = 0;
		int heightIndex = 0;

		for(int i = 0; i < this.pokemon.size(); i++) {
			
			if (maxHeight < this.pokemon.get(i).getHeight()){

				maxHeight = this.pokemon.get(i).getHeight();

				heightIndex = i;
			}
			
		}

		return this.pokemon.get(heightIndex).getSpecies();
	}

	//return species of Pokemon with smallest weight
	public String smallest(){
		int minWeight = this.pokemon.get(0).getWeight();
		int weightIndex = 0;

		for(int i = 0; i < this.pokemon.size(); i++) {

			if (minWeight > this.pokemon.get(i).getWeight()) {

				minWeight = this.pokemon.get(i).getWeight();

				weightIndex = i;
			}
		}
		return this.pokemon.get(weightIndex).getSpecies();
	}
	//returns list of Pokemon with experience level greather than the level passed
	public ArrayList<Pokemon> mostExperienced(int level){

		ArrayList<Pokemon> mostExperiencedPokemon = new ArrayList<Pokemon>();

		for (int i = 0; i < this.pokemon.size(); i++) {

			if (this.pokemon.get(i).getExperience() > level) {
				
				mostExperiencedPokemon.add(this.pokemon.get(i));
			}
		}

		return mostExperiencedPokemon;
	}
}
