import json
import tkinter as tk
import os
from PIL import Image, ImageTk

from modules.gui_shop.canvas import app
from modules.gui_shop.helpers import get_current_user, clean_screen

base_folder = os.path.dirname(__file__)

def update_current_user(username, product_id):
    with open("db/users.txt", "r+") as f:
        users = [json.loads(u.strip()) for u in f]
        for user in users:
            if user["username"] == username:
                user["products"].append(product_id)
                f.seek(0)
                f.truncate()
                f.writelines([json.dumps(u) + "\n" for u in users])
                return

def purchase_product(product_id):
    with open("db/products.txt", "r+") as f:
        products = [json.loads(p.strip()) for p in f]
        for product in products:
            if product["id"] == product_id:
                product["count"] -= 1
                f.seek(0)
                f.truncate()
                f.writelines([json.dumps(p) + "\n" for p in products])
                return




def buy_product(product_id):
    clean_screen()

    username = get_current_user()

    if username:
        update_current_user(username, product_id)
        purchase_product(product_id)

    render_products_screen()

def add_product(name, img, count):
    with open("db/products.txt", "r+") as f:
        if name == "" or img == "" or not count.isdigit() or int(count) < 0:
            render_add_product("Please fill all fields!")
            return
        f.write(json.dumps({
            "id": len(f.readlines()) + 1,
            "name": name,
            "img_path": img,
            "count": int(count)
        }) + "\n")

        render_products_screen()

def render_add_product(error=None):
    clean_screen()
    tk.Label(app, text="Product name ").grid(row=0, column=0)
    name = tk.Entry(app)
    name.grid(row=0, column=1)

    tk.Label(app, text="Product image: ").grid(row=1, column=0)
    img = tk.Entry(app)
    img.grid(row=1, column=1)

    tk.Label(app, text="Product count: ").grid(row=2, column=0)
    count = tk.Entry(app)
    count.grid(row=2, column=1)

    tk.Button(app, text="Add",
              command=lambda: add_product(name.get(), img.get(), count.get())
              ).grid(row=3, column=0)

    if error:
        tk.Label(app, text=error, fg="red").grid(row=4, column=0, columnspan=2)



def render_products_screen():
    clean_screen()

    username = get_current_user()
    with open("db/users.txt") as f:
        users = [json.loads(u.strip()) for u in f]
        user = next((u for u in users if u['username'] == username and u['is_admin']), None)
        if user:
            tk.Label(app, text=f"Welcome, {user['first_name']}", fg="red", font=("Comic Sans", 15)).grid(row=0, column=0, columnspan=6)
            tk.Button(app, text="Add product",
                      command=render_add_product).grid(row=1, column=0, sticky="w", padx=10)



    with open("db/products.txt") as file:
        products = [json.loads(p.strip()) for p in file]
        products = [p for p in products if p["count"] > 0]
        products_per_line = 6
        rows_for_product = len(products[0])
        for i, product in enumerate(products):
            row = i // products_per_line * rows_for_product +2 #because of the added label and button
            column = i % products_per_line

            tk.Label(app, text=product["name"]).grid(row=row, column=column)

            img = Image.open(os.path.join(base_folder, "db/images", product["img_path"])).resize((150, 150))
            photo_img = ImageTk.PhotoImage(img)
            img_label = tk.Label(app, image=photo_img)
            img_label.image = photo_img
            img_label.grid(row=row+1, column=column)

            tk.Label(app, text=product["count"]).grid(row=row+2, column=column)

            tk.Button(app,
                      text=f"Buy {product["id"]}",
                      command=lambda p=product["id"]: buy_product(p)
                      ).grid(row=row+3, column=column)
