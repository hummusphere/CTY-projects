//Write code to create an array for your book catalog.
bookData = [];


function AddBooks()
{
	//Write code to create a new book object with a title, an author.
	var bookName = prompt("What is the name of this book?")
	var authorName = prompt("Who is the author of this book?")

	//Give the book a property of isCheckedOut and set it to false.
	//Add the new book object to the array.
	bookData.push(book = {name: bookName, author: authorName, isCheckedOut: false})
	alert("Book added!")


	
	
}


function ShowBooks()
{

	//Loop through the array and display each book object's properties to the user. Use alerts.
	numOfBooks = bookData.length;
	if (numOfBooks > 0) {
		for (var i = 0; i < numOfBooks; i++) {
			//Be sure to display the information in a clear way.
			alert("Book Name : " + String(bookData[i].name) + "\n" + "Authors Name : " + bookData[i].author + "\n" + "Number in Catalog : " + String(i) + "\n" + "Is Checked Out : " + String(bookData[i].isCheckedOut))
		}
	} else {
		alert("No books found.")
	}

}

function CheckOutBook()
{	
	numOfBooks = bookData.length;
	if (numOfBooks > 0) {
		for (var i = 0; i < numOfBooks; i++) {
			//Loop through each book in the catalog. Display the book title and ask if this is the book that the user is checking out.
			if (bookData[i].isCheckedOut == false) {
				var response = prompt("Book Name : " + bookData[i].name + "\n" + "Authors Name : " + bookData[i].author + "\n" + "Number in Catalog : " + String(i) + "\n" + "Is this the book you wanted to check out? (yes or no).")
				if (response == "yes") {
					//If they say yes, end the loop and change that books' information so it is checkoutedOut
					bookData[i].isCheckedOut = true
					break;
				} else if (response == "no") {
					continue;
				} else {
					alert("You did not type a lowercase yes or no.");
				}
			}
		}
	} else {
		alert("No books are in the catalog.")
	}
}

function ReturnBook()
{

	numOfBooks = bookData.length;
	if (numOfBooks > 0) {
		for (var i = 0; i < numOfBooks; i++) {
			//Loop through each book in the catalog. Display the book title and ask if this is the book that the user is returning.
			if (bookData[i].isCheckedOut == true) {
				var response = prompt("Book Name : " + bookData[i].name + "\n" + "Authors Name : " + bookData[i].author + "\n" + "Number in Catalog : " + String(i) + "\n" + "Is this the book you wanted to return? (yes or no).")
				if (response == "yes") {
						//If they say yes, end the loop and change that books' information so it is checkoutedOut
					bookData[i].isCheckedOut = false
					break;
				} else if (response == "no") {
					continue;
				} else {
					alert("You did not type a lowercase yes or no.");
				}
			}
		}
	} else {
		alert("No books are in the catalog.")
	}
}
