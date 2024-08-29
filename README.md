<p align="center">
<h1>Kalmati Tarkari Bazaar Discord Bot</h1>
</p>  
<p align="center">
  <img src="https://github.com/user-attachments/assets/01a60ce6-f076-46bf-88b5-bb712415de8f" alt="kalimati" width="400" height="300">
</p>



Overview

Welcome to the Kalmati Tarkari Bazaar Discord Bot project! This bot is designed to help users in a Discord channel easily access the daily prices of vegetables and fruits from the Kalmati Tarkari Bazaar. The project showcases web scraping techniques, automation through CronJobs, and integration with the Discord platform.

Features

	•	Daily Price Updates: The bot scrapes the latest prices of vegetables and fruits from the Kalmati Tarkari Bazaar and posts them in a designated Discord channel.
	•	CronJob Automation: Prices are updated at regular intervals using CronJobs, ensuring that the information provided is current and accurate.
	•	Accessible to All: Any member of the Discord channel can access the bot’s features and receive the latest market prices with simple commands.

Technologies Used

	•	Python: The core programming language used for developing the bot.
	•	BeautifulSoup: A Python library for web scraping, used to extract data from the Kalmati Tarkari Bazaar website.
	•	Discord.py: A Python library to interact with the Discord API.
	•	Cron: A time-based job scheduler used to automate the scraping and updating process.

Setup Instructions

	1.	Clone the Repository:

git clone https://github.com/ahhnuska/KalmatiBot


	2.	Install Dependencies:

pip install -r requirements.txt


	3.	Configure Environment Variables:
	•	Set up your Discord bot token and other necessary credentials in a .env file.
	4.	Run the Bot:

python bot.py



Usage

Once the bot is added to your Discord server:

	•	Use the command kitna to get the latest vegetable and fruit prices.
	•	The bot will automatically post updated prices at regular intervals.
