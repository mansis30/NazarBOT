import customtkinter as ctk
import threading
import sys
import os
from main import run_nazar_scan # Ensure your main logic is in a function

class NazarDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("NazarBOT v1.0 | Cyber Intelligence Dashboard")
        self.geometry("1000x650")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Layout Configuration
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar for Status
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.logo = ctk.CTkLabel(self.sidebar, text="NazarBOT", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.status_label = ctk.CTkLabel(self.sidebar, text="● System Ready", text_color="green")
        self.status_label.grid(row=1, column=0, padx=20, pady=10)

        # Main Workspace
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        self.label = ctk.CTkLabel(self.main_frame, text="Target Reconnaissance", font=ctk.CTkFont(size=16))
        self.label.pack(pady=(20, 10))

        # Search Input
        self.entry = ctk.CTkEntry(self.main_frame, placeholder_text="Enter Name or Phone Number...", width=450)
        self.entry.pack(pady=10)

        self.scan_btn = ctk.CTkButton(self.main_frame, text="Initiate Protocol", command=self.start_thread)
        self.scan_btn.pack(pady=10)

        # Output Console (The "Terminal" look)
        self.console = ctk.CTkTextbox(self.main_frame, width=750, height=400, font=("Consolas", 12), fg_color="#0a0a0a", text_color="#00FF00")
        self.console.pack(pady=20, padx=20)
        
        # Redirect stdout so prints show up in the textbox
        sys.stdout = self

    def write(self, text):
        """Standard output redirection to the GUI textbox."""
        self.console.insert("end", text)
        self.console.see("end")

    def flush(self):
        pass # Required for sys.stdout redirection

    def start_thread(self):
        """Runs the scan in a background thread to prevent UI freezing."""
        target = self.entry.get()
        if not target:
            self.console.insert("end", "[!] Error: No target specified.\n")
            return
            
        self.status_label.configure(text="● Scanning...", text_color="orange")
        self.scan_btn.configure(state="disabled")
        
        # Start the background task
        thread = threading.Thread(target=self.execute_scan, args=(target,))
        thread.daemon = True
        thread.start()

    def execute_scan(self, target):
        """The actual logic executed by the thread."""
        try:
            run_nazar_scan(target) # This calls your existing modules
        except Exception as e:
            print(f"[!] System Error: {str(e)}")
        finally:
            self.status_label.configure(text="● Scan Complete", text_color="cyan")
            self.scan_btn.configure(state="normal")

if __name__ == "__main__":
    app = NazarDashboard()
    app.mainloop()