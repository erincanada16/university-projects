/**
	AristComparator will compare Artist's names in alphabetical order.

	@Author Erin Canada

**/
import java.util.Comparator;

public class ArtistComparator implements Comparator<MP3Class> {

	public int compare(MP3Class artist1, MP3Class artist2) {
		return artist1.getArtist().compareTo(artist2.getArtist());
	}
}