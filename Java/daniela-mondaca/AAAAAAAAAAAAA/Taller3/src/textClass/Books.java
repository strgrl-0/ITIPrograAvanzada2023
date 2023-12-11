package textClass;

public class Books extends Textos {
	private String editorial;
	private String literaryGenre;
	private String edition;
	
	public Books(int pubYear, int textCode,String mainAuthor, 
				 String textName, String editorial, String literaryGenre, String edition){
		super(pubYear, textCode, mainAuthor, textName);
		
		this.editorial = editorial;
		this.literaryGenre = literaryGenre;
		this.edition = edition;
	}

	//getters & setters
	public String getEditorial() {
		return editorial;
	}
	public void setEditorial(String editorial) {
		this.editorial = editorial;
	}
	public String getLiteraryGenre() {
		return literaryGenre;
	}
	public void setLiteraryGenre(String literaryGenre) {
		this.literaryGenre = literaryGenre;
	}
	public String getEdition() {
		return edition;
	}
	public void setEdition(String edition) {
		this.edition = edition;
	}
	
}
