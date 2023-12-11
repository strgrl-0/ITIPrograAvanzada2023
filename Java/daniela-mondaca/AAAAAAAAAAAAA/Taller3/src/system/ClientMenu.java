package system;
import personClass.Person;
import system.Menu;
import system.Mainframe;
import java.util.Scanner;
import textClass.*;
import bookingClass.Bookings;
import java.io.File;
import java.util.Scanner;

public class ClientMenu implements ClientMenuInterface{
	public void userMenu(Person person, SinglyLinkedList texts, SinglyLinkedList bookings,
						 SinglyLinkedList devolutions) {
		System.out.println("Point reached User");
		Scanner scannerClientMenu = new Scanner(System.in);
		boolean keepMenu = true;
		
		while(keepMenu==true) {
			System.out.println("0. Reservar texto");
			System.out.println("1. Devolver texto");
			System.out.println("2. Ver reservas");
			System.out.println("3. Pagar multas");
			
			int entry = scannerClientMenu.nextInt();
			//aaaa
			
			switch(entry) {
			case 0:
				boolean succesfulReserve = reserveText(person, texts, bookings, devolutions);
				if(succesfulReserve==true) {
					System.out.println("Succesfully reserved text");
				}
				break;
			case 1:
				boolean succesfulDevolution = returnText(person, texts, bookings, devolutions);
				break;
			case 2:
				break;
			case 3:
				break;
			default:
				System.out.println("not recognized");
			}

		}
		
		//Devolucion texto
		
		//Ver reservas
		
		//Pagar multas
		
	}
	
	public void workerMenu(Person person, SinglyLinkedList texts, SinglyLinkedList bookings,
			 			   SinglyLinkedList devolutions) {
		System.out.println("Point reached worker");
	}
	
	
	
	private int ingresarCodTexto() {
		System.out.println("Ingrese código texto");
		Scanner scannerTextcode = new Scanner(System.in);
		int textcode = 0;
		try {
			textcode = scannerTextcode.nextInt();
		} catch(Exception e) {
			System.out.println("Not a number");
		}
		return textcode;
		
	}
	
	
	//reservaTexto
	private boolean checkFechas(Bookings currentBooking, String fechaReserva, String fechaDevolucion, 
								SinglyLinkedList bookingsList, Person person, int textCodeCheckFechas) {
		String fechaPedReserva = currentBooking.getBookingDate();
		String fechaDevReserva = currentBooking.getReturnDate();
		Mainframe tempMainframe = new Mainframe();
		
		
		System.out.println(fechaPedReserva);
		System.out.println(fechaDevReserva);
		
		boolean pedido = false;
		boolean reservado = false;
		
		if(fechaPedReserva.equals(fechaReserva)) {
			pedido = true;
			System.out.println("changedReservaToTrue");
		}
		
		if(fechaDevReserva.equals(fechaDevolucion)) {
			reservado = true;
			System.out.println("changedDevToTrue");
		}
		
		if(pedido == false && reservado == false) {
			//reserve
			String lineToSave = ""; int bookingCode = 0;
			for(int i = 0; i<bookingsList.getTotalElements(); i++) {
				bookingCode++;
			}
			bookingCode = bookingCode + 100001;
			
			lineToSave = Integer.toString(bookingCode)+","+person.getRut()+","+textCodeCheckFechas+","+fechaReserva;
			lineToSave = lineToSave+","+fechaDevolucion;
			File bookingsFile = new File("src/files/reservas.txt");
			tempMainframe.save(bookingsFile, lineToSave);
		}
		
		return true;
		
	}
	
