import requests
from bs4 import BeautifulSoup
import pandas as pd
import dash
from dash import dcc, html

import plotly.express as px

# Scrape NBA data from Basketball Reference
def scrape_nba_stats():
    url = "https://www.basketball-reference.com/leagues/NBA_2024_per_game.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find('table', {'id': 'per_game_stats'})
    df = pd.read_html(str(table))[0]
    df = df[df['Player'] != 'Player']  # Remove repeated header rows
    df = df.dropna(subset=['Player'])
    return df

# Prepare data
nba_df = scrape_nba_stats()
nba_df['PTS'] = pd.to_numeric(nba_df['PTS'], errors='coerce')
nba_df['AST'] = pd.to_numeric(nba_df['AST'], errors='coerce')
nba_df['TRB'] = pd.to_numeric(nba_df['TRB'], errors='coerce')

# Create Dash app
app = dash.Dash(__name__)
fig = px.scatter(nba_df, x="AST", y="PTS", size="TRB", color="Tm", hover_name="Player",
                 title="NBA Player Stats: Points vs Assists (Bubble size = Rebounds)")

app.layout = html.Div([
    html.H1("NBA 2023-24 Per Game Stats Dashboard"),
    dcc.Graph(figure=fig),
    html.Div([
        html.H3("Top 10 Scorers"),
        html.Ul([html.Li(f"{row['Player']} ({row['PTS']} PTS)") for _, row in nba_df.nlargest(10, 'PTS').iterrows()])
    ])
])

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0")