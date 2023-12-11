package system;
import java.util.Scanner;
import system.Mainframe;


public class Menu{
	
	Scanner scannerMenu = new Scanner(System.in);
	boolean keepGoing = false; int option = -1;
	public String[] build() {
		
		while (keepGoing == false) {
			System.out.println("0.Inicio de Sesión");
			System.out.println("1.Registrar nuevo usuario");
			
			try {
				option = Integer.parseInt(scannerMenu.nextLine().strip());
			}catch(Exception NotAnInt) {
				System.out.println("Not an integer");
			}
			
			if(option==0) {
				System.out.println("Ingrese rut");
				String rut = scannerMenu.nextLine().strip();
				System.out.println("Ingrese contraseña");
				String password = scannerMenu.nextLine().strip();
				System.out.println("Ingrese fecha");
				String date = scannerMenu.nextLine().strip();
				
				
				boolean errRut = errCheckRut(rut);		// false = valido
				while(errRut==true) {
					System.out.println("Ingrese rut");
					rut = scannerMenu.nextLine().strip();
					errRut = errCheckRut(rut);
				}
				
				boolean errDate = errCheckFecha(date);	// false == valido
				while(errDate==true) {
					System.out.println("Ingrese fecha");
					date = scannerMenu.nextLine().strip();
					errDate = errCheckFecha(date);
					}
				
				String[] data = new String[3];
				data[0] = rut; data[1] = password; data[2] = date;
				keepGoing = true;
				return data;
				
			}else if(option==1) {
				System.out.println("Ingrese rut");
				String rut = scannerMenu.nextLine().strip();
				System.out.println("Ingrese nombre");
				String name = scannerMenu.nextLine().strip();
				System.out.println("Ingrese Contraseña");
				String password = scannerMenu.nextLine().strip();
				System.out.println("Ingrese fecha");
				String date = scannerMenu.nextLine().strip();
				
				boolean errRut = errCheckRut(rut);		// false = valido
				while(errRut==true) {
					System.out.println("Ingrese rut");
					rut = scannerMenu.nextLine().strip();
					errRut = errCheckRut(rut);
				}
				boolean errDate = errCheckFecha(date);	// false == valido
				while(errDate==true) {
					System.out.println("Ingrese fecha");
					date = scannerMenu.nextLine().strip();
					errDate = errCheckFecha(date);
					}
				
				String[] data = new String[4];
				data[0] = rut; data[1] = password; data[2] = date; data[3] = name;

				keepGoing = true;
				return data;
			}else {
				System.out.println("Opción no existe");
			}
		}

		return null;
	}
		
	public boolean errCheckRut(String rut) {
		boolean flag = false; int hyphenCount = 0;
		char[] rutArr = rut.toCharArray();
		int[] allowedChars = {48,49,50,51,52,53,54,55,56,45,57,107};
		int reqCont = 0;

		try {
			//9th character test
			if(rutArr[8]!=45) {
				flag = true;
				return flag;
			}
			
			for(int i = 0; i<rut.length(); i++) {
				int currentChar = rutArr[i]; 
				//hyphenCount
				if(currentChar == 45) {
					hyphenCount++;
				}
				for(int j = 0; j<allowedChars.length; j++) {
					
					//reqCount
					if(currentChar==allowedChars[j]) {
							reqCont++;
					}
				}
			}
			
			//reqCont condition
			if(reqCont!=10) {
				flag = true;
				System.out.println("El rut no corresponde al formato establecido req ");
				System.out.println(reqCont);
				return flag;
			}
			
			//hyphenCount condition
			if(hyphenCount!=1) {
				flag = true;
				System.out.println("El rut no corresponde al formato establecido hyphen");
				return flag;
			}
		} catch(Exception ArrayIndexOutOfBoundsException) {
			System.out.println("El rut no corresponde al formato establecido catch");
			flag = true;
		}
		return flag;
	}

	public boolean errCheckFecha(String date) {
		boolean flag = false; int hyphenCount = 0;
		char[] dateArr = date.toCharArray();
		int[] allowedChars = {48,49,50,51,52,53,54,55,56,45,57};
		int reqCount = 0;
		
		try {
			if (dateArr[2]!=45) {										//01-10-2022
				flag = true;
				return flag;
			}else if (dateArr[5]!=45) {
				flag = true;
				return flag;
			}
			
			for(int i = 0; i<date.length(); i++) {
				int currentChar = dateArr[i];
				if(currentChar == 45) {
					hyphenCount++;
				}
				
				for(int j = 0; j<allowedChars.length; j++) {
					if(currentChar==allowedChars[j]) {
						reqCount++;
					}
				}
			}
			
			//reqCount cond
			if(reqCount!=10) {
				flag = true;
				System.out.println("La fecha no corresponde al formato establecido");
				return flag;
			}
			//hyphenCount cond
			if(hyphenCount!=2) {
				flag = true;
				System.out.println("La fecha no corresponde al formato establecido");
				return flag;
			}
			
			//private class call
			flag = validDate(date);
		} catch(Exception ArrayIndexOutOfBoundsException){
			System.out.println("La fecha no corresponde al formato establecido");
			flag = true;
		}
		
		return flag;
	}
	
