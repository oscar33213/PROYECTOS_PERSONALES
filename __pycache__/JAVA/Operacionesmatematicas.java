package __pycache__.JAVA;


import java.util.Scanner;
public class Operacionesmatematicas {

	public static void main(String[] args) {
		
		Scanner datooperacion = new Scanner(System.in);
		
		System.out.println("Inserta el primer numero");
		
		double numero1 = datooperacion.nextDouble();
		
		System.out.println("Inserta el segundo numero");
		
		double numero2 = datooperacion.nextDouble();
		
		
		System.out.println("Indica el operador");
		
		System.out.println("1. SUMA (+)");
		System.out.println("2. RESTA (-)");
		System.out.println("3. MULTIPLICACION (*)");
		System.out.println("4. DIVISION (/)");
		System.out.println("5. RAIZ CUADRADA (√)");
		
		
		
		int operador = datooperacion.nextInt();
		
		
		switch(operador)  {
		
		case 1:
			
			System.out.println("El resultado de " + numero1 + " + " +  numero2 + " = " + (numero1 + numero2));
			break;
			
		case 2:
			System.out.println("El resultado de " + numero1 + " - " + numero2 + " = " + (numero1 - numero2));
			break;
			
		case 3: 
			System.out.println("El resultado de " + numero1 + " * " + numero2 + " = " + (numero1 * numero2));
			break;
			
		case 4:
			System.out.println("El resultado de " + numero1 + " / " + numero2 + " = " + (numero1 / numero2));
			break;
		case 5:
			System.out.println("La raiz cuadrada de " + numero1 + " + " + numero2 + " = " + (Math.sqrt(numero1)+ Math.sqrt(numero2)));
		
			
		default:
			System.out.println("Entrada no valida");
			break;
		}
		
		datooperacion.close();
	}

}