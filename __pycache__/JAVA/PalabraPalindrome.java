package __pycache__.JAVA;

import java.util.*;



public class PalabraPalindrome {

	public static void main(String[] args) {
		
		
		Scanner ingresa_palabra = new Scanner(System.in);
		
		System.out.println("Ingrese la palabra: ");
		
		String palabraAnalizar = ingresa_palabra.next();
		
		char[] palindrome = palabraAnalizar.toCharArray() ;
		
		boolean isPalindrome = true;
	
		
		for(int i = 0 ; i< palindrome.length; i++) {
			if(palindrome[i] != palindrome[palindrome.length- 1 - i] ) {
				isPalindrome = false;
				break;
			} 
		}
		
		if(isPalindrome) {
			System.out.println("La palabra " + palabraAnalizar + " es palindrome");
		} else {
			System.out.println("La palabra " + palabraAnalizar + " no es palindrome");
		}
		
		ingresa_palabra.close();
		System.exit(0);

	}

}