import tkinter as tk
from tkinter import Listbox, Scrollbar, scrolledtext, Entry
import pandas as pd
from newspaper import Article
from summarizer import summarize

class MainMenu:
    def __init__(self, master):
        self.master = master
        master.title("Main Menu")

        # Configure main menu window size and position
        width = 300
        height = 200
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        master.geometry(f"{width}x{height}+{x}+{y}")

        # Configure main menu window color
        master.configure(bg="#1a1918")

        # Configure main menu title
        title_label = tk.Label(master, text="Summarizer", font=("Helvetica", 16), bg="#1a1918")
        title_label.pack(pady=20)

        # Buttons to open different windows with styling
        button_style = {"font": ("Helvetica", 12), "width": 20, "height": 2, "bg": "#474646", "fg": "#5e5e5d", "borderwidth": 0}
        
        self.button1 = tk.Button(master, text="Open List of Medium Articles", command=self.open_list_of_articles, **button_style)
        self.button1.pack(pady=10)

        self.button2 = tk.Button(master, text="Enter URL of an Article", command=self.open_window2, **button_style)
        self.button2.pack(pady=10)

        self.button3 = tk.Button(master, text="Enter Custom Text", command=self.open_window3, **button_style)
        self.button3.pack(pady=10)

    def open_list_of_articles(self):
        self.master.withdraw()  # Hide the main menu window
        list_of_articles = tk.Toplevel(self.master)
        ListOfArticles(list_of_articles, self)

    def open_window2(self):
        self.master.withdraw()  # Hide the main menu window
        list_of_articles = tk.Toplevel(self.master)
        URLofArticle(list_of_articles, self)

    def open_window3(self):
        self.master.withdraw()  # Hide the main menu window
        list_of_articles = tk.Toplevel(self.master)
        CustomText(list_of_articles, self)

class CustomText:
    def __init__(self, master, main_menu):
        self.master = master
        self.main_menu = main_menu
        master.title("Custom Summarizer")

        # Configure List of Articles window size and position
        width = 600
        height = 400
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        master.geometry(f"{width}x{height}+{x}+{y}")

        # Configure List of Articles window color
        master.configure(bg="#1a1918")

        # Configure List of Articles title
        title_label = tk.Label(master, text="Enter Custom Text", font=("Helvetica", 16, "bold"), bg="#1a1918")
        title_label.pack(pady=10)
        
        self.input_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=80, height=40, font=("Helvetica", 12))
        self.input_text.pack(pady=10)
        
        # Input box and submit button
        # self.input_var = tk.StringVar()
        # entry = Entry(master, textvariable=self.input_var, font=("Helvetica", 12), width=100)
        # entry.pack(pady=10)

        style = {"font": ("Helvetica", 12), "width": 20, "height": 2, "bg": "#474646", "fg": "#5e5e5d", "borderwidth": 0}
        
        submit_button = tk.Button(master, text="Submit", command=self.submit_input, **style)
        submit_button.pack(pady=10)
        
        back_button = tk.Button(master, text="Back to Main Menu", command=self.back_to_main_menu, **style)
        back_button.pack(pady=10)

    def submit_input(self):
        user_input = self.input_text.get("1.0", tk.END).strip()
        summary = summarize(user_input, 0.6)
        self.show_selected_item(user_input, summary)

    def show_selected_item(self, intext, summary):
        new_window = tk.Toplevel(self.master)
        new_window.title("Custom Text Summary")

        label1 = tk.Label(new_window, text="Custom Text Summary", padx=20, pady=20)
        label1.pack()

        text_widget = scrolledtext.ScrolledText(new_window, wrap=tk.WORD, width=30, height=10, pady=20)
        text_widget.insert(tk.END, summary)
        text_widget.pack(expand=True, fill="both")

        # Add a collapsed section with a button
        section_label = scrolledtext.ScrolledText(new_window, wrap=tk.WORD, width=30, height=10, pady=20)
        section_label.insert(tk.END, intext)
        toggle_button = tk.Button(new_window, text="Show Full Article", command=lambda: self.toggle_section(section_label))
        toggle_button.pack()
        section_label.pack_forget()

    def toggle_section(self, section_label):
        if section_label.winfo_ismapped():
            section_label.pack_forget()
        else:
            section_label.pack(expand=True, fill="both")

    def back_to_main_menu(self):
        self.master.destroy()  # Close the current window
        self.main_menu.master.deiconify()  # Show the main menu window

