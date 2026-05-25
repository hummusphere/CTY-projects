function calculateTotal()
{
      //Don't change the code below
      var customerName = document.getElementById("name").value;
      var fruitName = document.getElementById("fruits");
      var i = fruitName.selectedIndex;
      var itemName = fruitName.options[i].text;
      var itemQuantity = document.getElementById("qty").value;
      var unitPrice = document.getElementById("unitPrice").value;
      var tax = document.getElementById("tax");
      var l = tax.selectedIndex;
      var salesTaxRate = tax.options[l].value;
      var output = "";
      // Don't change the code above
      
      /*
        Use the variables 
          i. customerName
         ii. itemName
        iii. itemQuantity
         iv. unitPrice, and 
          v. salesTaxRate 
         vi. output (to display your output)
        to do your assignment */
      
      //Start your code here

      var totalPrice = unitPrice * itemQuantity;
      var totalTax = totalPrice * salesTaxRate;
      var grandTotal = totalTax+totalPrice

      document.write("Customer Name : " + customerName + "<br>") 
      document.write("Item Name : " + itemName + "<br>")
      document.write("Item Quantity : " + itemQuantity+ "<br>")
      document.write("Unit Price : $" + unitPrice + "<br>")
      document.write("<br>")
      document.write("Total Price : $" + totalPrice + "<br>")
      document.write("Total Tax : $" + totalTax + " <br>")
      document.write("Grand Total : $" + grandTotal + " <br>")

      //Don't change the code below         
      document.getElementById("output").innerHTML = output;
}

