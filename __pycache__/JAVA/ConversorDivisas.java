package __pycache__.JAVA;


import java.util.Scanner;
public class ConversorDivisas {

	public static void main(String[] args) {
	
		Scanner divisa = new Scanner(System.in);
		
		
		System.out.println("Bienvenido al conversor de Divisas");
		System.out.println("Indica la cantidad en EUROS ");
		
		int moneda = divisa.nextInt();
		
		System.out.println("Indique el tipo de divisa");
		System.out.println("1. PESETAS");
		System.out.println("2. DOLARES");
		System.out.println("3. YUANES");
		System.out.println("4. LIBRAS");
		System.out.println("5. PESOS MEXICANOS");
		
		int conversor_divisa = divisa.nextInt();
		
		
		
		switch(conversor_divisa) {
		
		case 1: 
			conversor_divisa = moneda * 1000 / 6;
			System.out.println("La cantidad de " + moneda + " € en PESETAS es " + conversor_divisa + " PTAS");
			break;
			
			
		case 2: 
			conversor_divisa = (int) (moneda * 1.09);
			System.out.println("La cantidad de " + moneda + " € en DOLARES es " + conversor_divisa + " $");
			break;
			
			
		case 3:
			
			conversor_divisa = (int) (moneda * 7.83);
			System.out.println("La cantidad de " + moneda + " € en YUANES es " + conversor_divisa + " ¥");
			break;
			
		case 4:
			conversor_divisa = (int) (moneda * 0.86);
			System.out.println("La cantidad de " + moneda + " € en LIBRAS es " + conversor_divisa + " £");
			break;
			
		case 5:
			conversor_divisa = (int) (moneda * 18.20);
			System.out.println("La cantidad de " + moneda + " € en PESO MEXICANO es " + conversor_divisa + " MXN$");
			break;
		}
		
		
		divisa.close();
		System.exit(0);
		
	
	

	}

}