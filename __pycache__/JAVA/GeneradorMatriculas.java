package __pycache__.JAVA;


import java.util.*;

public class GeneradorMatriculas {

	public static void main(String[] args) {
		
		String numero = "";
		String letra = "";
		
		
		Random matricularandom = new Random();
		
		for(int i = 0; i<4; i++) {
			numero+= matricularandom.nextInt(10);
			
		}
		
		for(int i = 0; i< 3; i++) {
			letra += (char)(matricularandom.nextInt(26) + 'A');
		}
		
		String matricula = numero + letra;
		
		System.out.println("La matricula es: " + matricula);
		
		
	}

}