	private boolean validDate(String date) {
		boolean flag = false;
		char[] dateArrValid = date.toCharArray();
		
		//first pairing
		int firstPairing0 = dateArrValid[3];
		int firstPairing1 = dateArrValid[4];
		
		
		String month = "void"; int day = 0;
		switch(firstPairing0) {
		case(48):
			switch (firstPairing1) {			
			case(49):
				month = "Enero";
				day = makeDay(dateArrValid[0], dateArrValid[1]);
				flag = validDayForGivenMonth(month, day);
				return flag;
			case(50):
				month = "Febrero";
				day = makeDay(dateArrValid[0], dateArrValid[1]);
				flag = validDayForGivenMonth(month, day);
				return flag;
			case(51):
				month = "Marzo";
				day = makeDay(dateArrValid[0], dateArrValid[1]);
				flag = validDayForGivenMonth(month, day);
				return flag;
			case(52):
				month = "Abril";
				day = makeDay(dateArrValid[0], dateArrValid[1]);
				flag = validDayForGivenMonth(month, day);
				return flag;
			case(53):
				month = "Mayo";
				day = makeDay(dateArrValid[0], dateArrValid[1]);
				flag = validDayForGivenMonth(month, day);
				return flag;
			case(54):
				month = "Junio";
				day = makeDay(dateArrValid[0], dateArrValid[1]);
				flag = validDayForGivenMonth(month, day);
				return flag;
			case(55):
				month = "Julio";
				day = makeDay(dateArrValid[0], dateArrValid[1]);
				flag = validDayForGivenMonth(month, day);
				return flag;
			case(56):
				month = "Agosto";
				day = makeDay(dateArrValid[0], dateArrValid[1]);
				flag = validDayForGivenMonth(month, day);
				return flag;
			case(57):
				month = "Septiembre";
				day = makeDay(dateArrValid[0], dateArrValid[1]);
				flag = validDayForGivenMonth(month, day);
				return flag;
			default:
				System.out.println("Mes inválido");
				flag = true;
				return flag;
			}
		case(49):
			switch (firstPairing1) {
			case(48):
				month = "Octubre";
				day = makeDay(dateArrValid[0], dateArrValid[1]);
				flag = validDayForGivenMonth(month, day);
				return flag;
			case(49):
				month = "Noviembre";
				day = makeDay(dateArrValid[0], dateArrValid[1]);
				flag = validDayForGivenMonth(month, day);
				return flag;
				
			case(50):
				month = "Diciembre";
				day = makeDay(dateArrValid[0], dateArrValid[1]);
				flag = validDayForGivenMonth(month, day);
				return flag;
			}
		default:
			System.out.println("Mes inválido");
			flag = true;
			return flag;
		}
	}
	
	private int makeDay(int n0, int n1) {
		int[] allowedChars = {48,49,50,51,52,53,54,55,56,57};
		int[] n0ToInt = {0,1,2,3,4,5,6,7,8,9};
		
		for(int i = 0; i<allowedChars.length; i++) {
			if(n0==allowedChars[i]) {
				n0 = n0ToInt[i];
			}
			if(n1==allowedChars[i]) {
				n1 = n0ToInt[i];
			}
		} 
		String day = Integer.toString(n0) + Integer.toString(n1);
		int dayInt = Integer.parseInt(day); 
		return dayInt;
		
	}
	
	private boolean validDayForGivenMonth(String month, int day) {
		int maxDays = 0;

		switch(month) {
		case("Enero"):
			maxDays = 31;
		break;
		case("Febrero"):
			maxDays = 28;
		break;
		case("Marzo"):
			maxDays = 31;
		break;
		case("Abril"):
			maxDays = 30;
		break;
		case("Mayo"):
			maxDays = 31;
		break;
		case("Junio"):
			maxDays = 30;
		break;
		case("Julio"):
			maxDays = 31;
		break;
		case("Agosto"):
			maxDays = 31;
		break;
		case("Septiembre"):
			maxDays = 30;
		break;
		case("Octubre"):
			maxDays = 31;
		break;
		case("Noviembre"):
			maxDays = 30;
		break;
		case("Diciembre"):
			maxDays = 31;
		break;
		}
		
		if(day>maxDays) {
			System.out.println("Dia inválido");
			return true;
		}
		
		return false;
	}
	
	//relevant char codes
	/*
	 * 0=48
	 * 1=49
	 * 2=50
	 * 3=51
	 * 4=52
	 * 5=53
	 * 6=54
	 * 7=55
	 * 8=56
	 * -=45
	 * 9=57
	 * */

}
