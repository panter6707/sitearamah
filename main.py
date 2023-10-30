import requests

def make_request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


target_input_MKYLisans =input("Site Adı Giriniz: ")



with open("subdomainlist.txt","r") as subdomain_list:
    for word in subdomain_list:
        word = word.strip()
        url = "https://" + word + "." + target_input_MKYLisans
        response = make_request(url)
        if response:
            print("Bulunan Subdomain--->" + url)
