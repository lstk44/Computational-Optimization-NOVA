import pandas as pd

def transform_data():
    """This function was used to transform the data from the .csv file into a dictionary, 
    which was then stored below in this file to make the data easily importable.

    Returns:
        dictionary: The keys are the names of the McDonald's menu items and the values are corresponding nutritional values.
    """
    # Read in the data.
    df = pd.read_csv('DataCSV/McDonaldsMenuData.csv')
    # Create an empty dictionary.
    d = {}
    # Iterate through the rows of the dataframe.
    for index, row in df.iterrows():
        # Get the item name and the other columns as a list.
        item_name = row['Item']
        item_values = [row['Price ($)'], row['Calories (kcal)'], row['Total Fat (g)'],
                       row['Sodium (mg)'], row['Carbohydrates (g)'], row['Protein (g)']]
        
        # Add the item and its values to the dictionary.
        d[item_name] = item_values
    return d


###################################################################
# Nutrient minimum constraints
###################################################################
"""
    Source:
    https://www.researchgate.net/figure/Mean-Daily-Nutritional-Intake-for-Group-3_tbl7_235045008
"""

nutrients = {
    'Calories (kcal)':            1670,
    'Total Fat (g)':              60,
    'Sodium (mg)':                3820,
    'Carbohydrates (g)':          220,
    'Protein (g)':                70
}


###################################################################
# McDonald's Data
###################################################################
"""
    Menu Nutrients Source:
    https://github.com/Enjia/Nutrition-Facts-for-McDonald-s-Menu/blob/master/menu.csv

    Price Source:
    https://www.fastfoodmenuprices.com/mcdonalds-prices/
"""

