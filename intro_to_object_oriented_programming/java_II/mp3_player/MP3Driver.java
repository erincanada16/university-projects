
//TODO Exceptions

/**
	MP3Driver.java will build a list of MP3Classes and offer options to the user.
	@Author Erin Canada
**/

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Collections;
import java.util.Scanner;
import java.util.ArrayList;

import org.jaudiotagger.audio.AudioFile;
import org.jaudiotagger.audio.AudioFileIO;
import org.jaudiotagger.audio.exceptions.CannotReadException;
import org.jaudiotagger.audio.exceptions.InvalidAudioFrameException;
import org.jaudiotagger.audio.exceptions.ReadOnlyFileException;
import org.jaudiotagger.tag.FieldKey;
import org.jaudiotagger.tag.Tag;
import org.jaudiotagger.tag.TagException;

import javazoom.jl.decoder.JavaLayerException;
import javazoom.jl.player.Player;

public class MP3Driver{

	public static void main(String[] args) {
		
		//if no valid argument
		if (args.length == 0){
		System.out.println("No path entered.");
		System.exit(0);
		}

		MP3ClassBuilder builder = new MP3ClassBuilder();
		MP3List list = builder.buildMP3List(args[0]);
	
		String songFile = "";
		//Setting the main menu to true
		boolean menu = true;

		//No song currently playing
		boolean started = false;
		
		Player player = null;

		int number = 0;
		while(number!=6){
			System.out.println("\nPlease select an option:");
			Scanner scan = new Scanner(System.in);
			System.out.println("\t1. List all MP3s sorted by song title\n\t2. List all MP3s sorted by artist\n\t3. Play MP3\n\t4. Play random song\n\t5. Stop playback \n\t6. Exit the program");
			number = scan.nextInt();
			//Listing songs by title
			if(number == 1){
				list.songSort();
				System.out.println("\n" + list.toString());
				continue;
			}
			//Listing songs by artist
			else if(number == 2){
				list.artistSort();
				System.out.println("\n" + list.toString());
				continue;
			}
			//Playing song selected by user
			else if(number == 3){

				Scanner scanSong = new Scanner(System.in);
				System.out.println("Which song file would you like to play?");
				//prints a numbered list of ArrayList<MP3Class> list
				System.out.println(list.toString());
				//user input of a number corresponding to a song they would like to play
				int song = scanSong.nextInt();
				//assigns user input to variable
				songFile =list.selectSong(song);

				try{
					//Stops song if one is already playing
					if(started){
						player.close();
					}
					//plays song
					Player anotherPlayer = new Player(new FileInputStream(songFile));
					player = anotherPlayer;
			
					Thread t = new Thread() {
					    public void run() {
					        try {
					        	anotherPlayer.play();
					        } catch(Exception e) {
					            e.printStackTrace();
					        }
				   		}
					};       		
					t.start();
					started = true;
				}catch (FileNotFoundException fnf){
					System.out.println("File not found.");
				}catch(JavaLayerException jle){
					System.out.println("Java layer exception.");
				}	
				
					
				continue;
			}
			//play random song	
			else if (number == 4){
				if (started){
					player.close();
				}
				int song = list.randomSong();
				songFile = list.selectSong(song);
				try{
				
					Player anotherPlayer = new Player(new FileInputStream(songFile));
					player = anotherPlayer;
			
					Thread t = new Thread() {
					    public void run() {
					        try {
					        	anotherPlayer.play();
					        } catch(Exception e) {
					            e.printStackTrace();
					        }
				   		}
					};       		
					t.start();
					started = true;
				}catch (FileNotFoundException fnf){
					System.out.println("File not found.");
				}catch(JavaLayerException jle){
					System.out.println("Java layer exception.");
				}		
				continue;				
					
			}
			//Stops song if one is playing
			else if(number == 5){
				//if song is playing, stop playing.
				if(started){
					player.close();
				}				
				started = false;
				continue;
			}

			else if (number == 6){
				//if a song is playing, stop it and exit program
				if (started){
					player.close();
				}
				break;	
			}

			else{
				System.out.println("Please try again.");
				continue;
			}
		}
	}
}