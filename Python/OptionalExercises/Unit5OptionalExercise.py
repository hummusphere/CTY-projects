#-----------------------------------------------------------------------------------------------------------------------

#Calculate and print score.

def football_score(touchdowns, extra_points, two_point_conversions, field_goals, safeties):
    score = int(touchdowns) + int(extra_points) + int(two_point_conversions) + int(field_goals) + int(safeties)
    score = str(score)
    print('The ' + team_name + ' have ' + score + ' points!')

#------------------------------------------------------------------------------------------------------------------------

team_name = 'Dallas Cow Boys' #<- Enter Team Name
football_score(6,1,2,3,2) # <- Enter Numbers (Touchdowns, Extra Points, Two Point Conversions, Field Goals, Safeties)

#------------------------------------------------------------------------------------------------------------------------
