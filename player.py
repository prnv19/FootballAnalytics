from app.services.players.achievements import TransfermarktPlayerAchievements
from app.services.players.market_value import TransfermarktPlayerMarketValue
from app.services.players.injuries import TransfermarktPlayerInjuries
from app.services.players.profile import TransfermarktPlayerProfile
from app.services.players.stats import TransfermarktPlayerStats

# Convert string currency to float value
def str2currency(value):
    try:
        if value == '-':
            return 0
        else:
            if 'm' in value:
                return float(value.replace('€', '').replace('m', '')) * 1e6
            elif 'k' in value:
                return float(value.replace('€', '').replace('k', '')) * 1e3
            else:
                return float(value.replace('€', ''))
    except:
        return 0

# Get player stats
def GetPlayerStats(player_id):
    player = {}
    player['id'] = str(player_id)
    
    try:
        tfmk = TransfermarktPlayerProfile(player_id=player['id'])
        result = tfmk.get_player_profile()
        
        if result['isRetired']:
            return None

        player['name'] = result['name']
        player['dateOfBirth'] = result['dateOfBirth']
        player['Age'] = result['age']
        player['Height'] = result['height']
        player['Foot'] = result['foot']
        player['Position'] = result['position']['main']
        player['OtherPosition'] = result['position']['other']
        player['National'] = result['placeOfBirth']['country']
        player['MarketValue'] = str2currency(result['marketValue'])
        player['Outfitter'] = result['outfitter']
        player['Club_name'] = result['club']['name']
        player['ContractExpiry'] = result['club']['contractExpires']
        player['ContractOption'] = result['club']['contractOption']
        
        
        tfmkt = TransfermarktPlayerStats(player_id=player['id'])
        result = tfmkt.get_player_stats()

        for i in range(19, 25):
            player[f'{i+1}YC'] = 0
            player[f'{i+1}2YC'] = 0
            player[f'{i+1}RC'] = 0
            player[f'{i+1}G'] = 0
            player[f'{i+1}A'] = 0
            player[f'{i+1}MP'] = 0
            player[f'{i+1}AP'] = 0

        for stat in result['stats']:
            season_key = stat['seasonId'][-2:]
            
            if season_key.startswith('2'):
                player[f'{season_key}YC'] += int(stat['yellowCards'] if stat['yellowCards'] != '-' else 0)
                player[f'{season_key}2YC'] += int(stat['secondYellowCards'] if stat['secondYellowCards'] != '-' else 0)
                player[f'{season_key}RC'] += int(stat['redCards'] if stat['redCards'] != '-' else 0)
                player[f'{season_key}G'] += int(stat['goals'] if stat['goals'] != '-' else 0)
                player[f'{season_key}A'] += int(stat['assists'] if stat['assists'] != '-' else 0)
                player[f'{season_key}MP'] += float(stat['minutesPlayed'].replace("'", "") if stat['minutesPlayed'] != '-' else 0)
                player[f'{season_key}AP'] += int(stat['appearances'] if stat['appearances'] != '-' else 0)
        
        
        tfmkt = TransfermarktPlayerMarketValue(player_id=player['id'])
        result = tfmkt.get_player_market_value()
        try:
            player['Ranking'] = result['ranking']['Worldwide']
        except:
            player['Ranking'] = 0

        for i in range(2020, 2026):
            # Initialize the market value list for each year
            player[f'{i}MV'] = []

        # Populate the player dictionary with market values by year
        
        for entry in result['marketValueHistory']:
            # Extract the year from the date string
            year = int(entry['date'].split()[-1])  # Extract year from the date
            # Add market value to the corresponding year in the player dictionary
            if 2020 <= year <= 2025:
                player[f'{year}MV'].append(str2currency(entry['marketValue']))

        # Compute the average market value for each year
        for year in range(2020, 2026):
            if player[f'{year}MV']:  # Check if there are any market values for that year
                print(player[f'{year}MV'])
                player[f'{year}AvgMV'] = sum(player[f'{year}MV']) / len(player[f'{year}MV'])
            else:
                player[f'{year}AvgMV'] = 0  # If no values, assign 0
            #Remove the list of market values for each year
            player.pop(f'{year}MV')
            
        tfmkt = TransfermarktPlayerAchievements(player_id=player['id'])
        result = tfmkt.get_player_achievements()
        
        player['TotalCups'] = sum(achievement['count'] for achievement in result['achievements'])
        
        return player
    except Exception as e:
        print(f"Could not get player stats ({player_id}): ", e)
        return None
    
if __name__ == "__main__":
    player_id = 342229
    player_stats = GetPlayerStats(player_id)
    print(player_stats)
        
    
    
    