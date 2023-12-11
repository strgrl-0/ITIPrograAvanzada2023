package main;

import system.*;
import textClass.*;
import java.io.File;

public class Main {

	public static void main(String[] args) {
		Mainframe mainframe = new Mainframe();
		//preload
		////Load file
		File textos = new File("src/files/textos.txt");
		File reservas = new File("src/files/reservas.txt");
		File personas = new File("src/files/personas.txt");
		File devoluciones = new File("src/files/devoluciones.txt");
		
		SinglyLinkedList textosMain = (SinglyLinkedList) mainframe.read(textos);
		SinglyLinkedList reservasMain = (SinglyLinkedList) mainframe.read(reservas);
		SinglyLinkedList personasMain = (SinglyLinkedList) mainframe.read(personas);
		SinglyLinkedList devolucionesMain = (SinglyLinkedList) mainframe.read(devoluciones);
		
		textosMain.printListContents();
		reservasMain.printListContents();
		personasMain.printListContents();
		devolucionesMain.printListContents();
		
		mainframe.login(personasMain, textosMain, reservasMain, devolucionesMain,
						textos, reservas, personas, devoluciones);

	}

}
