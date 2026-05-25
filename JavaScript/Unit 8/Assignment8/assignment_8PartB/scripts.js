var deleteData, saveData, loadData, data, title;

saveData = function() {
    title = prompt("What title would you like to store this under?")
    data = prompt("What data would you like to store?")
    localStorage.setItem(title, data)
    alert("Data Saved.")
}


deleteData = function() {
    localStorage.clear()
    alert("Data Cleared.")
}
loadData = function() {
    title = prompt("What title was your data stored in?")
    data = localStorage.getItem(title)
    if (data == null) {
        alert("No data found.")
    } else {
        alert(data)
    }
}

