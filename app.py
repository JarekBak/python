import csv
import os.path
import pandas as pd

from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, url_for
from constants import BAZA_PRODUKT, KONTO, SALDO
from models import Product

app = Flask(__name__)
app.secret_key = "super_tajny_klucz"

def get_products():
    products = []

    # Zwrócenie pustej listy w przypadku braku danych w pliku csv
    if not os.path.exists(BAZA_PRODUKT):
        return products

    with open(BAZA_PRODUKT, "r", encoding="utf-8") as file_product:
        reader = csv.DictReader(file_product)

        for row in reader:
            product = Product(item_name=row["item_name"], quantity=row["quantity"], price=row["price"])
            products.append(product)

    return products


def show_table_operations():
    """
    Funkcja zwracająca wszystkie zapisane operacje w pliku SALDO
    """
    new_headers = ["Data i czas operacji", "Rodzaj operacji", "Nazwa produktu", "Liczba produktów"]
    df = pd.read_csv(SALDO, header=0, names=new_headers)
    # table_html = df.to_html(classes="table table-striped table-hover", index=True)
    # return table_html
    return df


def log_operation(operation, item_name, quantity):
    """
    Funkcja zapisująca rodzaj wykonanej operacji, jej czas oraz jaki produkt i w jakiej ilości jej dotyczył
    """
    try:
        with open(SALDO, "a", newline="", encoding="utf-8") as saldo_file:
            fieldnames = ["date", "operation", "item_name", "quantity"]
            writer = csv.DictWriter(saldo_file, fieldnames=fieldnames)

            if os.path.getsize(SALDO) == 0:
                writer.writeheader()

            writer.writerow(
                {
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "operation": operation,
                    "item_name": item_name,
                    "quantity": quantity
                }
            )
    except Exception as e:
        print(f"Wystąpił błąd {e}")


def count_operation():
    """
    Funkcja zliczająca wszystkie wykonane operacje na podstawie pliku SALDO.
    Informacja wykorzystana na stronie history.html
    """
    saldo_file = SALDO
    df = pd.read_csv(saldo_file)
    row_count = len(df)
    return row_count

def account_balance(file_path = KONTO):
    """
    Funkcja odczytująca plik stan_konta.txt
    """
    try:
        with open(KONTO, "r", encoding="utf-8") as account:
            return account.read()
    except FileNotFoundError:
        return None

def save_account_balance(ac_sum):
    """
    funkcja nadpisująca plik stan_konta.txt
    """

    with open(KONTO, "w") as ac:
        ac.write(str(ac_sum))

