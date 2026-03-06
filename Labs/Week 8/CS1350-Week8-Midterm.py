# CS1350 - Computer Science II
# Cody Burton
# 3/6/2026
# CS1350-Week8-Midterm.py

# Problem 1: Contact Manager (Dictionaries)

#Write a class ContactBook that stores contacts in a dictionary mapping names to a dictionary of
# {"phone": str, "email": str}.

#Methods to implement:
# add_contact(name, phone, email): Adds a contact to the book. If it already exists, it should update the phone and email.
# search(query): Returns a list of names where query (case-insensitive) appears in the name, phone, or email.
# merge(other_book): Merges another ContactBook into this one, combining contacts. If a contact exists in both, the other_book's info should overwrite this book's info.
# export_csv(): Returns a single string with one line per contact in the format "name,phone,email". The contacts should be sorted alphabetically by name.

class ContactBook:
    def __init__(self):
        self.contacts = {}
        
    def add_contact(self, name, phone, email):
        self.contacts[name] = {"phone": phone, "email": email}
        
    def search(self, query):
        query = query.lower()
        results = []
        for name, info in self.contacts.items():
            if (query in name.lower() or 
                query in info["phone"].lower() or 
                query in info["email"].lower()):
                results.append(name)
        return results
    
    def merge(self, other_book):
        for name, info in other_book.contacts.items():
            self.contacts[name] = info

    def export_csv(self):
        lines = []
        for name in sorted(self.contacts.keys()):
            info = self.contacts[name]
            lines.append(f"{name},{info['phone']},{info['email']}")
        return "\n".join(lines)

# Test cases
print("=" * 10 + " Problem 1 " + "=" * 10)

book1 = ContactBook()
book1.add_contact("Alice Smith", "555-1234", "alice@mail.com")
book1.add_contact("Bob Jones", "555-5678", "bob@work.com")
book1.add_contact("Carol White", "555-9999", "carol@mail.com")

# Search
print(book1.search("alice"))
# ['Alice Smith']
print(book1.search("555"))
# ['Alice Smith', 'Bob Jones', 'Carol White']
print(book1.search("mail.com"))
# ['Alice Smith', 'Carol White']

# Merge
book2 = ContactBook()
book2.add_contact("Alice Smith", "555-0000", "alice@new.com") # Updated info
book2.add_contact("Dave Brown", "555-4444", "dave@mail.com") # New contact
book1.merge(book2)

# Export
print(book1.export_csv())
# Alice Smith,555-0000,alice@new.com
# Bob Jones,555-5678,bob@work.com
# Carol White,555-9999,carol@mail.com
# Dave Brown,555-4444,dave@mail.com

# Problem 2: Event Planner with Sets

# Write the following for a volunteer scheduling system:
# 1.) class Event with:
#   Constructor that takes a name and a set of volunteers (strings).
#   add_volunteer(name): Adds a volunteer to the event.
#   remove_volunteer(name): Removes a volunteer from the event. If the volunteer is not in the event, it should do nothing.
#   volunteer_count(): Returns number of volunteers

# 2.) Standalone functions:
# find_overcommitted(events, max_events): returns a set of volunteers signed up for more than max_events events.
# find_availiable(all_volunteers, events): takes a set of all volunteers and a list of events, and returns a set of volunteers who are not signed up for any events.
# schedule_conflict(event1, event2): returns a set of volunteers who are signed up for both events.

class Event:
    def __init__(self, name):
        self.name = name
        self.volunteers = set()

    def add_volunteer(self, name):
        self.volunteers.add(name)

    def remove_volunteer(self, name):
        self.volunteers.discard(name)

    def volunteer_count(self):
        return len(self.volunteers)

def find_overcommitted(events, max_events):
    volunteer_counts = {}
    for event in events:
        for volunteer in event.volunteers:
            volunteer_counts[volunteer] = volunteer_counts.get(volunteer, 0) + 1
    return {v for v, count in volunteer_counts.items() if count > max_events}
    
def find_available(all_volunteers, events):
    signed_up = set()
    for event in events:
        signed_up.update(event.volunteers)
    return all_volunteers - signed_up

def schedule_conflict(event1, event2):
    return event1.volunteers.intersection(event2.volunteers)

# Test cases
print("=" * 10 + " Problem 2 " + "=" * 10)

setup = Event("Setup")
for v in ["Alice", "Bob", "Carol", "Dave"]:
    setup.add_volunteer(v)
    
ceremony = Event("Ceremony")
for v in ["Carol", "Dave", "Eve", "Frank"]:
    ceremony.add_volunteer(v)
    
cleanup = Event("Cleanup")
for v in ["Alice", "Dave", "Frank", "Grace"]:
    cleanup.add_volunteer(v)
    
print(f"Setup: {setup.volunteer_count()} volunteers") # 4
print(f"Ceremony: {ceremony.volunteer_count()} volunteers") # 4

# Conflicts
print(schedule_conflict(setup, ceremony)) # {'Carol', 'Dave'}

# Overcommitted (signed up for more than 2 events)
events = [setup, ceremony, cleanup]
print(find_overcommitted(events, 2)) # {'Dave'}

# Available (not signed up for anything)
everyone = {"Alice", "Bob", "Carol", "Dave", "Eve", "Frank", "Grace", "Hank"}
print(find_available(everyone, events)) # {'Hank'}