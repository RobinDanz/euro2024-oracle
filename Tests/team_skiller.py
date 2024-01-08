from trueskill import Rating

teams = [
    [
        'Albania',
        'Austria',
        'Belgium',
        'Croatia'
    ],
    [
        'Denmark',
        'England',
        'France',
        'Germany'
    ],
    [
        'Hungary',
        'Italia',
        'Netherlands',
        'Portugal'
    ],
    [
        'Romania',
        'Scotland',
        'Serbia',
        'Slovakia'
    ],
    [
        'Slovenia',
        'Spain',
        'Switzerland',
        'Turkey'
    ]
]

team_rating = {}

if __name__ == '__main__':
    for group in teams:
        for team in group:
            team_rating[team] = Rating()

            