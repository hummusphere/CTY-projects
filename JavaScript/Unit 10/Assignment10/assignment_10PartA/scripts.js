class Student {
    constructor(name, age, id, favorite_subject, books_checked_out) {
        this.name  = name;
        this.age  = age;
        this.id = id
        this.favorite_subject  = favorite_subject;
        this.books_checked_out  = books_checked_out;
    }

    displayInformation() {
        return ("Student Name : " + this.name + "\n Student Id : " + this.id + "\n Student Age : " + this.age +  "\n Favorite Subject : " + this.favorite_subject + "\n List of Checked Out Books : " + this.books_checked_out)
    }
}


John = new Student("John", "14", "1230", "Math", ["The Art of War", "Harry Potter"])
Elliot = new Student("Elliot", "15", "4090", "Science", ["Allies", "Grenade", "The Odyssey"])
Samuel = new Student("Samuel", "15", "8129", "English", ["Lord of The Rings", "Tunnel of Bones", "The Communist Manifesto"])


alert(John.displayInformation())
alert(Elliot.displayInformation())
alert(Samuel.displayInformation())