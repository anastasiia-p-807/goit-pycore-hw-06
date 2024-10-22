import sys
sys.path.append('/AddressBookModule/contact_book')

from AddressBookModule import AddressBook, Record, NewRecord, Name, Phone

# Create an instance of AddressBook
address_book = AddressBook()

# Create a new record using NewRecord
new_record = NewRecord(name=Name("Alice"), phones=[Phone("1234567890")])
address_book.add_record(new_record)

# Find a record by name
record = address_book.find("Alice")
print(record)  # Output: Contact name: Alice, phones: 1234567890

# Edit the found record
if record:
    updated_record = record
    updated_record.phones = [Phone("0987654321")]
    address_book.edit_record(updated_record)

# Get the updated record by id and print it
updated_record = address_book.get(record.id)
print(updated_record)  # Output: Contact name: Alice, phones: 0987654321

# Add another phone to Alice
if updated_record:
    updated_record.add_phone("5555555555")
    print(updated_record)  # Output: Contact name: Alice, phones: 0987654321; 5555555555

# Remove a phone from Alice
updated_record.remove_phone("0987654321")
print(updated_record)  # Output: Contact name: Alice, phones: 5555555555

# Delete the record by name
address_book.delete("Alice")
record_after_deletion = address_book.find("Alice")
print(record_after_deletion)  # Output: None
