/**
	SongComparator will compare Song titles in alphabetical order.

	@Author Erin Canada

**/

import java.util.Comparator;
public class SongComparator implements Comparator<MP3Class> {

	public int compare(MP3Class song1, MP3Class song2) {
		return song1.getSongTitle().compareTo(song2.getSongTitle());
	}
}