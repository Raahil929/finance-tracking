# Finance logger

## Overview
This is a modular, object-oriented **Python application** that allows users to log and manage financial records. Unlike the first version, this implementation introduces **new naming conventions**, **alternative class structures**, and **different expense categories**. The program works entirely via command line and saves all data in a JSON file for persistence.

---

## Features

- Add new financial records  
- Delete records by ID  
- View all saved records, with optional sorting  
- Saves and loads data from `records.json`  

---

## Supported Categories

Users can log expenses under the following categories:

- **Healthcare**: Doctor, Pharmacy, Hospital, Insurance  
- **Entertainment**: Movies, Concerts, Games  
- **Subscription**: Netflix, Spotify, Gym  
- **Miscellaneous**: Anything else, no tag needed

---

## Record Format

Each record contains:

- Unique ID
- Category (e.g., Subscription)
- Cost (e.g., 59.99)
- Tag (e.g., Netflix, Doctor)
- Date (in `YYYY-MM-DD` format)

---

## Object-Oriented Concepts Used

| OOP Concept    | Description                                                                     |
|----------------|---------------------------------------------------------------------------------|
| Abstraction     | `Record` class abstracts the data fields of a financial entry                  |
| Inheritance     | While not subclassed here, logic was organized through modular components      |
| Polymorphism    | Multiple modules interact using shared method structures (`details`, `all`)    |
| Encapsulation   | Private variables inside the `Record` class ensure internal state protection   |

---

## Design Patterns Used

| Pattern            | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| Factory Pattern    | `RecordFactory` dynamically creates record objects                          |
| Singleton Pattern  | `StorageHandler` manages file access and data persistence from one place    |



## Example Input Flow

--- Finance Log Menu ---

1. Add Record

2. Delete Record

3. View Records

4. Exit


### When adding a record:

- Enter category (Healthcare, Entertainment, etc.)
- Enter cost (e.g., 250.50)
- Enter a tag (e.g., Netflix)
- Enter date (YYYY-MM-DD)


## Example Output

ID : 3

Category : Subscription

Cost : $15.00

Tag : Netflix

Date : 2025-05-01



---

## Error Handling

- Incorrect amount → prompts again  
- Invalid date format → shows correct format and retries  
- Invalid ID during delete → shows warning  
- JSON errors are handled safely during load/save  

---

## How to Run

1. Make sure Python 3 is installed.
2. Run:

    ```bash
    python main.py
    ```

## Conclusion

- All records persist across sessions via records.json

- The code is structured for maintainability and testing

- Easily expandable for new features or more expense types
