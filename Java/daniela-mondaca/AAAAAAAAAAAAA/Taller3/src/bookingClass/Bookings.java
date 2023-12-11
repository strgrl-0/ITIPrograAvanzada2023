package bookingClass;

public class Bookings {
	private int bookingCode;
	private String associatedRut;
	private int objectCode;
	private String bookingDate;
	private String returnDate;
	
	public Bookings (int bookingCode, String associatedRut, int objectCode, 
					String bookingDate, String returnDate) {
		this.bookingCode = bookingCode;
		this.associatedRut = associatedRut;
		this.objectCode = objectCode;
		this.bookingDate = bookingDate;
		this.returnDate = returnDate;
	}

	public int getBookingCode() {
		return bookingCode;
	}

	public void setBookingCode(int bookingCode) {
		this.bookingCode = bookingCode;
	}

	public String getAssociatedRut() {
		return associatedRut;
	}

	public void setAssociatedRut(String associatedRut) {
		this.associatedRut = associatedRut;
	}

	public int getObjectCode() {
		return objectCode;
	}

	public void setObjectCode(int objectCode) {
		this.objectCode = objectCode;
	}

	public String getBookingDate() {
		return bookingDate;
	}

	public void setBookingDate(String bookingDate) {
		this.bookingDate = bookingDate;
	}

	public String getReturnDate() {
		return returnDate;
	}

	public void setReturnDate(String returnDate) {
		this.returnDate = returnDate;
	}
}
