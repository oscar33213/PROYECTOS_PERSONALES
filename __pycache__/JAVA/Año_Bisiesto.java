package __pycache__.JAVA;

import java.util.*;
public class Año_Bisiesto {

	public static void main(String[] args) {
		
		Scanner ingresa_año = new Scanner(System.in);
		
		System.out.println("Ingrese el año ");
		int año_Bisiesto = ingresa_año.nextInt();
		boolean isBisiesto = false;
		
		
		if ((año_Bisiesto % 4 == 0 && año_Bisiesto % 100 != 0) || año_Bisiesto % 400 == 0) {
		
			
					isBisiesto = true;
				}
				
				
			else if(año_Bisiesto != año_Bisiesto / 400 && año_Bisiesto == año_Bisiesto / 100){
				isBisiesto = false;
			}
			
		
		
		if(isBisiesto) {
			System.out.println("El año " + año_Bisiesto + " es bisiesto");
		} else {
			System.out.println("El año " + año_Bisiesto + " no es bisiesto");
		}
		ingresa_año.close();
		System.exit(0);
	}

}