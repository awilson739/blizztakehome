# blizztakehome

## Requirements
1. Battle.net account
1. API Client ID and Secret 
## Installation
```
git clone https://github.com/awilson739/blizztakehome.git
pip3 install -r requirements.txt
python3 app.py
```
Access the site through 127.0.0.1:5000
## Program Breakdown
This is a Flask web application which pulls down warlock and druid legendary cards. It then combines them together, removes cards that are under 7 mana, and then shuffles and chooses 10 cards to display. It also uses metadata api to match the set, class, and type of the card. To create the html page, it passes the cards to the jinja template which creates the table. 
### Known Issues
The table is not very good to look at :) 
Pulling the api constantly at each call- this could be resolved with caching or using a class instead of functions
Seen problems of duplicate cards 
Cards are not ordered by ID
## Diagram 
![diagram](https://lucid.app/publicSegments/view/94f15ee5-b118-4c35-86a1-2c052e08b70c/image.png)
