package textClass;

public abstract class Textos {
	private int pubYear;
	private int textCode;
	private String mainAuthor;
	private String textName;
	

	//getters & setters
	
	public Textos(int pubYear, int textCode, String mainAuthor, String textName) {
		this.pubYear = pubYear;
		this.textCode = textCode;
		this.mainAuthor = mainAuthor;
		this.textName = textName;
	}
	public int getPubYear() {
		return pubYear;
	}
	public void setPubYear(int pubYear) {
		this.pubYear = pubYear;
	}
	public int getTextCode() {
		return textCode;
	}
	public void setTextCode(int textCode) {
		this.textCode = textCode;
	}
	public String getMainAuthor() {
		return mainAuthor;
	}
	public void setMainAuthor(String mainAuthor) {
		this.mainAuthor = mainAuthor;
	}
	public String getTextName() {
		return textName;
	}
	public void setTextName(String textName) {
		this.textName = textName;
	}
	
	
}