def add_product():
    """
    Funkcja dodająca nowy produkt do bazy produktów.
    """
    # Pobranie danych z formularza:
    if request.method == "POST":
        new_product = request.form.get("new_product")
        new_quantity = request.form.get("new_quantity")
        new_price = request.form.get("new_price")

        products = []
        product_found = False
        try:
            # Wczytanie istniejącej bazy produktów
            if os.path.exists(BAZA_PRODUKT):
                with open(BAZA_PRODUKT, "r", encoding="utf-8") as file_product:
                    reader = csv.DictReader(file_product)
                    for row in reader:
                        if row["item_name"] == new_product and row["price"] == new_price:
                            # Produkt istnieje w bazie - zwiększamy liczbę dostępnych produktów
                            all_quantity = int(row["quantity"]) + int(new_quantity)
                            row["quantity"] = all_quantity
                            product_found = True
                            cost = int(new_quantity) * int(row["price"])
                            account = float(account_balance())
                            ac_sum = account - cost
                            save_account_balance(ac_sum)
                        products.append(row)
            if not product_found:
                # Brak produktu w bazie - dodajemy go do listy produktów
                products.append({"item_name": new_product, "quantity": str(new_quantity), "price": new_price})
                cost = int(new_quantity) * float(new_price)
                account = float(account_balance())
                ac_sum = account - cost
                save_account_balance(ac_sum)

            # Zapisanie zaktualizowanej listy produktów ponownie do pliku csv
            with open(BAZA_PRODUKT, "w", newline="", encoding="utf-8") as file_product:
                fieldnames = ["item_name", "quantity", "price"]
                writer = csv.DictWriter(file_product, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(products)
            # przygotowanie komunikatów informujących o dokonanej operacji
            if product_found:
                operation = "Zwiększono liczbę produktów w bazie"
                flash(
                    f"Zwiększono liczbę produktu {new_product} o {new_quantity} szt.",
                    "success"
                )
            else:
                operation = "Dodano nowy produkt"
                flash(
                    f"Dodano nowy produkt {new_product} w ilości: {new_quantity} szt.",
                    "success"
                )

            log_operation(operation, new_product, new_quantity)
            return redirect(url_for("index"))
        except Exception as e:
            flash(f"Wystąpił błąd podczas dodawania produktu: {e}", "error")
            # return render_template("index.html")

    # return redirect(url_for("index"))


def sell_product():
    """
    Funkcja na podstawie, której sprzedawane są produkty
    """
    products = get_products()

    if request.method == "POST":
        product = request.form.get("product")
        quantity = request.form.get("quantity")

        products = []
        product_found = False

        try:
            with open(BAZA_PRODUKT, "r", encoding="utf-8") as file_product:
                reader = csv.DictReader(file_product)
                for row in reader:
                    if row["item_name"] == product:
                        product_found = True
                        av_product = int(row["quantity"])
                        if av_product >= int(quantity):
                            # wystarczająca liczba produktów do sprzedania
                            row["quantity"] = int(av_product) - int(quantity)
                            flash(f"Sprzedano produkt {product} w ilości {quantity}", "success")
                            log_operation("Sprzedano produkt", product, quantity)
                            cost = int(quantity) * int(row["price"])
                            account = float(account_balance())
                            ac_sum = account + cost
                            save_account_balance(ac_sum)
                        else:
                            # Wyświetlenie komunikatu o braku wystarczającej liczy produktów. Operacja nie zostaje zapisana
                            flash(
                                f"Brak wystarczającej liczby produktu {product} - dostępne {av_product} szt.",
                                "error"
                            )
                    products.append(row)

            if not product_found:
                flash("Brak podanego produktu w bazie", "error")

            # nadpisanie pliku csv z produktami
            with open(BAZA_PRODUKT, "w", newline="", encoding="utf-8") as file_product:
                fieldnames = ["item_name", "quantity", "price"]
                writer = csv.DictWriter(file_product, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(products)
            return redirect(url_for("index"))

        except Exception as e:
            flash(f"Wystąpił błąd podczas sprzedaży produktu: {e}", "error")
            # return render_template("index.html")

@app.route("/action_button", methods=["POST"])
def action_button():
    """
    Funkcja na podstawie której w zależności od rodzaju operacji i użyciu różnych przycisków na stronie wykonywana jest
    odpowiednia funkcja (zakup lub sprzedaż produktu)
    :return:
    """
    action = request.form.get("button")
    if action == "add_product":
        return add_product()
    elif action == "sell_product":
        return sell_product()
    # W razie niepoprawnej akcji przekieruj na stronę główną
    return redirect(url_for("index"))

@app.route("/", methods=["GET"])
def index():
    products = get_products()
    account = account_balance()

    return render_template(
        "index.html",
        products=products,
        account=account,
        )

@app.route("/history/")
@app.route("/history/<int:od>/<int:do>")
def history(od=None, do=None):
    history_df = show_table_operations()
    count_op = count_operation()
    error = None

    if od is not None and do is not None:
        try:
            if 0 <= od < len(history_df) and 0 < do <= len(history_df):
                history_df = history_df.iloc[od:do].reset_index(drop=True)
            else:
                error = f"Zakres musi mieścić się od 0 do {len(history_df) - 1}."
                flash(error, "error")
        except ValueError:
            error = "Nieprawidłowy zakres."

    history_table = history_df.to_html(classes="table table-striped", index=False) if not history_df.empty else "Brak historii."
    return render_template("history.html", od=od, do=do, data=history_table, error=error, count_op=count_op)

if __name__ == ("__main__"):
    app.run(debug=True)