commodities = {
    'Egg McMuffin': [4.48, 300, 13.0, 750, 31, 17],
    'Egg White Delight': [3.9, 250, 8.0, 770, 30, 18],
    'Sausage McMuffin': [2.09, 370, 23.0, 780, 29, 14],
    'Sausage McMuffin with Egg': [3.76, 450, 28.0, 860, 30, 21],
    'Sausage McMuffin with Egg Whites': [3.76, 400, 23.0, 880, 30, 21],
    'Steak & Egg McMuffin': [3.99, 430, 23.0, 960, 31, 26],
    'Bacon, Egg & Cheese Biscuit (Regular Biscuit)': [4.61, 460, 26.0, 1300, 38, 19],
    'Bacon, Egg & Cheese Biscuit (Large Biscuit)': [5.2, 520, 30.0, 1410, 43, 19],
    'Bacon, Egg & Cheese Biscuit with Egg Whites (Regular Biscuit)': [4.61, 410, 20.0, 1300, 36, 20],
    'Bacon, Egg & Cheese Biscuit with Egg Whites (Large Biscuit)': [5.2, 470, 25.0, 1420, 42, 20],
    'Sausage Biscuit (Regular Biscuit)': [2.01, 430, 27.0, 1080, 34, 11],
    'Sausage Biscuit (Large Biscuit)': [3.9, 480, 31.0, 1190, 39, 11],
    'Sausage Biscuit with Egg (Regular Biscuit)': [4.22, 510, 33.0, 1170, 36, 18],
    'Sausage Biscuit with Egg (Large Biscuit)': [5.4, 570, 37.0, 1280, 42, 18],
    'Sausage Biscuit with Egg Whites (Regular Biscuit)': [4.22, 460, 27.0, 1180, 34, 18],
    'Sausage Biscuit with Egg Whites (Large Biscuit)': [5.4, 520, 32.0, 1290, 40, 18],
    'Southern Style Chicken Biscuit (Regular Biscuit)': [4.22, 410, 20.0, 1180, 41, 17],
    'Southern Style Chicken Biscuit (Large Biscuit)': [5.4, 470, 24.0, 1290, 46, 17],
    'Bacon, Egg & Cheese McGriddles': [4.64, 460, 21.0, 1250, 48, 19],
    'Bacon, Egg & Cheese McGriddles with Egg Whites': [4.64, 400, 15.0, 1250, 47, 20],
    'Sausage McGriddles': [3.21, 420, 22.0, 1030, 44, 11],
    'Sausage, Egg & Cheese McGriddles': [4.63, 550, 31.0, 1320, 48, 20],
    'Sausage, Egg & Cheese McGriddles with Egg Whites': [4.63, 500, 26.0, 1320, 46, 21],
    'Bacon, Egg & Cheese Bagel': [4.81, 620, 31.0, 1480, 57, 30],
    'Bacon, Egg & Cheese Bagel with Egg Whites': [4.81, 570, 25.0, 1480, 55, 30],
    'Steak, Egg & Cheese Bagel': [5.51, 670, 35.0, 1510, 56, 33],
    'Big Breakfast (Regular Biscuit)': [5.32, 740, 48.0, 1560, 51, 28],
    'Big Breakfast with Hotcakes (Regular Biscuit)': [6.69, 1090, 56.0, 2150, 111, 36],
    'Hotcakes': [4.2, 350, 9.0, 590, 60, 8],
    'Hotcakes and Sausage': [4.88, 520, 24.0, 930, 61, 15],
    'Sausage Burrito': [6.98, 300, 16.0, 790, 26, 12],
    'Hash Brown': [1.6, 150, 9.0, 310, 15, 1],
    'Cinnamon Melts': [1.8, 460, 19.0, 370, 66, 6],
    'Fruit & Maple Oatmeal': [3.66, 290, 4.0, 160, 58, 5],
    'Fruit & Maple Oatmeal without Brown Sugar': [3.66, 260, 4.0, 115, 49, 5],
    'Big Mac': [5.53, 530, 27.0, 960, 47, 24],
    'Quarter Pounder with Cheese': [5.65, 520, 26.0, 1100, 41, 30],
    'Quarter Pounder with Bacon & Cheese': [6.3, 600, 29.0, 1440, 48, 37],
    'Quarter Pounder with Bacon Habanero Ranch': [8.61, 610, 31.0, 1180, 46, 37],
    'Quarter Pounder Deluxe': [9.61, 540, 27.0, 960, 45, 29],
    'Double Quarter Pounder with Cheese': [11.12, 750, 43.0, 1280, 42, 48],
    'Hamburger': [1.62, 240, 8.0, 480, 32, 12],
    'Cheeseburger': [1.88, 290, 11.0, 680, 33, 15],
    'Double Cheeseburger': [5.99, 430, 21.0, 1040, 35, 24],
    'Bacon Clubhouse Burger': [6.99, 720, 40.0, 1470, 51, 39],
    'McDouble': [2.6, 380, 17.0, 840, 34, 22],
    'Bacon McDouble': [3.37, 440, 22.0, 1110, 35, 27],
    'Daily Double': [3.34, 430, 22.0, 760, 34, 22],
    'Jalapeno Double': [4.34, 430, 23.0, 1030, 35, 22],
    'McRib': [4.5, 500, 26.0, 980, 44, 22],
    'Premium Crispy Chicken Classic Sandwich': [5.17, 510, 22.0, 990, 55, 24],
    'Premium Grilled Chicken Classic Sandwich': [5.17, 350, 9.0, 820, 42, 28],
    'Premium Crispy Chicken Club Sandwich': [5.17, 670, 33.0, 1410, 58, 36],
    'Premium Grilled Chicken Club Sandwich': [5.17, 510, 20.0, 1250, 44, 40],
    'Premium Crispy Chicken Ranch BLT Sandwich': [6.14, 610, 28.0, 1400, 57, 32],
    'Premium Grilled Chicken Ranch BLT Sandwich': [6.14, 450, 15.0, 1230, 43, 36],
    'Bacon Clubhouse Crispy Chicken Sandwich': [7.14, 750, 38.0, 1720, 65, 36],
    'Bacon Clubhouse Grilled Chicken Sandwich': [7.14, 590, 25.0, 1560, 51, 40],
    'Southern Style Crispy Chicken Sandwich': [6.78, 430, 19.0, 910, 43, 21],
    'McChicken': [2.08, 360, 16.0, 800, 40, 14],
    'Bacon Cheddar McChicken': [3.18, 480, 24.0, 1260, 43, 22],
    'Bacon Buffalo Ranch McChicken': [3.77, 430, 21.0, 1260, 41, 20],
    'Buffalo Ranch McChicken': [2.98, 360, 16.0, 990, 40, 14],
    'Chicken McNuggets (4 piece)': [2.64, 190, 12.0, 360, 12, 9],
    'Chicken McNuggets (6 piece)': [3.62, 280, 18.0, 540, 18, 13],
    'Chicken McNuggets (10 piece)': [6.72, 470, 30.0, 900, 30, 22],
    'Chicken McNuggets (20 piece)': [6.99, 940, 59.0, 1800, 59, 44],
    'Chicken McNuggets (40 piece)': [13.35, 1880, 118.0, 3600, 118, 87],
    'Filet-O-Fish': [4.98, 390, 19.0, 590, 39, 15],
    'Premium Bacon Ranch Salad (without Chicken)': [5.13, 140, 7.0, 300, 10, 9],
    'Premium Bacon Ranch Salad with Crispy Chicken': [6.45, 380, 21.0, 860, 22, 25],
    'Premium Bacon Ranch Salad with Grilled Chicken': [6.46, 220, 8.0, 690, 8, 29],
    'Premium Southwest Salad (without Chicken)': [5.19, 140, 4.5, 150, 20, 6],
    'Premium Southwest Salad with Crispy Chicken': [6.47, 450, 22.0, 850, 42, 23],
    'Premium Southwest Salad with Grilled Chicken': [6.89, 290, 8.0, 680, 28, 27],
    'Chipotle BBQ Snack Wrap (Crispy Chicken)': [2.39, 340, 15.0, 780, 37, 14],
    'Chipotle BBQ Snack Wrap (Grilled Chicken)': [2.43, 260, 8.0, 700, 30, 16],
    'Honey Mustard Snack Wrap (Crispy Chicken)': [2.39, 330, 15.0, 730, 34, 14],
    'Honey Mustard Snack Wrap (Grilled Chicken)': [2.43, 250, 8.0, 650, 27, 16],
    'Ranch Snack Wrap (Crispy Chicken)': [2.39, 360, 20.0, 810, 32, 15],
    'Ranch Snack Wrap (Grilled Chicken)': [2.43, 280, 13.0, 720, 25, 16],
    'Small French Fries': [2.34, 230, 11.0, 130, 30, 2],
    'Medium French Fries': [2.77, 340, 16.0, 190, 44, 4],
    'Large French Fries': [3.57, 510, 24.0, 290, 67, 6],
    'Side Salad': [2.46, 20, 0.0, 10, 4, 1],
    'Apple Slices': [0.89, 15, 0.0, 0, 4, 0],
    "Fruit 'n Yogurt Parfait": [2.12, 150, 2.0, 70, 30, 4],
    'Baked Apple Pie': [1.09, 250, 13.0, 170, 32, 2],
    'Chocolate Chip Cookie': [0.88, 160, 8.0, 90, 21, 2],
    'Hot Fudge Sundae': [2.83, 330, 9.0, 170, 53, 8],
    'Strawberry Sundae': [2.14, 280, 6.0, 85, 49, 6]
    }
