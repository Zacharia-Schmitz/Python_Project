# Python Project

**checkbookmvp.py** is the minimum viable product. Once I had that I started working on the bonus.

**checkbookbonus.py** has the following bonus features:
- timestamps on the ledger
- option for transaction descriptions
- an option to view previous transactions input by the user

### Things learned:

**os library (operating system)**
 - operating system library, utilized for ease of access to file system
 - specifically used os.path

 **date time library**
 - allowed for ease of manipulating date and time
 - specifically used datetime.datetime.now().strftime to format the time as I wanted it.

 **try-except statement**
 - used this for trying to convert a user input to a float if they type something else.
 - TRY to convert to a float
 - EXCEPT if it can't, do this. In my case I used return.



---
## The Project: Build a .py file that will be run from the command line.

- When run, the application should welcome the user, and prompt them for an action to take:
    - view current balance
    - add a debit (withdrawal)
    - add a credit (deposit)
    - exit

- The application should notify the user if the input is invalid and prompt for another choice.

- The application should persist between times that it is run.

---

### Bonus Features:

- Add a menu item that allows the user to view all historical transactions
- Assign categories to each transaction
- Add a menu item to allow the user to view all the transactions in a given category
- Provide the user with summary statistics about the transactions in each category
- Keep track of the date and time that each transaction happened
- Allow the user to view all the transactions for a given day
- Hint: Make sure your list of previous transactions includes the timestamp for each
- Allow the user to optionally provide a description for each transaction
- Allow the user to search for keywords in the transaction descriptions, and show all the transactions that match the user's search term
- Allow the user to modify past transactions
