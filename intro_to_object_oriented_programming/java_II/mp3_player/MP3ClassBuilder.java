

/**
	MP3ClassBuilder will read in the files found from MP3FileFinder
	and create MP3Class objects that will be added to ArrayList of MP3Classes.

	@Author Erin Canada
**/ 
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

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

import java.util.Scanner;
import java.util.ArrayList;
import java.io.FileNotFoundException;
import java.util.Collections;

public class MP3ClassBuilder{

	public static MP3List buildMP3List(String filePath){

		//create list
		MP3List list = new MP3List();

		ArrayList<String> result = MP3FileFinder.findMP3Files(filePath);

		for(String file : result){
			try{
				AudioFile f = AudioFileIO.read(new File(file));
				Tag tag = f.getTag();
				String songTitle = tag.getFirst(FieldKey.ARTIST);
				String artist = tag.getFirst(FieldKey.TITLE);
				String album =  tag.getFirst(FieldKey.ALBUM);
				String fileMP3 = file;

				MP3Class mp3 = new MP3Class(songTitle, artist, album, fileMP3);
				list.addMP3(mp3);

			}catch(FileNotFoundException fnf){
				System.out.println("File" + file + "was not found.");
			}catch(CannotReadException cne){
				System.out.println("Cannot read file.");
			}catch(ReadOnlyFileException rofe){
				System.out.println("This file can only be read");
			}catch(InvalidAudioFrameException iafe){
				System.out.println("Invalid audio frame.");
			}catch(IOException ioe){
				System.out.println("IO Exception Found");
			}catch(TagException te){
				System.out.println("Tag exception found.");
			}
		}
		return list;
	}
}

