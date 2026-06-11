"""
COMP.CS.100 Ohjelmointi 1
Mikko Eerola, ID 151184192

T13.7 Bmi laskuri Tkinteri-graafisen käyttöliittymän avulla
"""


from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()

        self.__weight_expl = Label(self.__mainwindow, text="Syötä painosi:")
        self.__weight_value = Entry(self.__mainwindow)

        self.__height_expl = Label(self.__mainwindow, text="Syötä pituutesi:")
        self.__height_value = Entry(self.__mainwindow)

        self.__calculate_button = Button(self.__mainwindow, text="Laske",
                                         background="red",
                                         command=self.calculate_BMI)

        self.__result_text = Label(self.__mainwindow, relief=GROOVE)
        self.__result_expl = Label(self.__mainwindow, text="bmi:")

        self.__explanation_text = Label(text="")

        self.__stop_button = Button(self.__mainwindow, text="Lopeta",
                                    command=self.stop)

        # If you read the Gaddis book, you can use pack here instead of grid!
        self.__weight_expl.grid(row=0, column=0, columnspan=2, sticky=W)
        self.__weight_value.grid(row=1, column=0, columnspan=2, sticky=W+E)
        self.__height_expl.grid(row=0, column=2, columnspan=2, sticky=W)
        self.__height_value.grid(row=1, column=2, columnspan=2, sticky=W+E)
        self.__calculate_button.grid(row=2, column=1, columnspan=2, sticky=W+E)
        self.__stop_button.grid(row=5, column=4, sticky=E)
        self.__result_expl.grid(row=2, column=0, sticky=W+S)
        self.__result_text.grid(row=3, column=0, sticky=W+E)
        self.__explanation_text.grid(row=4, column=0, columnspan=4, sticky=W)

    def calculate_BMI(self):
        """
        Part b) This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Part e) Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """
        try:
            paino = float(self.__weight_value.get())
            pituus = float(self.__height_value.get())
        except ValueError:
            self.__explanation_text.configure(
                text="Error: height and weight must be numbers.")
            self.reset_fields()
            return None

        if paino <= 0 or pituus <= 0:
            self.__explanation_text.configure(
                text="Error: height and weight must be positive.")
            self.reset_fields()
        else:
            pituus = pituus / 100
            bmi = paino/ (pituus ** 2)
            self.__result_text.configure(text=f"{bmi:.2f}")

            if bmi < 18.5:
                self.__explanation_text.configure(text="You are underweight.")
            elif bmi > 25:
                self.__explanation_text.configure(text="You are overweight.")
            else:
                self.__explanation_text.configure(
                    text="Your weight is normal.")

    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """

        self.__weight_value.delete(0, END)
        self.__height_value.delete(0, END)
        self.__result_text.configure(text="")

    def stop(self):
        """
        Ends the execution of the program.
        """

        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    # Notice how the user interface can be created and
    # started separately.  Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
