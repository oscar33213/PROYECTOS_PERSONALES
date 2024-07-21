package __pycache__.JAVA;

import java.util.*;
public class Capicua {

	public static void main(String[] args) {
		Scanner ingresa_dato = new Scanner(System.in);
		System.out.println("Ingrese el numero");
		String numeroCapicua = ingresa_dato.nextLine();
		char [] capicua = numeroCapicua.toCharArray();
		
		boolean isCapicua = true;
		
		for(int i=0; i<capicua.length / 2; i++) {
			
			if(capicua[i]!= capicua[capicua.length - 1 - i]) {
				isCapicua = false;
				break;
			} 
		}
		
		if(isCapicua) {
			System.out.println("El numero " + numeroCapicua + " es capicua");
		} else {
			System.out.println("El numero " + numeroCapicua + " no es capicua");
		}
		
		ingresa_dato.close();
		System.exit(0);
		}
		
	
		}
		

	

