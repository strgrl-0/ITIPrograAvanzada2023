package textClass;

public class Papers extends Textos{
	private String researchArea;
	private String doi;
	
	public Papers(int pubYear, int textCode,String mainAuthor, 
			      String textName,String researchArea, String doi) {
		super(pubYear, textCode, mainAuthor, textName);
		this.researchArea = researchArea;
		this.doi = doi;
	}
	//getters & setters
	public String getResearchArea() {
		return researchArea;
	}
	public void setResearchArea(String researchArea) {
		this.researchArea = researchArea;
	}
	public String getDoi() {
		return doi;
	}
	public void setDoi(String doi) {
		this.doi = doi;
	}
}
