package system;

import personClass.Person;

public interface ClientMenuInterface {
	public void userMenu(Person person, SinglyLinkedList texts, SinglyLinkedList bookings,
						 SinglyLinkedList devolutions);
	public void workerMenu(Person person, SinglyLinkedList texts, SinglyLinkedList bookings,
						   SinglyLinkedList devolutions);
}
