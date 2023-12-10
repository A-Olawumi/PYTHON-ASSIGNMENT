import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request to the website
url = "https://www.jumia.com.ng/womens-shoes/"
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Identify HTML attributes for the data points you want to pull
    # For example, let's assume you want to extract product names and prices
    product_names = [name.text.strip() for name in soup.select('.name')]
    product_prices = [price.text.strip() for price in soup.select('.price')]

    # Create a Pandas DataFrame
    data = {'Product Name': product_names, 'Product Price': product_prices}
    df = pd.DataFrame(data)

    # Display the DataFrame
    print(df)

    # Visualize the data (you can choose any plot of your choice)
    import matplotlib.pyplot as plt

    
    df['Product Price'] = df['Product Price'].str.replace('₦', '').astype(float)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.bar(df['Product Name'], df['Product Price'])
    plt.xlabel('Product Name')
    plt.ylabel('Product Price (₦)')
    plt.title('Women\'s Shoes Prices on Jumia')
    plt.xticks(rotation=45, ha='right')
    plt.show()
