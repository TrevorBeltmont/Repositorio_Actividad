# %%
import csv
import pandas as pd
import statistics as stats

df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")

with open('ulabox_orders_with_categories_partials_2017.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    customer = []
    order = []
    total_items = []
    discount = []
    weekday = []
    hour = []
    food = []
    fresh = []
    drinks = []
    home = []
    beauty = []
    health = []
    baby = []
    pets = []
    counter = 0;
    for row in reader:
        counter = counter + 1
        if counter > 1:
            # customer
            value_c = row[0]
            value_c = value_c.replace(',', '')
            customer.append(int(value_c))
            # order
            value_o = row[1]
            value_o = value_o.replace(',', '')
            order.append(int(value_o))
            # total_items
            value_t = row[2]
            value_t = value_t.replace(',', '')
            total_items.append(int(value_t))
            # discount
            value_d = row[3]
            value_d = value_d.replace(',', '')
            discount.append(float(value_d))
            # weekday
            value_w = row[4]
            value_w = value_w.replace(',', '')
            weekday.append(int(value_w))
            # hour
            value_h = row[5]
            value_h = value_h.replace(',', '')
            hour.append(int(value_h))
            # food
            value_f = row[6]
            value_f = value_f.replace(',', '')
            food.append(float(value_f))
            # fresh
            value_fr = row[7]
            value_fr = value_fr.replace(',', '')
            fresh.append(float(value_fr))
            # drinks
            value_dr = row[8]
            value_dr = value_dr.replace(',', '')
            drinks.append(float(value_dr))
            # home
            value_h = row[9]
            value_h = value_h.replace(',', '')
            home.append(float(value_h))
            # beauty
            value_b = row[10]
            value_b = value_b.replace(',', '')
            beauty.append(float(value_b))
            # health
            value_h = row[11]
            value_h = value_h.replace(',', '')
            health.append(float(value_h))
            # baby
            value_ba = row[12]
            value_ba = value_ba.replace(',', '')
            baby.append(float(value_ba))
            # pets
            value_p = row[13]
            value_p = value_p.replace(',', '')
            pets.append(float(value_p))

minimun_customer = min(customer)
maximun_customer = max(customer)

minimun_order = min(order)
maximun_order = max(order)

minimun_total = min(total_items)
maximun_total = max(total_items)

minimun_discount = min(discount)
maximun_discount = max(discount)

minimun_weekday = min(weekday)
maximun_weekday = max(weekday)

minimun_hour = min(hour)
maximun_hour = max(hour)

minimun_food = min(food)
maximun_food = max(food)

minimun_fresh = min(fresh)
maximun_fresh = max(fresh)

minimun_drinks = min(drinks)
maximun_drinks = max(drinks)

minimun_home = min(home)
maximun_home = max(home)

minimun_beauty = min(beauty)
maximun_beauty = max(beauty)

minimun_health = min(health)
maximun_health = max(health)

minimun_baby = min(baby)
maximun_baby = max(baby)

minimun_pets = min(pets)
maximun_pets = max(pets)

print("--- RANGOS ---")
print("El rango de la variable customer es de: ", (maximun_customer - minimun_customer))
print("El rango de la variable order es de: ", (maximun_order - minimun_order))
print("El rango de la variable total_items es de: ", (maximun_total - minimun_total))
print("El rango de la variable discount es de: ", (maximun_discount - minimun_discount))
print("El rango de la variable weekday es de: ", (maximun_weekday - minimun_weekday))
print("El rango de la variable hour es de: ", (maximun_hour - minimun_hour))
print("El rango de la variable food es de: ", (maximun_food - minimun_food))
print("El rango de la variable fresh es de: ", (maximun_fresh - minimun_fresh))
print("El rango de la variable drinks es de: ", (maximun_drinks - minimun_drinks))
print("El rango de la variable home es de: ", (maximun_home - minimun_home))
print("El rango de la variable beauty es de: ", (maximun_beauty - minimun_beauty))
print("El rango de la variable health es de: ", (maximun_health - minimun_health))
print("El rango de la variable baby es de: ", (maximun_baby - minimun_baby))
print("El rango de la variable pets es de: ", (maximun_pets - minimun_pets))

# Medidas de tendencia central

# Media
print("\n--- MEDIAS ---")
print("La media de la variable customer es de: ", stats.mean(customer))
print("La media de la variable order es de: ", stats.mean(order))
print("La media de la variable total_items es de: ", stats.mean(total_items))
print("La media de la variable discount es de: ", stats.mean(discount))
print("La media de la variable weekday es de: ", stats.mean(weekday))
print("La media de la variable hour es de: ", stats.mean(hour))
print("La media de la variable food es de: ", stats.mean(food))
print("La media de la variable fresh es de: ", stats.mean(fresh))
print("La media de la variable drinks es de: ", stats.mean(drinks))
print("La media de la variable home es de: ", stats.mean(home))
print("La media de la variable beauty es de: ", stats.mean(beauty))
print("La media de la variable health es de: ", stats.mean(health))
print("La media de la variable baby es de: ", stats.mean(baby))
print("La media de la variable pets es de: ", stats.mean(pets))

# Mediana
print("\n--- MEDIANAS ---")
print("La media de la variable customer es de: ", stats.median_low(customer))
print("La media de la variable order es de: ", stats.median_low(order))
print("La media de la variable total_items es de: ", stats.median_low(total_items))
print("La media de la variable discount es de: ", stats.median_low(discount))
print("La media de la variable weekday es de: ", stats.median_low(weekday))
print("La media de la variable hour es de: ", stats.median_low(hour))
print("La media de la variable food es de: ", stats.median_low(food))
print("La media de la variable fresh es de: ", stats.median_low(fresh))
print("La media de la variable drinks es de: ", stats.median_low(drinks))
print("La media de la variable home es de: ", stats.median_low(home))
print("La media de la variable beauty es de: ", stats.median_low(beauty))
print("La media de la variable health es de: ", stats.median_low(health))
print("La media de la variable baby es de: ", stats.median_low(baby))
print("La media de la variable pets es de: ", stats.median_low(pets))

# Moda
print("\n--- MODAS ---")
print("La media de la variable customer es de: ", stats.mode(customer))
print("La media de la variable order es de: ", stats.mode(order))
print("La media de la variable total_items es de: ", stats.mode(total_items))
print("La media de la variable discount es de: ", stats.mode(discount))
print("La media de la variable weekday es de: ", stats.mode(weekday))
print("La media de la variable hour es de: ", stats.mode(hour))
print("La media de la variable food es de: ", stats.mode(food))
print("La media de la variable fresh es de: ", stats.mode(fresh))
print("La media de la variable drinks es de: ", stats.mode(drinks))
print("La media de la variable home es de: ", stats.mode(home))
print("La media de la variable beauty es de: ", stats.mode(beauty))
print("La media de la variable health es de: ", stats.mode(health))
print("La media de la variable baby es de: ", stats.mode(baby))
print("La media de la variable pets es de: ", stats.mode(pets)) 

# Desviación estandar
print("\n--- MODAS ---")
print("La media de la variable customer es de: ", stats.pstdev(customer))
print("La media de la variable order es de: ", stats.pstdev(order))
print("La media de la variable total_items es de: ", stats.pstdev(total_items))
print("La media de la variable discount es de: ", stats.pstdev(discount))
print("La media de la variable weekday es de: ", stats.pstdev(weekday))
print("La media de la variable hour es de: ", stats.pstdev(hour))
print("La media de la variable food es de: ", stats.pstdev(food))
print("La media de la variable fresh es de: ", stats.pstdev(fresh))
print("La media de la variable drinks es de: ", stats.pstdev(drinks))
print("La media de la variable home es de: ", stats.pstdev(home))
print("La media de la variable beauty es de: ", stats.pstdev(beauty))
print("La media de la variable health es de: ", stats.pstdev(health))
print("La media de la variable baby es de: ", stats.pstdev(baby))
print("La media de la variable pets es de: ", stats.pstdev(pets))

# Cuantiles
c_1 = df["customer"].quantile(0.25)
print("\nEl primer cuartil es de la variable customer es: ", c_1)
c_2 = df["customer"].quantile(0.50)
print("El segundo cuartil es de la variable customer es: ", c_2)
c_3 = df["customer"].quantile(0.75)
print("El tercer cuartil es de la variable customer es: ", c_3)
c_4 = df["customer"].quantile(1)
print("El último cuartil es de la variable customer es: ", c_4)

o_1 = df["order"].quantile(0.25)
print("\nEl primer cuartil es de la variable order es: ", o_1)
o_2 = df["order"].quantile(0.50)
print("El segundo cuartil es de la variable order es: ", o_2)
o_3 = df["order"].quantile(0.75)
print("El tercer cuartil es de la variable order es: ", o_3)
o_4 = df["order"].quantile(1)
print("El último cuartil es de la variable order es: ", o_4)

t_1 = df["total_items"].quantile(0.25)
print("\nEl primer cuartil es de la variable total_items es: ", t_1)
t_2 = df["total_items"].quantile(0.50)
print("El segundo cuartil es de la variable total_items es: ", t_2)
t_3 = df["total_items"].quantile(0.75)
print("El tercer cuartil es de la variable total_items es: ", t_3)
t_4 = df["total_items"].quantile(1)
print("El último cuartil es de la variable total_items es: ", t_4)

d_1 = df["discount%"].quantile(0.25)
print("\nEl primer cuartil es de la variable discount es: ", d_1)
d_2 = df["discount%"].quantile(0.50)
print("El segundo cuartil es de la variable discount es: ", d_2)
d_3 = df["discount%"].quantile(0.75)
print("El tercer cuartil es de la variable discount es: ", d_3)
d_4 = df["discount%"].quantile(1)
print("El último cuartil es de la variable discount es: ", d_4)

w_1 = df["weekday"].quantile(0.25)
print("\nEl primer cuartil es de la variable weekday es: ", w_1)
w_2 = df["weekday"].quantile(0.50)
print("El segundo cuartil es de la variable weekday es: ", w_2)
w_3 = df["weekday"].quantile(0.75)
print("El tercer cuartil es de la variable weekday es: ", w_3)
w_4 = df["weekday"].quantile(1)
print("El último cuartil es de la variable order es: ", w_4)

h_1 = df["hour"].quantile(0.25)
print("\nEl primer cuartil es de la variable hour es: ", h_1)
h_2 = df["hour"].quantile(0.50)
print("El segundo cuartil es de la variable hour es: ", h_2)
h_3 = df["hour"].quantile(0.75)
print("El tercer cuartil es de la variable hour es: ", h_3)
h_4 = df["hour"].quantile(1)
print("El último cuartil es de la variable hour es: ", h_4)

f_1 = df["Food%"].quantile(0.25)
print("\nEl primer cuartil es de la variable food es: ", f_1)
f_2 = df["Food%"].quantile(0.50)
print("El segundo cuartil es de la variable food es: ", f_2)
f_3 = df["Food%"].quantile(0.75)
print("El tercer cuartil es de la variable food es: ", f_3)
f_4 = df["Food%"].quantile(1)
print("El último cuartil es de la variable food es: ", f_4)

fr_1 = df["Fresh%"].quantile(0.25)
print("\nEl primer cuartil es de la variable fresh es: ", fr_1)
fr_2 = df["Fresh%"].quantile(0.50)
print("El segundo cuartil es de la variable fresh es: ", fr_2)
fr_3 = df["Fresh%"].quantile(0.75)
print("El tercer cuartil es de la variable fresh es: ", fr_3)
fr_4 = df["Fresh%"].quantile(1)
print("El último cuartil es de la variable fresh es: ", fr_4)

dr_1 = df["Drinks%"].quantile(0.25)
print("\nEl primer cuartil es de la variable drinks es: ", dr_1)
dr_2 = df["Drinks%"].quantile(0.50)
print("El segundo cuartil es de la variable drinks es: ", dr_2)
dr_3 = df["Drinks%"].quantile(0.75)
print("El tercer cuartil es de la variable drinks es: ", dr_3)
dr_4 = df["Drinks%"].quantile(1)
print("El último cuartil es de la variable drinks es: ", dr_4)

ho_1 = df["Home%"].quantile(0.25)
print("\nEl primer cuartil es de la variable home es: ", ho_1)
ho_2 = df["Home%"].quantile(0.50)
print("El segundo cuartil es de la variable home es: ", ho_2)
ho_3 = df["Home%"].quantile(0.75)
print("El tercer cuartil es de la variable home es: ", ho_3)
ho_4 = df["Home%"].quantile(1)
print("El último cuartil es de la variable home es: ", ho_4)

b_1 = df["Beauty%"].quantile(0.25)
print("\nEl primer cuartil es de la variable beauty es: ", b_1)
b_2 = df["Beauty%"].quantile(0.50)
print("El segundo cuartil es de la variable beauty es: ", b_2)
b_3 = df["Beauty%"].quantile(0.75)
print("El tercer cuartil es de la variable beauty es: ", b_3)
b_4 = df["Beauty%"].quantile(1)
print("El último cuartil es de la variable beauty es: ", b_4)

he_1 = df["Health%"].quantile(0.25)
print("\nEl primer cuartil es de la variable health es: ", he_1)
he_2 = df["Health%"].quantile(0.50)
print("El segundo cuartil es de la variable health es: ", he_2)
he_3 = df["Health%"].quantile(0.75)
print("El tercer cuartil es de la variable health es: ", he_3)
he_4 = df["Health%"].quantile(1)
print("El último cuartil es de la variable health es: ", he_4)

ba_1 = df["Baby%"].quantile(0.25)
print("\nEl primer cuartil es de la variable baby es: ", ba_1)
ba_2 = df["Baby%"].quantile(0.50)
print("El segundo cuartil es de la variable baby es: ", ba_2)
ba_3 = df["Baby%"].quantile(0.75)
print("El tercer cuartil es de la variable baby es: ", ba_3)
ba_4 = df["Baby%"].quantile(1)
print("El último cuartil es de la variable baby es: ", ba_4)

pe_1 = df["Pets%"].quantile(0.25)
print("\nEl primer cuartil es de la variable pets es: ", pe_1)
pe_2 = df["Pets%"].quantile(0.50)
print("El segundo cuartil es de la variable pets es: ", pe_2)
pe_3 = df["Pets%"].quantile(0.75)
print("El tercer cuartil es de la variable pets es: ", pe_3)
pe_4 = df["Pets%"].quantile(1)
print("El último cuartil es de la variable pets es: ", pe_4)
# %%
