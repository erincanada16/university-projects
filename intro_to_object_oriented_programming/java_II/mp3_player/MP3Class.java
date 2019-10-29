/**
	MP3Class will implement a new MP3Class object with data members of songTitle
	and the artist.

	@Author Erin Canada


**/

public class MP3Class{
	//Data members
	private String songTitle;
	private String artist;
	private String album;
	private String file;


	//Getters
	public String getSongTitle(){
		return this.songTitle;
	}

	public String getArtist(){
		return this.artist;
	}

	public String getAlbum(){
		return this.album;
	}

	public String getFile(){
		return this.file;
	}

	//Setters
	public void setSongTitle(String other){
		this.songTitle = other;
	}

	public void setArtist(String other){
		this.artist = other;
	}

	public void setAlbum(String other){
		this.album = other;
	}

	public void setFile(String other){
		this.file = other;
	}

	//Constructor
	public  MP3Class(String songTitle, String artist, String album, String file){
		this.songTitle = songTitle;
		this.artist = artist;
		this.album = album;
		this.file = file;
	}

	public String toString(){
		return "Song Title: " + songTitle + " Artist: " + artist + " Album: ";
	}

}




