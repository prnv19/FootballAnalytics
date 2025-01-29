# **Football Player Performance Dataset**  

## **Overview**  
This dataset contains detailed performance metrics, contract details, and market value trends for 12,952 football players. The data spans multiple years, covering key statistics such as goals, assists, appearances, and disciplinary records.  

## **Dataset Structure**  
The dataset consists of **64 columns**, categorized into the following groups:  

### **1. Player Information**  
- `id` - Unique identifier for each player.  
- `name` - Full name of the player.  
- `dateOfBirth` - Player's date of birth.  
- `Age` - Current age of the player.  
- `Height` - Player's height (in meters).  
- `Foot` - Preferred foot (Left/Right).  
- `Position` - Primary playing position.  
- `OtherPosition` - Additional positions the player can play.  
- `National` - Player’s nationality.  

### **2. Contract and Club Details**  
- `Club_name` - Current club of the player.  
- `ContractExpiry` - Expiration date of the current contract.  
- `ContractOption` - Additional contract details (if applicable).  
- `Outfitter` - Brand sponsoring the player's kit (if available).  

### **3. Performance Metrics (Yearly Stats)**  
Performance metrics are recorded for multiple years (2020-2025), indicated by the prefix (`20`, `21`, `22`, etc.). Each year contains:  
- `YC` - Yellow Cards.  
- `YC2` - Second Yellow Cards.  
- `RC` - Red Cards.  
- `G` - Goals scored.  
- `A` - Assists.  
- `MP` - Minutes played.  
- `AP` - Appearances.  

Example:  
- `20G` - Goals scored in 2020.  
- `21MP` - Minutes played in 2021.  

### **4. Market Value Trends**  
- `MarketValue` - Current estimated market value of the player.  
- `2020AvgMV`, `2021AvgMV`, `2022AvgMV`, `2023AvgMV`, `2024AvgMV`, `2025AvgMV` - Average market value for each year.  

### **5. Rankings & Achievements**  
- `Ranking` - Player ranking based on performance.  
- `TotalCups` - Total number of cups/titles won.  

## **Usage**  
This dataset is useful for:  
- **Player Performance Analysis** - Evaluate player statistics over multiple seasons.  
- **Market Value Prediction** - Analyze trends in player valuation.  
- **Club and Transfer Analytics** - Assess the impact of players in different clubs.  
- **Fantasy Football & Sports Betting Models** - Build predictive models based on historical performance data.  

## **Notes**  
- Missing values exist in `Outfitter` and `ContractOption` fields due to incomplete data collection.  
- Some players might have changing positions or clubs over time.  

---
