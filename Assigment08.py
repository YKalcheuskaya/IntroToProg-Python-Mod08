# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2022,Created started script
# RRoot,1.1.2022,Added pseudo-code to start assignment 8
# YKalch,3.10.2022,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
products_registry_name = 'products.txt'
list_of_products = []


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2022,Created Class
        YKalch,3.10.2022,Modified code to complete assignment 8
    """

    # -- Constructor --

    def __init__(self, product_name: str, product_price: float):
        # -- Attributes --
        self.product_name = product_name
        self.product_price = product_price

    # -- Properties --

    # Getter for 'product_name'
    @property
    def product_name(self):
        return str(self.__product_name)

    # Setter for 'product_name'
    @product_name.setter
    def product_name(self, value: str):
        if not str(value).isnumeric():
            self.__product_name = value
        else:
            raise Exception("Product name can not be a number!")

    # Getter for 'product_price'
    @property
    def product_price(self):
        return str(self.__product_price)

    # Setter for 'product_price'
    @product_price.setter
    def product_price(self, value: float):
        try:
            if float(value) > 0:
                self.__product_price = value
            else:
                print("Product price should be positive!")
        except ValueError:
            print("Product price should be a number!")
            self.__product_price = None
# Data -------------------------------------------------------------------- #


# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, products):
        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        YKalch,3.10.2022,Modified code to complete assignment 8
    """

    @staticmethod
    def save_data_to_file(file_name: str, products: list):
        """ Save list of products to a text file.

        :param file_name: (string) with name of file:
        :param products: (list) products list:
        :return: nothing
        """

        if len(products) == 0:
            print("The product list is empty, so there is nothing to save!")
        else:
            # Adding exception handling for scenarios when we can't write to the file
            try:
                # Creating/opening the file in write mode
                file = open(file_name, "w")

                # Writing the data to the file
                for product in products:
                    file.write(product.product_name + "," + product.product_price + "\n")

                # Closing the file
                file.close()

                # The file has been saved successfully
                print("Products are saved successfully!")
            except Exception as ex:
                print(ex)
                print(type(ex))
                print(ex.__doc__)
                print(ex.__str__())

        # If we are here, we did not write to the file for whatever reason
        print("Failed to save products to the file!")

    @staticmethod
    def read_data_from_file(file_name: str):
        """ Load products from a text file.

        :param file_name: (string) with name of file:
        :return: (list) the list of loaded products (empty list if the load failed)
        """

        products = []

        # Adding exception handling for scenario when the file does not exist
        try:
            # Opening the file in read mode
            file = open(file_name, "r")

            # Read the file content line by line and convert it to a product
            for line in file:
                product_data = line.strip().split(",")

                # Verifying that the format is valid
                if len(product_data) == 2:
                    # Adding a new product to the list
                    products.append(Product(product_data[0].strip(), product_data[1].strip()))
                else:
                    print("Unexpected value detected!")

            # Closing the file
            file.close()
        except FileNotFoundError:
            print("The product registry file does not exist!")
        except Exception as ex:
            print("Failed to load products from the file!")
            print(ex)
            print(type(ex))
            print(ex.__doc__)
            print(ex.__str__())

        return products
# Processing  ------------------------------------------------------------- #


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Performs input and output tasks:

    methods:
        show_menu_tasks():
        input_menu_choice(): -> (the user choice)
        display_products(list_of_products):
        input_new_product(): -> (the product name and price to be added to the list)
        input_product_to_remove(): -> (the product name to be removed from the list)

    changelog: (When,Who,What)
        YKalch,3.10.2022,Initial version with methods
    """

    @staticmethod
    def show_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """

        print('''
        Menu of Options:
        1) Add a new Product
        2) Remove the Product by name
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        menu_choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks

        return menu_choice

    @staticmethod
    def display_products(products: list):
        """  Displays the list of products to the user

        :param products: (list) with products to display:
        :return: nothing
        """
        if products is not None and len(products) > 0:
            print()  # Add an extra line for looks
            print("Current list of products:")
            print("-----------------------------------")

            for product in products:
                print(product.product_name + " - " + product.product_price)

            print("-----------------------------------")
        else:
            print("The list of products is empty!")

    @staticmethod
    def input_new_product():
        """  Gets product name and price values to be added to the list

        :return: (string, string) with product name and price
        """
        product_name = input("What is the product name? ").strip()
        product_price = input("What is the product price? [Float] ").strip()

        return product_name, product_price

    @staticmethod
    def input_product_to_remove():
        """  Gets the product name to be removed from the list

        :return: (string) with product name
        """
        product_name = input("What product do you want to remove? ").strip()

        return product_name
# Presentation (Input/Output)  -------------------------------------------- #


# Main Body of Script  ---------------------------------------------------- #
# Step 1 - When the program starts, load the product list from the file
list_of_products = FileProcessor.read_data_from_file(products_registry_name)

# Step 2 - Display a menu of choices to the user
while True:
    # Show current data
    IO.display_products(list_of_products)  # Show the products
    IO.show_menu_tasks()  # Show menu
    choice = IO.input_menu_choice()  # Input the menu choice

    # Step 4 - Process user's menu choice
    if choice == '1':  # Add a new Product
        name, price = IO.input_new_product()

        # Adding a new Product to the list
        list_of_products.append(Product(product_name=name, product_price=price))

        continue  # to show the menu

    elif choice == '2':  # Remove an existing Product
        name = IO.input_product_to_remove()

        # Deleting a Product from the list by Product name
        for i in range(len(list_of_products)):
            if list_of_products[i].product_name == name:
                del list_of_products[i]
                print("Deleted '{}' product from the list".format(name))
                break

        continue  # to show the menu

    elif choice == '3':  # Save Data to File
        FileProcessor.save_data_to_file(file_name=products_registry_name, products=list_of_products)

        continue  # to show the menu

    elif choice == '4':  # Exit Program
        print("Goodbye!")
        break  # by exiting loop
# Main Body of Script  ---------------------------------------------------- #
