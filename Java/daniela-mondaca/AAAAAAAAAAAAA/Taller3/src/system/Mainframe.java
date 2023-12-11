package system;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

import textClass.*;
import personClass.Person;
import devolutionClass.Devolutions;
import bookingClass.Bookings;
import system.*;
import system.ClientMenu;

//scanner import
import java.util.Scanner;

public class Mainframe {

	public void save(File file, String data) {
		//oh no here it goes again
		try {
			FileWriter fw = new FileWriter(file, true);
			fw.append(data);
			fw.close();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}

	public Object read(File readFrom) {
		//my oh my here starts
		try {
			Scanner scannerRead = new Scanner(readFrom);
			SinglyLinkedList textsLL = new SinglyLinkedList();
			SinglyLinkedList bookingsLL = new SinglyLinkedList();
			SinglyLinkedList peopleLL = new SinglyLinkedList();
			SinglyLinkedList devolutionLL = new SinglyLinkedList();
			
			while(scannerRead.hasNextLine()==true) {
				String currentLine = scannerRead.nextLine().strip();
				String[] lineParts = currentLine.split(",");
				//System.out.println(currentLine);
				int lineLength = lineParts.length;
				
				if(lineLength>=6) {
					textsLL.insert(morphIntoTexts(lineParts));
				}else if(lineLength==4) {
					peopleLL.insert(morphIntoPeople(lineParts));
				}
				
				if(lineLength==5) {
					switch(lineParts[4]) {
					case("pendiente"):
						devolutionLL.insert(morphIntoDevolution(lineParts));
						break;
					case("pagado"):
						devolutionLL.insert(morphIntoDevolution(lineParts));
						break;
					default:
						bookingsLL.insert(morphIntoBookings(lineParts));
						break;
					}
				}
				
			}
			
			String fileName = readFrom.getName();
			switch(fileName) {
			case("textos.txt"):
				return textsLL;
			case("reservas.txt"):
				return bookingsLL;
			case("personas.txt"):
				return peopleLL;
			case("devoluciones.txt"):
				return devolutionLL;
			}
			
			//default
			return null;
		} catch (Exception FileNotFoundException ) {
			System.out.println("Archivo No Existe o está vacío");
		}
		
		return null;
	}

	public void login(Object originalLinkedList, SinglyLinkedList textos,
					  SinglyLinkedList reservas, SinglyLinkedList devoluciones,
					  File textosFile, File reservasFile, File personasFile, File devolucionesFile) {
		//need to send login info to a method depending on the clearance level
		Menu menu = new Menu();
		String[] accessData = menu.build();					//0 = rut, 1= pass, 2= date 3=name
		
		ClientMenu MenuMainframe = new ClientMenu();
		SinglyLinkedList peopleLinkedList = (SinglyLinkedList) originalLinkedList;
		

		//existence flags
		boolean passwordExists = false;
		boolean userExists = false;
		//data validation

		
		try {
			
			//alternate way, new user
			if(accessData.length==4) {
				Person newPerson = (Person) registration(accessData[3], accessData[0], accessData[1], personasFile);
				sync(peopleLinkedList, newPerson);
			}
			
			for(int i = 0; i<peopleLinkedList.getTotalElements(); i++) {
				Person personFromLinkedList = (Person) peopleLinkedList.getDataFromList(i);	
				//common login
				if(accessData[0].equals(personFromLinkedList.getRut())) {
					userExists = true;
					System.out.println("TRACE0");
					if(accessData[1].equals(personFromLinkedList.getPassword())) {
						passwordExists = true;
						System.out.println("TRACE1");
					}
				}
				
				if (passwordExists == true && userExists == true) {
					System.out.println("TRACEF");
					switch(personFromLinkedList.getClearance()) {
					case("Usuario"):
						MenuMainframe.userMenu(personFromLinkedList, textos, reservas, devoluciones);
						break;
					case("Trabajador"):
						MenuMainframe.workerMenu(personFromLinkedList, textos, reservas, devoluciones);
						break;
					}
					break;
				}		
				
			}
				
		}catch(Exception e){
			System.out.println("Parameter not found");
			e.printStackTrace();
		}
	}

	public void logout() {
		// TODO Auto-generated method stub
		
	}
	public void checkIfExistsOnFile(String chechkIfExists) {
		
	}
	
	public Object registration(String name, String rut, String pass, File file) {
		
		String newUser = name+","+rut+","+pass+","+"Usuario";
		save(file, newUser);
		Person newPerson = new Person(name, rut, pass, "Usuario");
		
		return newPerson;
	}
	
	public void sync(SinglyLinkedList listToSync, Object newData) {
		listToSync.insert(newData);
	}
	
	
	
	
	
	
	//morph methods
	private Object morphIntoTexts(String[] line) {
		Object text = null;
		
		switch (line[4]) {
		case("Libro"):
			Books currentBook = new Books(Integer.parseInt(line[0]), Integer.parseInt(line[1]), 
										  line[2], line[3], line[4], line[5], line[6]);
			text = currentBook;
			break;
		case("Comic"):
			Comics currentComic = new Comics(Integer.parseInt(line[0]), Integer.parseInt(line[1]), 
										  line[2], line[3], line[4], line[5], line[6]);
			text = currentComic;
			break;
		case("Apuntes"):
			Notes currentNotes = new Notes(Integer.parseInt(line[0]), Integer.parseInt(line[1]), 
										  line[2], line[3], line[4], line[5]);
			text = currentNotes;
			break;
		case("Paper"):
			Papers currentPaper = new Papers(Integer.parseInt(line[0]), Integer.parseInt(line[1]), 
										  line[2], line[3], line[4], line[5]);
			text = currentPaper;
			break;
		default:
			text = null;
			System.out.println("No se ha reconocido el texto");
			break;
		}
		
		return text;
		
	}
	
	private Object morphIntoPeople(String[] line) {
		Person currentPerson = new Person(line[0], line[1], line[2], line[3]);
		return currentPerson;
	}
	
	private Object morphIntoDevolution(String[] line) {
		Devolutions currentDevolution = new Devolutions(Integer.parseInt(line[0]), 
														Integer.parseInt(line[1]), line[2],
														line[3], line[4]);
		return currentDevolution;
	}
	
	private Object morphIntoBookings(String[] line){
		Bookings currentBooking = new Bookings(Integer.parseInt(line[0]), line[1],
											   Integer.parseInt(line[2]), line[3], line[4]);
		return currentBooking;
	}

}
