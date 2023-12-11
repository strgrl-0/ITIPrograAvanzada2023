package system;

public class SinglyLinkedList {
	
	
	class Node{
		private Object data;
		private Node next;
		
		public Node(Object data) {
			this.data = data;
			this.next = null;
		}
		
		public Object getData() {
			return this.data;
		}
	}
		
	Node head = null; 
	Node tail = null;
	
	public void insert(Object data) {
		Node current = new Node(data);
		if(head == null) {
			head = current;
			tail = current;
		}else {
			tail.next = current;
			tail = current;
		}
	}
	
	public void printListContents() {
		Node current = head;
		if(head==null) {
			System.out.println("The list is empty");
		}
		
		while(current!=null) {
			System.out.println(current.data);
			current = current.next;
		}
	}
	
	public int getTotalElements() {
		Node current = head; int total = 0;
		if(head==null) {
			return total;
		}
		
		while(current!=null) {
			total++;
			current = current.next;
		}
		
		return total;
	}
	
	public Object getDataFromList(int index) {
		Node current = head;
		for(int i = 0; i<index; i++){
			current = current.next;
		}
		return current.data;
	}
	
	
	
}
