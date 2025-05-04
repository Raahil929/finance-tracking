import json
import os

class Record:
    def __init__(self, record_id, category, cost, tag, date_str):
        self.__record_id = record_id
        self.__category = category
        self.__cost = cost
        self.__tag = tag
        self.__date = date_str

    def details(self):
        return {
            "record_id": self.__record_id,
            "category": self.__category,
            "cost": self.__cost,
            "tag": self.__tag,
            "date": self.__date
        }


class RecordFactory:
    @staticmethod
    def create_record(record_id, category, cost, tag, date_str):
        return Record(record_id, category, cost, tag, date_str)

class StorageHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self._data = []
        self._load()

    def _load(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                try:
                    self._data = json.load(f)
                except:
                    self._data = []

    def save_all(self):
        with open(self.file_path, 'w') as f:
            json.dump(self._data, f, indent=2)

    def add(self, record_data):
        self._data.append(record_data)
        self.save_all()

    def remove(self, record_id):
        self._data = [r for r in self._data if r["record_id"] != record_id]
        self.save_all()

    def all(self):
        return self._data.copy()


class RecordValidator:
    @staticmethod
    def float_input(msg):
        while True:
            try:
                return float(input(msg))
            except:
                print("Invalid amount. Try again.")

    @staticmethod
    def date_input(msg):
        while True:
            date_str = input(msg).strip()
            if RecordValidator.valid_date(date_str):
                return date_str
            print("Invalid date. Format: YYYY-MM-DD")

    @staticmethod
    def valid_date(d):
        return len(d) == 10 and d[4] == '-' and d[7] == '-' and d.replace('-', '').isdigit()


class RecordManager:
    def __init__(self):
        self.db = StorageHandler("records.json")
        self.last_id = self._get_last_id()

    def _get_last_id(self):
        all_items = self.db.all()
        return max([i["record_id"] for i in all_items], default=0)

    def insert_record(self):
        print("\nAvailable Categories: Healthcare, Entertainment, Subscription, Miscellaneous")
        cat = input("Enter category: ").strip().capitalize()
        amount = RecordValidator.float_input("Enter cost: ")
        tag = input("Enter a tag (e.g., Doctor, Netflix, etc.): ").strip()
        date = RecordValidator.date_input("Enter date (YYYY-MM-DD): ")

        self.last_id += 1
        rec = RecordFactory.create_record(self.last_id, cat, amount, tag, date)
        self.db.add(rec.details())
        print("Record saved.")

    def delete_record(self):
        try:
            rec_id = int(input("Enter Record ID to remove: "))
            self.db.remove(rec_id)
            print("Deleted successfully.")
        except:
            print("Invalid ID input.")

    def view_all(self):
        records = self.db.all()
        if not records:
            print("No records found.")
            return

        print("\nSort by:\n1. Date\n2. Category\n3. Default")
        opt = input("Choose: ").strip()

        if opt == '1':
            records.sort(key=lambda x: x["date"])
        elif opt == '2':
            records.sort(key=lambda x: x["category"])

        for r in records:
            print("-" * 40)
            print(f"ID       : {r['record_id']}")
            print(f"Category : {r['category']}")
            print(f"Cost     : ${r['cost']:.2f}")
            print(f"Tag      : {r['tag']}")
            print(f"Date     : {r['date']}")
        print("-" * 40)


def main():
    manager = RecordManager()
    while True:
        print("\n--- Finance Log Menu ---")
        print("1. Add Record")
        print("2. Delete Record")
        print("3. View Records")
        print("4. Exit")

        option = input("Choose an option: ").strip()
        if option == "1":
            manager.insert_record()
        elif option == "2":
            manager.delete_record()
        elif option == "3":
            manager.view_all()
        elif option == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()