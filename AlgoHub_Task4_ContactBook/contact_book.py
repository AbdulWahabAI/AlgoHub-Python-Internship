from collections import deque
import heapq
from sorting_algos import optimized_sort

def run_contact_book():
    # 1. Dictionaries & Sets (Week 4 Concepts)[span_3](start_span)[span_3](end_span)
    contacts_dict = {}
    unique_emails = set()
    
    # 2. Queue using collections.deque (Week 4 Models/Tools)[span_4](start_span)[span_4](end_span)
    recent_searches = deque(maxlen=5)
    
    # Priority Queue tracking using heapq (Week 4 Tools)[span_5](start_span)[span_5](end_span)
    priority_queue_list = [] 

    while True:
        print("\n--- ALGOHUB WEEK 4: CONTACT BOOK APP (CLI) ---")
        print("1. Add Contact")
        print("2. View All Contacts (Sorted)")
        print("3. Search Contact (Queue Tracked)")
        print("4. View Recent Searches (Queue)")
        print("5. View Priority/Favorite Contacts (Heapq)")
        print("6. Delete Contact")
        print("7. Exit")
        
        choice = input("Select an option (1-7): ").strip()
        
        if choice == '1':
            name = input("Enter Name: ").strip()
            phone = input("Enter Phone: ").strip()
            email = input("Enter Email: ").strip()
            try:
                priority = int(input("Enter Priority (1 for High, 2 for Normal): ").strip())
            except ValueError:
                priority = 2

            if phone in contacts_dict:
                print("Error: Contact with this phone number already exists!")
            elif email in unique_emails:
                print("Error: Email already registered in sets!")
            else:
                # Storing in Dictionaries
                contacts_dict[phone] = {
                    'name': name,
                    'phone': phone,
                    'email': email,
                    'priority': priority
                }
                # Adding to Set for uniqueness[span_6](start_span)[span_6](end_span)
                unique_emails.add(email)
                
                # Using heapq for priority management[span_7](start_span)[span_7](end_span)
                heapq.heappush(priority_queue_list, (priority, name, phone))
                
                print(f"Success: '{name}' added successfully!")
                
        elif choice == '2':
            if not contacts_dict:
                print("Contact book is empty.")
            else:
                contact_list = list(contacts_dict.values())
                # Using Week 4 sorting approach[span_8](start_span)[span_8](end_span)
                sorted_contacts = optimized_sort(contact_list)
                
                print("\n--- SORTED CONTACTS LIST ---")
                for idx, c in enumerate(sorted_contacts, 1):
                    print(f"{idx}. {c['name']} | Phone: {c['phone']} | Email: {c['email']} | Priority: {c['priority']}")
                    
        elif choice == '3':
            query = input("Enter name to search: ").strip().lower()
            found = False
            print("\n--- SEARCH RESULTS ---")
            for phone, info in contacts_dict.items():
                if query in info['name'].lower():
                    print(f"Found -> Name: {info['name']}, Phone: {info['phone']}")
                    # Adding search query to Queue (collections.deque)[span_9](start_span)[span_9](end_span)
                    recent_searches.append(info['name'])
                    found = True
            if not found:
                print("No matching contact found.")
                
        elif choice == '4':
            print("\n--- RECENT SEARCH QUEUE (deque) ---")
            if not recent_searches:
                print("No recent searches.")
            else:
                for item in recent_searches:
                    print(f"- Searched: {item}")
                    
        elif choice == '5':
            print("\n--- PRIORITY CONTACTS (Heapq) ---")
            if not priority_queue_list:
                print("No priority contacts available.")
            else:
                for p, name, phone in sorted(priority_queue_list):
                    print(f"Priority {p}: {name} ({phone})")
                    
        elif choice == '6':
            del_phone = input("Enter phone number to delete: ").strip()
            if del_phone in contacts_dict:
                removed = contacts_dict.pop(del_phone)
                unique_emails.remove(removed['email'])
                print(f"Contact '{removed['name']}' deleted.")
            else:
                print("Phone number not found.")
                
        elif choice == '7':
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Choose between 1 and 7.")

if __name__ == "__main__":
    run_contact_book()