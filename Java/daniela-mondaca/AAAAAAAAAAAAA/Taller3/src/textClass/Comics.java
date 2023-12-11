package textClass;

public class Comics extends Textos{
	private String edCompany;
	private String comicGenre;
	private String seriesNumber;
	
	public Comics(int pubYear, int textCode,String mainAuthor, 
			 	  String textName, String edCompany, String comicGenre, String seriesNumber) {
		super(pubYear, textCode, mainAuthor, textName);
		this.edCompany = edCompany;
		this.comicGenre = comicGenre;
		this.seriesNumber = seriesNumber;
	}
	//getters & setters
	
	public String getEdCompany() {
		return edCompany;
	}
	public void setEdCompany(String edCompany) {
		this.edCompany = edCompany;
	}
	public String getComicGenre() {
		return comicGenre;
	}
	public void setComicGenre(String comicGenre) {
		this.comicGenre = comicGenre;
	}
	public String getSeriesNumber() {
		return seriesNumber;
	}
	public void setSeriesNumber(String seriesNumber) {
		this.seriesNumber = seriesNumber;
	}
}
