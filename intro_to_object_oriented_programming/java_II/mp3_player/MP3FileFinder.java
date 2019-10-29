/**
	MP3FileFinder  will read in an absolute path and count the total
	number of valid mp3 class files found recursively.

	@Author Erin Canada
**/
import java.util.ArrayList;
import java.io.File;

public class MP3FileFinder{

	public static ArrayList<String> findMP3Files(String directory){

		ArrayList<String> result = new ArrayList<String> ();
		findMP3Files(new File(directory), result);
		return result;
	}

	private static void findMP3Files(File input, ArrayList<String> result){
		
		if(input.isFile()){

			String file = input.getAbsolutePath();
			int extension = file.lastIndexOf(".");

			String ext = file.substring(extension);
			//checking for java file, adding it to result list
			if (ext.equals(".mp3")){
				result.add(file);
			}
			
		}

		else if (input.isDirectory()){
			File[] children = input.listFiles();
			for(File f: children){
				findMP3Files(f, result);
			}
		}
	}
}