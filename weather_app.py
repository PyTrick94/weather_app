import requests
import json, requests, os, datetime
from tkinter import *
from PIL import Image, ImageTk


print("***WELCOME IN WEATHER APP***")


# window settings
window = Tk()
window.title('Weather App')
window.geometry('400x550')
window['background'] = "white"


# Labels and buttons
city_name = StringVar()
city_entry = Entry(window, textvariable=city_name, width=20,
                   bd=10, font=("bold", 14))
city_entry.grid(row=1, column=0, ipady=10, stick=N + E + S + W)


# Logo image
work_path = os.getcwd()
logo_path = os.path.join(work_path, 'equal_game.png')
logo_obj = Image.open(logo_path)
logo_resized = logo_obj.resize((400, 225), Image.ANTIALIAS)
logo_img = ImageTk.PhotoImage(logo_resized)
panel = Label(window, image=logo_img)
panel.place(x=0, y=360)


# Place current date & time into panel
curr_datetime = datetime.datetime.now()
curr_week_day = Label(window, text=curr_datetime.strftime('%a -- '),
                      bg="white", font=("bold", 14))
curr_week_day.place(x=10, y=60)
curr_day_month = Label(window, text=curr_datetime.strftime(('%d %B')),
                       bg="white", font=("bold", 14))
curr_day_month.place(x=65, y=60)
curr_time = Label(window, text=curr_datetime.strftime('%I : %M %p'),
                  bg="white", font=("bold", 14))
curr_time.place(x=10, y=85)


def day_night_theme(time_obj):
    work_path = os.getcwd()
    if int(time_obj.strftime('%H')) >= 18 or int(time_obj.strftime('%H')) <= 6:
        image_path = os.path.join(work_path, 'night.png')
    else:
        image_path = os.path.join(work_path, 'day.png')
    return image_path


def get_api():
    try:
        API_iteration = True
        print('Do u have API key or use default?')

        while API_iteration:
            answer = input("Please write: 'Mine' or 'Default' or write 'exit' to finish")
            answer1 = answer.title()
            if answer1 == "Mine":
                print("Keys are available on https://home.openweathermap.org/api_keys")
                API_key = str(input("Please input API key"))
                if len(API_key) != 32:
                    print("Wrong API key, please write again or chose 'Default'")
                    API_iteration = True
                else:
                    print("API key seems to be ok!")
                    return answer1, API_key
                    API_iteration = False
            elif answer1 == 'Default':
                # add here module to encrypt hashed API key from outer file
                API_key = '09b82d144ca6406375c743c108259026'
                return answer1, API_key
                API_iteration = False
            elif answer1 == "Exit":
                print("Application terminated")
                return answer1, None
                iteration == False
            else:
                API_iteration = True
    except:
        return "Something went wrong. Please run app again."

answer1, api_key = get_api()


if answer1 == "Exit":
    sys.exit()


def city_name():
    api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                               + city_entry.get() + "&units=metric&appid=" + api_key)

    data = json.loads(api_request.content)
    try:
        if data["message"] =="city not found":
            print("Please input proper name of city")
    except KeyError:
        pass

    #weather
    main = data["main"]
    temperature = int(main["temp"])
    temperature = str(temperature) + "°C"
    pressure = main["pressure"]
    humidity = main["humidity"]
    wind_speed = data["wind"]["speed"]
    wind_deg = data["wind"]["deg"]
    clouds = data["clouds"]["all"]
    visibility = data["visibility"]

    #coords
    coords = data["coord"]
    longitude = round(coords["lon"],2)
    longitude = "coords:(" + str(longitude) + ","
    lattitude = round(coords["lat"],2)
    lattitude = str(lattitude) + ")"

    #more info
    country = data["sys"]["country"]
    name = data["name"]

    #Add info to panel
    temp.configure(text=temperature)
    press.configure(text=pressure)
    humid.configure(text=humidity)
    wind_sp.configure(text=wind_speed)
    wind_d.configure(text=wind_deg)
    cloud.configure(text=clouds)
    visib.configure(text=visibility)
    latt.configure(text=lattitude)
    long.configure(text=longitude)
    countr.configure(text=country)
    city.configure(text=name)

#Day/night image
image_path = day_night_theme(curr_datetime)
image_orig = Image.open(image_path)
image_resized = image_orig.resize((200,200), Image.ANTIALIAS)#downsampling filter
day_night_image = ImageTk.PhotoImage(image_resized)
panel = Label(window, image = day_night_image)
panel.place(x=200, y=150)


# Search Bar and Button
city_nameButton = Button(window, text="Search", command=city_name)
city_nameButton.grid(row=1, column=1, padx=5, stick=W + E + N + S)


#Placing Labels
temp = Label(window, text = "   ", width = 0, bg = "white",
             font = ("Arial", 60), fg = "black")
temp.place(x=10, y = 140)

press_label = Label(window, text = "Pressure [hPa]: ", width = 0, bg = "white",
             font = ("Arial", 10), fg = "black")
press_label.place(x=10, y = 270)

press = Label(window, text = "   ", width = 0, bg = "white",
             font = ("Arial", 10), fg = "black")
press.place(x=130, y = 270)

humid_label = Label(window, text = "Humidity [%]: ", width = 0, bg = "white",
             font = ("Arial", 10), fg = "black")
humid_label.place(x=10, y = 290)

humid = Label(window, text = "   ", width = 0, bg = "white",
             font = ("Arial", 10), fg = "black")
humid.place(x=130, y = 290)

wind_sp = Label(window, text = "   ", width = 0, bg = "white",
             font = ("Arial", 10), fg = "black")
wind_sp.place(x=130, y = 250)

wind_sp_label = Label(window, text = "Wind speed (m/s): ", width = 0, bg = "white",
             font = ("Arial", 10), fg = "black")
wind_sp_label.place(x=10, y = 250)

wind_d_label = Label(window, text = "Wind [deg]: ", width = 0, bg = "white",
             font = ("Arial", 10), fg = "black")
wind_d_label.place(x=10, y = 230)

wind_d = Label(window, text = "   ", width = 0, bg = "white",
             font = ("Arial", 10), fg = "black")
wind_d.place(x=130, y = 230)

cloud_label = Label(window, text = "Clouds [%]", width = 0, bg = "white",
             font = ("Arial", 10), fg = "black")
cloud_label.place(x=10, y = 310)

cloud = Label(window, text = "   ", width = 0, bg = "white",
             font = ("Arial", 10), fg = "black")
cloud.place(x=130, y = 310)

visib = Label(window, text = "   ", width = 0, bg = "white",
             font = ("Arial", 10), fg = "black")
visib.place(x=130, y = 330)

visib_label = Label(window, text = "Visibility [m]: ", width = 0, bg = "white",
             font = ("Arial", 10), fg = "black")
visib_label.place(x=10, y = 330)

latt = Label(window, text = "   ", width = 0, bg = "white",
             font = ("Arial", 10), fg = "black")
latt.place(x=250, y = 120)

long = Label(window, text = "   ", width = 0, bg = "white",
             font = ("Arial", 10), fg = "black")
long.place(x=160, y = 120)

countr = Label(window, text = "   ", width = 0, bg = "white",
             font = ("Arial", 10), fg = "black")
countr.place(x=80, y = 120)

city = Label(window, text = "   ", width = 0, bg = "white",
             font = ("Arial", 10), fg = "black")
city.place(x=10, y = 120)

window.mainloop()