class ListOfArticles:
    def __init__(self, master, main_menu):
        self.master = master
        self.main_menu = main_menu
        master.title("List of Articles")

        # Configure List of Articles window size and position
        width = 600
        height = 400
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        master.geometry(f"{width}x{height}+{x}+{y}")

        # Configure List of Articles window color
        master.configure(bg="#1a1918")

        # Configure List of Articles title
        title_label = tk.Label(master, text="List of Articles", font=("Helvetica", 16, "bold"), bg="#1a1918")
        title_label.pack(pady=10)
        
        style = {"font": ("Helvetica", 12), "width": 20, "height": 2, "bg": "#474646", "fg": "#5e5e5d", "borderwidth": 0}
        
        back_button = tk.Button(master, text="Back to Main Menu", command=self.back_to_main_menu, **style)
        back_button.pack(pady=10)

        # Create a list of items
        data = pd.read_csv("articles.csv")
        items = [str(i) + '\t\t' + t for i, t in enumerate(data['title'])]

        # Create a listbox and fill it with items
        listbox = Listbox(master, selectmode=tk.SINGLE, font=("Helvetica", 16), bg="#1a1918", fg="#82807f")
        for item in items:
            listbox.insert(tk.END, item)

        # Create a scrollbar for the listbox
        scrollbar = Scrollbar(master, command=listbox.yview)
        listbox.config(yscrollcommand=scrollbar.set)

        # Pack the listbox and scrollbar
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Bind the on_select function to the listbox selection event
        listbox.bind("<<ListboxSelect>>", lambda event: self.on_select(event, data))


    def on_select(self, event, data):
        selected_item = event.widget.get(event.widget.curselection())
        self.show_selected_item(selected_item, data)

    def show_selected_item(self, item, data):
        new_window = tk.Toplevel(self.master)
        i,_,t = item.split('\t')
        new_window.title(t)

        label1 = tk.Label(new_window, text=f"Summarizing Article: {t}", padx=20, pady=20)
        label1.pack()

        summary = summarize(data['text'][int(i)], 0.2)

        text_widget = scrolledtext.ScrolledText(new_window, wrap=tk.WORD, width=30, height=10, pady=20)
        text_widget.insert(tk.END, summary)
        text_widget.pack(expand=True, fill="both")

        # Add a collapsed section with a button
        section_label = scrolledtext.ScrolledText(new_window, wrap=tk.WORD, width=30, height=10, pady=20)
        section_label.insert(tk.END, data['text'][int(i)])
        toggle_button = tk.Button(new_window, text="Show Full Article", command=lambda: self.toggle_section(section_label))
        toggle_button.pack()
        section_label.pack_forget()

    def toggle_section(self, section_label):
        if section_label.winfo_ismapped():
            section_label.pack_forget()
        else:
            section_label.pack(expand=True, fill="both")

    def back_to_main_menu(self):
        self.master.destroy()  # Close the current window
        self.main_menu.master.deiconify()  # Show the main menu window

class URLofArticle:
    def __init__(self, master, main_menu):
        self.master = master
        self.main_menu = main_menu
        master.title("URL Summarizer")

        # Configure List of Articles window size and position
        width = 600
        height = 400
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        master.geometry(f"{width}x{height}+{x}+{y}")

        # Configure List of Articles window color
        master.configure(bg="#1a1918")

        # Configure List of Articles title
        title_label = tk.Label(master, text="Enter URL of Article", font=("Helvetica", 16, "bold"), bg="#1a1918")
        title_label.pack(pady=10)
        
        # Input box and submit button
        self.input_var = tk.StringVar()
        entry = Entry(master, textvariable=self.input_var, font=("Helvetica", 12), width=40)
        entry.pack(pady=10)

        style = {"font": ("Helvetica", 12), "width": 20, "height": 2, "bg": "#474646", "fg": "#5e5e5d", "borderwidth": 0}
        
        submit_button = tk.Button(master, text="Submit", command=self.submit_input, **style)
        submit_button.pack(pady=10)
        
        back_button = tk.Button(master, text="Back to Main Menu", command=self.back_to_main_menu, **style)
        back_button.pack(pady=10)

    def submit_input(self):
        user_input = self.input_var.get()
        url = user_input
        article = Article(url)
        article.download()
        article.parse()
        summary = summarize(article.text)
        self.show_selected_item(article.text, summary)

    def show_selected_item(self, intext, summary):
        new_window = tk.Toplevel(self.master)
        new_window.title("Online Article")

        label1 = tk.Label(new_window, text="Online Article", padx=20, pady=20)
        label1.pack()

        text_widget = scrolledtext.ScrolledText(new_window, wrap=tk.WORD, width=30, height=10, pady=20)
        text_widget.insert(tk.END, summary)
        text_widget.pack(expand=True, fill="both")

        # Add a collapsed section with a button
        section_label = scrolledtext.ScrolledText(new_window, wrap=tk.WORD, width=30, height=10, pady=20)
        section_label.insert(tk.END, intext)
        toggle_button = tk.Button(new_window, text="Show Full Article", command=lambda: self.toggle_section(section_label))
        toggle_button.pack()
        section_label.pack_forget()

    def toggle_section(self, section_label):
        if section_label.winfo_ismapped():
            section_label.pack_forget()
        else:
            section_label.pack(expand=True, fill="both")

    def back_to_main_menu(self):
        self.master.destroy()  # Close the current window
        self.main_menu.master.deiconify()  # Show the main menu window

def main():
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main()
