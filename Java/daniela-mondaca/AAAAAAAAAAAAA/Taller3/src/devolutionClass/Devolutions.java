package devolutionClass;

public class Devolutions {
	private int devolutionCode;
	private int bookingCode;
	private String originalReturnDate;
	private String finalReturnDate;
	private String debtStatus;
	
	public Devolutions(int devolutionCode, int bookingCode, String originalReturnDate,
					   String finalReturnDate, String debtStatus) {
		this.devolutionCode = devolutionCode;
		this.bookingCode = bookingCode;
		this.originalReturnDate = originalReturnDate;
		this.finalReturnDate = finalReturnDate;
		this.debtStatus = debtStatus;
	}
}
