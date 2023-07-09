package Helpers.Node;

import MainClasses.StatHuman;

public class Node {
    private StatHuman data;
    private Node next;

    public Node(StatHuman data){
        this.data = data;
    }

    public void setNext(Node next){
        this.next = next;
    }

    public void setData(StatHuman data){
        this.data = data;
    }

    public Node getNext(){
        return next;
    }

    public StatHuman getData(){
        return data;
    }
}
