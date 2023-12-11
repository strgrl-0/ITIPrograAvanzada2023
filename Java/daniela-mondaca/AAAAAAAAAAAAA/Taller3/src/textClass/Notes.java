package textClass;

public class Notes extends Textos {
	private String associatedClass;
	private String associatedCareer;
	
	public Notes(int pubYear, int textCode,String mainAuthor, 
			     String textName, String associatedClass, String associatedCareer) {
		super(pubYear, textCode, mainAuthor, textName);
		this.associatedClass = associatedClass;
		this.associatedCareer = associatedCareer;
	}
	//getters & setters
	
	public String getAssociatedClass() {
		return associatedClass;
	}
	public void setAssociatedClass(String associatedClass) {
		this.associatedClass = associatedClass;
	}
	public String getAssociatedCareer() {
		return associatedCareer;
	}
	public void setAssociatedCareer(String associatedCareer) {
		this.associatedCareer = associatedCareer;
	}
}
