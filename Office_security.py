class OfficeSecurityApp:
    def __init__(self):
        
        self.visitors_log =[]
        
        self.security_alerts =[]
    def display_menu(self):
        print("\n---Office Security System ---")
        
        print("1. Login")
        
        print("2. Add Visitor")
        
        print("3. View Visitors Log")
        
        print("4. Issue Security Alert")
        
        print("5. View Security Alerts")
        
        print("6. Exit")
    def login(self):
          print("\n--- Login ---")
          username = input("Enter username: ")
          
          password = input("Enter password: ")
          
          print("Login successful!")
    def add_visitor(self):
        print("\n--- Add Visitor ---")
        name = input("Enter visitor's name: ")  
        purpose = input("Enter purpose of visit: ") 
        self.visitors_log.append({'name':name,'purpose':purpose})
        
        print(f"Visitor'{name}' added to the log")
    def view_visitors_log(self):
        print("\n--- Visitors Log ---")
        if not self.visitors_log:
            print("No visitors logged.")
        else:
            
            for idx,visitor in enumerate(self.visitors_log,start=1):
                print(f"{idx}. Name:{visitor['name']},Purpose:{visitor['purpose']}")
    def issue_security_alert(self):
        print("\n---Issue Security Alert ---") 
        alert_message  = input("Enter alert message: ")
        self.security_alerts.append(alert_message)        
        print("Security alert issued.")
    def view_security_alerts(self):
        
        print("\n---Security Alerts ---")
        if not self.security_alerts:
            print("No security alerts issued.")
        else:
            for idx,alert in enumerate(self.security_alerts,start=1):
                print(f"{idx}.{alert}")
    def run(self):
        while True:
            self.display_menu()
            choice = input("Select an option(1-6):")
            if choice =='1':
                self.login()
            elif choice =='2':
                self.add_visitor()
            elif choice =='3':
                self.view_visitors_log()
            elif choice =='4':
                self.issue_security_alert()
            elif choice=='5':
                self.view_security_alerts()
            elif choice =='6':
                print("Exiting the system.")        
                
                break
            else:
                print("Invalid option,please try again.")
                
if __name__=="__main__":
    app = OfficeSecurityApp()
    app.run()