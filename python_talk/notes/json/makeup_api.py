import json
from urllib.request import urlopen

url="https://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline"

with urlopen(url) as response:
    source = response.read()
    
data = json.loads(source)
print(json.dumps(data, indent=2))

# print items above $10 
for item in data:
    item_name = item['name']
    price = item['price']
    if float(price) > 10.00:
        print({item_name:price})


"""
{'Maybelline Face Studio Master Hi-Light Light Booster Bronzer': '14.99'}
{'Maybelline Fit Me Bronzer': '10.29'}
{'Maybelline Facestudio Master Contour Kit': '15.99'}
{'Maybelline Face Studio Master Hi-Light Light Booster Blush': '14.99'}
{'Maybelline Face Studio Master Hi-Light Light Booster Blush ': '14.99'}
{'Maybelline Fit Me Blush': '10.29'}
{'Maybelline Dream Bouncy Blush': '11.99'}
{'Maybelline Dream Smooth Mousse Foundation': '14.79'}
{'Maybelline Fit Me Shine-Free Foundation Stick': '10.99'}
{'Maybelline Dream Matte Mousse Foundation': '14.79'}
{'Maybelline Mineral Power Natural Perfecting Powder Foundation': '14.99'}
{'Maybelline Dream Velvet Foundation': '18.49'}
{'Maybelline Superstay Better Skin Foundation ': '14.99'}
{'Maybelline Dream Wonder Liquid Touch Foundation': '14.99'}
{'Maybelline Dream Liquid Mousse': '14.79'}
{'Maybelline FIT ME! Matte + Poreless Foundation': '10.99'}
{'Maybelline Fit Me Foundation with SPF': '10.99'}
{'Maybelline Eyestudio Color Tattoo Concentrated Crayon': '10.99'}
{'Maybelline The Nudes Eye Shadow Palette': '17.99'}
{'Maybelline The Nudes Eyeshadow Palette in The Blushed Nudes': '17.99'}
{'Maybelline Eye Studio Master Graphic in Striking Black': '11.99'}
{'Maybelline EyeStudio Master Precise Ink Pen Eyeliner': '11.99'}
{'Maybelline Line Stiletto Ultimate Precision Liquid Eyeliner': '10.29'}
{'Maybelline Liquid Eyeliner': '10.99'}
{'Maybelline Eye Studio Lasting Drama Gel Eyeliner': '11.99'}
{'Maybelline Color Sensational Vivid Matte Liquid Lip Colour': '12.99'}
{'Maybelline Lip Studio Color Blur ': '11.99'}
{"Maybelline Volum'Express Falsies Big Eyes Mascara": '12.99'}
{'Maybelline Define-A-Lash Lengthening & Defining Mascara': '10.79'}
{'Maybelline Illegal Length Fiber Extensions Mascara': '11.49'}
{"Maybelline Volum' Express The Rocket Mascara": '10.99'}
{'Maybelline Lash Stiletto Ultimate Length Mascara': '10.99'}
"""