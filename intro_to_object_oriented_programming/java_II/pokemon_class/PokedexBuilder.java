/* A program that will create a new Pokedex from a csv file.

	@Author Erin Canada

*/
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


public class PokedexBuilder {

	public Pokedex buildPokedex (String filename) {

		//create list to be returned
		Pokedex list = new Pokedex();


		//open file
		File inputFile = new File(filename);




		try (Scanner input = new Scanner(inputFile)) {


			//read in each line of file
			//	create Pokemon
			//	add Pokemon to list
			input.useDelimiter(",|\n");
			System.out.println(input.nextLine());

			while(input.hasNextLine()) {
				input.next();
				String species = input.next();
				input.next();
				int height= Integer.parseInt(input.next());
				int weight = Integer.parseInt(input.next());
				int experience = Integer.parseInt(input.next());
				input.next();
				input.next();

				Pokemon pokemon = new Pokemon (species, height, weight, experience, false);
				
				list.addPokemon(pokemon);
			}

		}catch(FileNotFoundException fnf) {
			System.out.println(fnf.getMessage());
			return null;
		}

		//return list
		return list; 
	}
}