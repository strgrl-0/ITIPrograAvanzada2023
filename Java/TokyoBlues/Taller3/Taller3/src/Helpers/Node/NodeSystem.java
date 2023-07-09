package Helpers.Node;

import MainClasses.StatHuman;

public class NodeSystem {
    private Node head = null;
    private Node tail = null;

    public NodeSystem(){
        
    }

    public boolean add(StatHuman data){
        Node current = new Node(data);

        if(head == null){
            this.head = current;
            this.tail = current;
            return true;
        }

        tail.setNext(current);
        tail = current;
        return true;
    }

    public StatHuman find(String name){
        if(head == null){
            return null;
        }

        Node current = head;

        while(current != null){
            current = current.getNext();
            String currentId = current.getData().getUniqueName();

            if(currentId == name){
                return current.getData();
            }
        }

        return null;
    }

    public boolean delete(String name){
        if(head == null){
            return false;
        }

        Node current = head;
        Node prev = current;

        while (current != null){
            current = current.getNext();
            String currentId = current.getData().getUniqueName();

            if(currentId == name){
                prev.setNext(current.getNext());
                return true;
            }
        }

        return false;
    }
}
