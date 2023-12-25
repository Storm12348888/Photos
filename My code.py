print("Welke taal/With language?")
print("Nederlands")
language = input("English")
if language == "Nederlands":
    print("Wat wil je doen?")
    print("Wie is beter")
    print("Storbux")
    print("Winkelwagen")
    print("Temperatuur meten")
    print("Email noemer")
    print("Timer")
    a = input("Informatie")
    if a == "Informatie":
        print("Welke?")
        print("Gewoon")
        ac = input("Voetbal")
        if ac == "Gewoon":
            name = input("Wat is jouw naam?")
            age = int(input("Hoe oud ben jij?"))
            car = input("Wat is jouw favoriete automerk?")
            youtube = input("Wat is jouw favoriete YouTuber?")
            pizza = input("Wat is jouw favoriete pizza?")
            print("Hallo "+name)
            print("Jij bent "+str(age)+" jaar oud")
            print("Jouw favoriete automerk is "+car)
            print("Jouw favoriete YouTuber is "+youtube)
            aca = input("Jouw favoriete pizza is "+pizza)
        if ac == "Voetbal":
            position = input("Als jij een voetvballer was, welke positie was jij dan geweest?")
            acb = input("Als jij een voetballer was, zou jij een "+str(position)+" willen zijn.")
    if a == "Wie is beter":
        aa = input("Ronaldo of Messi")
        if aa == "Ronaldo":
            input("Jij hebt hetzelfde gekozen als ik gekozen zal hebben")
        if aa == "Messi":
            input("Wij zijn niet hetzelfde")
    if a == "Storbux":
        print("Welkom bij Storbux!")
        print("Wat wil je kopen?")
        print("iPhone")
        print("Games")
        ac = input("Popcorn")
        if ac == "Popcorn":
            aaaa = input("Bedankt voor het shoppen bij Storbux!")
        if ac == "Games":
            print("Welke?")
            print("Fortnite")
            print("Gran Turismo")
            aca = input("Minecraft")
            if aca == "Fortnite":
                acaa = input("Bedankt voor het shoppen bij Storbux!")
            if aca == "Gran Turismo":
                acab = input("Bedankt voor het shoppen bij Storbux!")
            if aca == "Minecraft":
                acac = input("Bedankt voor het shoppen bij Storbux!")
        if ac == "iPhone":
            print("Welke?")
            print("iPhone 13")
            print("iPhone 14")
            acb = input("iPhone 15")
            if acb == "iPhone 13":
                acba = input("Bedankt voor het shoppen bij Storbux!")
            if acb == "iPhone 14":
                acbb = input("Bedankt voor het shoppen bij Storbux!")
            if acb == "iPhone 15":
                acbc = input("Bedankt voor het shoppen bij Storbux!")
    if a == "Winkelwagen":
        item = input("Welke ding wil je kopen?")
        price = float(input("Wat is de prijs?"))
        quantity = int(input("Hoeveel wil je?"))
        soort = input(f"Welke soort {item} wil je?")
        total = price * quantity
        print(f"Jij hebt {quantity}x {item} {soort} gekocht")
        print(f"Jouw totaal is: €{round(total, 2)}")
    if a == "Temperatuur meten":
        unit = input("Is de temperatuur in Celsius of in Fahrenheit (C/F)")
        temp = float(input("Wat is de temperatuur?"))
        if unit == "C":
            temp = round((9 * temp) / 5 + 32, 1)
            print(f"De temperatuur in Fahrenheit is {temp}°F")
        elif unit == "F":
            temp = round((temp - 32) * 5 / 9, 1)
            print(f"De temperatuur in Celsius is {temp}°C")
        else:
            print(f"{unit} is geen temperatuur")
    if a == "Email noemer":
        email = input("Voeg jouw email in")
        username = email[:email.index("@")]
        domain = email[email.index("@") + 1:]
        print(f"Jouw username is {username} en de domein is {domain}")
    if a == "Timer":
        import time
        my_time = int(input("Voeg de tijd in met seconde"))
        for x in range(my_time, 0, -1):
            seconds = x % 60
            minutes = int(x / 60) % 60
            hours = int(x / 3600)
            print(f"{hours:02}:{minutes:02}:{seconds:02}")
            time.sleep(1)
        print("TIJD IS OM!")
if language == "English":
    print("What do you want to do?")
    english_a = input("To-do list")
    if english_a == "To-do list":
        tasks = []


        def addTask():
          task = input("Please enter a task: ")
          tasks.append(task)
          print(f"Task '{task}' added to the list.")


        def listTasks():
          if not tasks:
            print("There are no tasks currently.")
          else:
            print("Current Tasks:")
            for index, task in enumerate(tasks):
              print(f"Task #{index}. {task}")


        def deleteTask():
          listTasks()
          try:
            taskToDelete = int(input("Enter the # to delete: "))
            if taskToDelete >= 0 and taskToDelete < len(tasks):
              tasks.pop(taskToDelete)
              print(f"Task {taskToDelete} has been removed.")
            else:
              print(f"Task #{taskToDelete} was not found.")
          except:
            print("Invalid input.")


        if __name__ == "__main__":
          ### Create a loop to run the app
          print("Welcome to the to do list app :)")
          while True:
            print("\n")
            print("Please select one of the following options")
            print("------------------------------------------")
            print("1. Add a new task")
            print("2. Delete a task")
            print("3. List tasks")
            print("4. Quit")

            choice = input("Enter your choice: ")

            if (choice == "1"):
              addTask()
            elif (choice == "2"):
              deleteTask()
            elif (choice == "3"):
              listTasks()
            elif (choice == "4"):
              break
            else:
              print("Invalid input. Please try again.")
