
import java.util.ArrayList;

/* A program that prints a list of Pokemon from the PokedexBuilder and a csv file, "pokemon.csv," and prints the average height,
	weight, experience, the tallest, the smallest and then the Pokemon with greater experience than
	the input level (350).

	@Author Erin Canada

*/





public class PokemonDriver {

	public static void main(String[] args) {
		//use the builder to build a student list from file
		PokedexBuilder builder = new PokedexBuilder();
		Pokedex list = builder.buildPokedex("pokemon.csv");


		//print innformation about all Pokemon
		System.out.println("All Pokemon: " + list.toString());

		//printing average height info
		System.out.printf("Average Height: %.2f ",list.averageHeight());

		//printing average weight
		System.out.printf("\nAverage Weight: %.2f ",list.averageWeight());

		//printing average Experience
		System.out.printf("\nAverage Experience: %.2f ",list.averageExperience());

		//printing species of tallest
		System.out.println("\nSpecies of Tallest: " + list.tallest());

		//printing species of smallest
		System.out.println("Species of Smallest: " + list.smallest());

		//printing Pokemon with experience greater than input:
		System.out.println("Pokemon with experience greater than 350: ");

		ArrayList<Pokemon> mostExperiencedPokemon = list.mostExperienced(350);
		
		for (Pokemon pokemon : mostExperiencedPokemon) {

			System.out.println(pokemon.toString());
		}

		


	}

}

