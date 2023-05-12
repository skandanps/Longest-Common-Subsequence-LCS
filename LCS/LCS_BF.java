import java.io.File;
import java.io.FileNotFoundException;  
import java.util.Scanner;
import java.lang.Math;
import java.time.Duration;
import java.time.Instant;

public class LCS_BF{
	public static void main(String[] args){
		LCS_BF obj = new LCS_BF();
		String fileName = "LCS1.txt";
		// StopWatch watch = new StopWatch();
		// Instant timestamp = Instant.now();
		String[] Strings = readFile(fileName);
		System.out.println(Strings[1]);
		for(int i = 0; i < Strings.length - 1; i++){			
			// watch.start();
			// Instant start = Instant.now();
			// char[] X = Strings[i].toCharArray();
			// char[] Y = Strings[i + 1].toCharArray();
			// int length = obj.lcs(X, Y, Strings[i].length(), Strings[i+1].length());
			// watch.stop();
			// Instant finish = Instant.now();
			// long elapsedTime = Duration.between(start, finish).toMillis();
			// System.out.println();
			// System.out.println("##########################################################");
			// System.out.println("Length of the Longest common Subsequence of Strings " + Strings[i] + " & " + Strings[i+1] + " is " + length);
			// System.out.println("Time taken to find length of longest common subsequence is : " + elapsedTime);
			// System.out.println("##########################################################");
			// System.out.println();
		}
		System.out.println();
	}
	
	int lcs(char[] X, char[] Y, int m, int n){
		if(m == 0 || n == 0){
			return 0;
		}
		if(X[m-1] == Y[n-1]){
			return lcs(X, Y, m-1, n-1)+1;
		}
		else{
			return Math.max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n-1));
		}
	}
	
	public static String[] readFile(String file){
		String[] data = new String[100];
		try{
			File myObj = new File(file);
			Scanner myReader = new Scanner(myObj);
			int index = 0;
			while (myReader.hasNextLine()) {
				// System.out.println(myReader.nextLine());
				String[] words = myReader.nextLine().split(",");
				System.out.println(words[0]);
				data[index] = words[0];
				data[index + 1] = words[1];
				index++;
			}
			myReader.close();
			
		} catch (FileNotFoundException e) {
			System.out.println("An error occurred.");
			e.printStackTrace();
		}
		return data;
	}
}