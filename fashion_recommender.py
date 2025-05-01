class FashionRecommender:
    def __init__(self):
        self.recommendations = {
            'male': {
                'summer': {
                    'casual': [
                        {'outfit': 'T-shirt and shorts', 'image': 'male_summer_casual1.jpg'},
                        {'outfit': 'Polo shirt with chinos', 'image': 'male_summer_casual2.jpg'},
                        {'outfit': 'Linen shirt with jeans', 'image': 'male_summer_casual3.jpg'}
                    ],
                    'formal': [
                        {'outfit': 'Light suit with dress shirt', 'image': 'male_summer_formal1.jpg'},
                        {'outfit': 'Blazer with dress pants', 'image': 'male_summer_formal2.jpg'},
                        {'outfit': 'Button-down shirt with slacks', 'image': 'male_summer_formal3.jpg'}
                    ],
                    'party': [
                        {'outfit': 'Silk shirt with dress pants', 'image': 'male_summer_party1.jpg'},
                        {'outfit': 'Printed shirt with jeans', 'image': 'male_summer_party2.jpg'},
                        {'outfit': 'Smart casual blazer', 'image': 'male_summer_party3.jpg'}
                    ]
                },
                'winter': {
                    'casual': [
                        {'outfit': 'Sweater with jeans', 'image': 'male_winter_casual1.jpg'},
                        {'outfit': 'Hoodie with joggers', 'image': 'male_winter_casual2.jpg'},
                        {'outfit': 'Flannel shirt with cargo pants', 'image': 'male_winter_casual3.jpg'}
                    ],
                    'formal': [
                        {'outfit': 'Wool suit with turtleneck', 'image': 'male_winter_formal1.jpg'},
                        {'outfit': 'Overcoat with dress pants', 'image': 'male_winter_formal2.jpg'},
                        {'outfit': 'Blazer with sweater', 'image': 'male_winter_formal3.jpg'}
                    ],
                    'party': [
                        {'outfit': 'Leather jacket with jeans', 'image': 'male_winter_party1.jpg'},
                        {'outfit': 'Turtleneck with blazer', 'image': 'male_winter_party2.jpg'},
                        {'outfit': 'Wool coat with dress pants', 'image': 'male_winter_party3.jpg'}
                    ]
                }
            },
            'female': {
                'summer': {
                    'casual': [
                        {'outfit': 'Sundress', 'image': 'female_summer_casual1.jpg'},
                        {'outfit': 'T-shirt with shorts', 'image': 'female_summer_casual2.jpg'},
                        {'outfit': 'Tank top with skirt', 'image': 'female_summer_casual3.jpg'}
                    ],
                    'formal': [
                        {'outfit': 'Light blazer with dress', 'image': 'female_summer_formal1.jpg'},
                        {'outfit': 'Silk blouse with pencil skirt', 'image': 'female_summer_formal2.jpg'},
                        {'outfit': 'Linen suit', 'image': 'female_summer_formal3.jpg'}
                    ],
                    'party': [
                        {'outfit': 'Cocktail dress', 'image': 'female_summer_party1.jpg'},
                        {'outfit': 'Off-shoulder top with palazzo pants', 'image': 'female_summer_party2.jpg'},
                        {'outfit': 'Maxi dress', 'image': 'female_summer_party3.jpg'}
                    ]
                },
                'winter': {
                    'casual': [
                        {'outfit': 'Sweater with jeans', 'image': 'female_winter_casual1.jpg'},
                        {'outfit': 'Cardigan with leggings', 'image': 'female_winter_casual2.jpg'},
                        {'outfit': 'Turtleneck with skirt', 'image': 'female_winter_casual3.jpg'}
                    ],
                    'formal': [
                        {'outfit': 'Wool coat with dress', 'image': 'female_winter_formal1.jpg'},
                        {'outfit': 'Blazer with trousers', 'image': 'female_winter_formal2.jpg'},
                        {'outfit': 'Turtleneck with pencil skirt', 'image': 'female_winter_formal3.jpg'}
                    ],
                    'party': [
                        {'outfit': 'Velvet dress', 'image': 'female_winter_party1.jpg'},
                        {'outfit': 'Sequined top with pants', 'image': 'female_winter_party2.jpg'},
                        {'outfit': 'Fur coat with dress', 'image': 'female_winter_party3.jpg'}
                    ]
                }
            }
        }

    def get_recommendation(self, gender, weather, occasion):
        try:
            return self.recommendations[gender.lower()][weather.lower()][occasion.lower()]
        except KeyError:
            return [{'outfit': 'No recommendations available for the given combination.', 'image': None}]

def main():
    recommender = FashionRecommender()
    
    print("Welcome to the Fashion Recommendation System!")
    print("Please provide the following information:")
    
    gender = input("Enter your gender (male/female): ")
    weather = input("Enter the weather (summer/winter): ")
    occasion = input("Enter the occasion (casual/formal/party): ")
    
    recommendations = recommender.get_recommendation(gender, weather, occasion)
    
    print("\nHere are your fashion recommendations:")
    for i, outfit in enumerate(recommendations, 1):
        print(f"{i}. {outfit['outfit']}")

if __name__ == "__main__":
    main() 