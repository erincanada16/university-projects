/**
	MP3List.java creates an ArrayList of type MP3Class and provides methods for that list.
**/

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Collections;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Random;

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


public class MP3List {

	private ArrayList<MP3Class> list;

	public MP3List() {
		this.list = new ArrayList<MP3Class>();
	}

	public String toString(){
		String returnString = "";
		int num = 1;
		for (MP3Class mp3 : this.list) {
			returnString = returnString + num +". " + mp3.toString() + "\n";
			num++;
		}
		return returnString;
	}

	public void addMP3(MP3Class mp3){
		this.list.add(mp3);
	}

	//Sorting ArrayList<MP3> by song title
	public void songSort(){
		Collections.sort(this.list, new SongComparator());
		
	}

	//Sorting ArrayList<MP3> by artist
	public void artistSort(){
		Collections.sort(this.list, new ArtistComparator());
	
	}
	// //Prints out a numbered list of the songs in list
	// public void numberedList(ArrayList<MP3Class> list){
	// 	for (int i = 0; i<list.size(); i++){
	// 		System.out.println((i+1) +": " + list.get(i));
	// 	}
	// }

	//Finds song to play from user input
	public String selectSong(int song){
		String message = "";
		int index = 0;
		for(int i = 0; i<this.list.size(); i++){
		//index + 1 = song in numberedList 
		//numbered list starts at 1 while ArrayList index starts at 0
			if(song == (index+1)){
				return this.list.get(index).getFile();
			}
			index++;
		}
		return "invalid";			
	}

	public int randomSong(){
		Random song = new Random();
		int num = song.nextInt(list.size()-1)+1; 
		return num;
	}



}