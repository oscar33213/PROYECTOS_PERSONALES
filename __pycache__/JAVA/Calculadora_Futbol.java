package __pycache__.JAVA;

import java.util.Scanner;

public class Calculadora_Futbol {

	public static void main(String[] args) {
		//INDICAMOS LOS EQUIPOS
				
				
				Scanner ingresa_dato = new Scanner(System.in);
				System.out.println("Bienvenido a la calculadora de La Liga. Porfavor, ingrese el numero total de equipos ");
				int numero_equipos = ingresa_dato.nextInt();
				
				ingresa_dato.nextLine();
				
				String [] equipo = new String [numero_equipos];
				
				for(int i=0; i<numero_equipos; i++) {
					System.out.println("Ingrese el equipo " + (i+1) + ": ");
					equipo[i] = ingresa_dato.nextLine();
					
					
				}
				//INDICAMOS LOS RESULTADOS
				int[][] resultados = new int[numero_equipos][numero_equipos];
				
				for(int i=0;i<numero_equipos; i++) {
					for(int j=i + 1; j<numero_equipos; j++) {
						System.out.print("Ingrese el resultado del partido entre " + equipo[i] + " y " + equipo[j] + " (goles del primero): ");
						int goles_equipo1 = ingresa_dato.nextInt();
						System.out.print("Ingrese el resultado del partido entre " + equipo[j] + " y " + equipo[i] + " (goles del segundo): ");
						int goles_equipo2 = ingresa_dato.nextInt();
						
						resultados[i][j] = goles_equipo1 - goles_equipo2;
						resultados[j][i] = goles_equipo2 - goles_equipo1;
						
						
					}
					
				}
				
				int [] puntos = new int[numero_equipos];
				int [] diferencia_goles = new int [numero_equipos];
				
				for(int i=0;i<numero_equipos;i++) {
					for(int j=0; j<numero_equipos;j++) {
						puntos[i] += (resultados[i][j] > 0) ? 3 : (resultados[i][j] == 0) ? 1 : 0;
		                diferencia_goles[i] += resultados[i][j];
					}
				}
				
				for (int i = 0; i < numero_equipos - 1; i++) {
		            for (int j = 0; j < numero_equipos - i - 1; j++) {
		                if (puntos[j] < puntos[j + 1]) {
		                    // Intercambiar puntos
		                    int tempPuntos = puntos[j];
		                    puntos[j] = puntos[j + 1];
		                    puntos[j + 1] = tempPuntos;
		                    // Intercambiar nombres de equipos
		                    String tempEquipo = equipo[j];
		                    equipo[j] = equipo[j + 1];
		                    equipo[j + 1] = tempEquipo;
		                    // Intercambiar diferencia de goles
		                    int tempDiferencia =  diferencia_goles[j];
		                    diferencia_goles[j] =  diferencia_goles[j + 1];
		                    diferencia_goles[j + 1] = tempDiferencia;
		                }
		            }
		        }

				
				System.out.println("\nTabla de posiciones:");
		        System.out.println("Equipo\t\tPuntos\t\tDiferencia de Goles");
		        for (int i = 0; i < numero_equipos; i++) {
		            System.out.println(equipo[i] + "\t\t" + puntos[i] + "\t\t" + diferencia_goles[i]);
		        }
		        
		        ingresa_dato.close();
		        System.exit(0);

	}

}