	private boolean reserveText(Person person, SinglyLinkedList texts, SinglyLinkedList bookings,
			 SinglyLinkedList devolutions) {
		//Reserva texto
		int textcode = 0;
		boolean keep = true;
		while(keep==true) {
			textcode = ingresarCodTexto();
			if(textcode != 0) {
				keep = false;
			}
		}
		boolean textFound = false; boolean keepTextChecking = true; 
		Menu tempmenu = new Menu();
		
		while(keepTextChecking == true) {
			for(int i = 0; i<texts.getTotalElements(); i++) {
				Textos textoActual = (Textos) texts.getDataFromList(i);
				System.out.println(textoActual.getTextCode());
				if(textcode == textoActual.getTextCode()) {
					textFound = true;
					keepTextChecking = false;
					break;
				}else {
					System.out.println("Texto no encontrado");
				}
			}
		}
		
		if(textFound == true) {
			Scanner scanReq1 = new Scanner(System.in);
			boolean checkFechaPedido = true; boolean checkFechaDevolucion = true;
			String fechaPedido = ""; String fechaDevolucion = "";
			
			while(checkFechaPedido == true) {
				System.out.println("Ingrese fecha pedido");
				fechaPedido = scanReq1.nextLine().strip();
				checkFechaPedido = tempmenu.errCheckFecha(fechaPedido);
			}
			
			while(checkFechaDevolucion == true) {
				System.out.println("Ingrese fecha devolucion");
				fechaDevolucion = scanReq1.nextLine().strip();
				checkFechaDevolucion = tempmenu.errCheckFecha(fechaDevolucion);
			}
			
			if(checkFechaPedido == false && checkFechaDevolucion == false) {
				boolean available = false;
				
				for(int i = 0; i<bookings.getTotalElements(); i++) {
					Bookings currentBooking = (Bookings) bookings.getDataFromList(i);
					
					if(currentBooking.getObjectCode()==textcode) {
						available = checkFechas(currentBooking, fechaPedido, fechaDevolucion, bookings, person, textcode);
						
						System.out.println(available);
						return available;
					}
				}
			}
			
		}
		return false;
	}
	
	//Devolucion texto
	private boolean returnText(Person person, SinglyLinkedList texts, SinglyLinkedList bookings, SinglyLinkedList devolutions) {
		Scanner scanReturnText = new Scanner(System.in);
		System.out.println("Ingrese codigo de texto a devolver");
		
		int returnText = scanReturnText.nextInt();
		boolean textFound = searchBookings(bookings, returnText, person);
		
		if(textFound == true) {
			
		}else {
			return false;
		}
		return false;
	}
	
	
	private boolean searchBookings(SinglyLinkedList bookings, int textToSearch, Person person) {
		String personRut = person.getRut();
		SinglyLinkedList bookingHits = new SinglyLinkedList();
		
		
		for(int i = 0; i<bookings.getTotalElements(); i++) {
			Bookings currentBooking = (Bookings) bookings.getDataFromList(i);
			int currentBookingObjInt = currentBooking.getObjectCode();			
			
			if(currentBookingObjInt == textToSearch) {
				Bookings currentBookingHit = userBookingLink(personRut, currentBooking);
				bookingHits.insert(currentBookingHit);
				
			}
			
		}
		if(bookingHits.getTotalElements()>1) {
			Bookings instanceChosen = chooseAnInstance(bookingHits);
			
			//verificar devolucion dentro del plazo
		}else {
			
		}
			
		bookingHits.printListContents();
		System.out.println("Texto no existe en lista");
		return false;
	}
	
	//Texto coincide con rut de usuario
	
	private Bookings userBookingLink(String personRut, Bookings currentBooking) {
		System.out.println("BookingLink reached");
		if(personRut.equals(currentBooking.getAssociatedRut())) {
			System.out.println(" the good one");
			return currentBooking;
		}
		return null;
		
	}
	
	//revisar instancias
	private Bookings chooseAnInstance(SinglyLinkedList bookingHits) {
		System.out.println("Reservas encontradas:");
		Scanner scannerChooseAnInstance = new Scanner(System.in);
		
		for(int i = 0; i<bookingHits.getTotalElements(); i++) {
			Bookings currentBooking = (Bookings) bookingHits.getDataFromList(i);
			String cBookingStr = i + " "+ currentBooking.getBookingCode()+" " + currentBooking.getAssociatedRut()+ " " + currentBooking.getObjectCode() +
								 " " + currentBooking.getBookingDate()+" " + currentBooking.getReturnDate();
			System.out.println(cBookingStr);
		}
		
		System.out.println("Ingrese reserva a devolver");
		int chooseAnInstance = scannerChooseAnInstance.nextInt();
		Bookings instanceChosen = (Bookings) bookingHits.getDataFromList(chooseAnInstance);
		
		return instanceChosen;
	}
	
	//revisar devolucion dentro del plazo
	private boolean checkReturnDate(Bookings textToCheckDate) {
		System.out.println("Checking Date");
		
	}
}
