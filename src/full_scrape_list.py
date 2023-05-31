
end_url = "&orderBy=relevance"

list_of_search_pages = []
step = 25000
for i in range(20,40):
    print(i)
"""
for index in range(40):
    min_price = index*step
    max_price = min_price +step - 1
    base_url = f"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&priceType=SALE_PRICE&minPrice={min_price}&maxPrice={max_price}&page="
    for page_number in range(25):
        list_of_search_pages.append(base_url+str(page_number)+end_url)

step = 50000
for index in range(20, 40):
    min_price = index*step
    max_price = min_price +step - 1
    base_url = f"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&priceType=SALE_PRICE&minPrice={min_price}&maxPrice={max_price}&page="
    for page_number in range(25):
        list_of_search_pages.append(base_url+str(page_number)+end_url)
        """
