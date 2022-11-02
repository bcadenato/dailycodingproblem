'''
You are given an array of non-negative integers that represents a
two-dimensional elevation map where each element is unit-width wall and the
integer is the height. Suppose it will rain and all spots between two walls
get filled up.

Compute how many units of water remain trapped on the map in O(N) time
and O(1) space.
'''


def calculate_water(wall):
    '''Function to solve
    the problem'''

    print(f'Wall: {wall}')

    ref_position = 0
    ref_height = 0
    water_count = 0

    # Count water from left to right

    for position, pillar in enumerate(wall):

        if pillar >= ref_height:
            ref_height = pillar
            ref_position = position
        else:
            wall[position] = pillar - ref_height

    # Check if there's water on one extreme and if so count water backwards
    # until ref_position

    if wall[-1] < 0:

        ref_height_right = 0

        wall_enum = list(enumerate(wall))

        for position, pillar_trans in wall_enum[-1:ref_position:-1]:
            pillar = ref_height + pillar_trans

            if pillar >= ref_height_right:
                ref_height_right = pillar
                wall[position] = pillar
            else:
                wall[position] = pillar - ref_height_right

    for pillar in wall:
        if pillar < 0:
            water_count += -pillar

    print(f'Water: {water_count}')


calculate_water([3, 0, 1, 3])

calculate_water([2, 1, 1, 4, 2, 2, 4])

calculate_water([2, 1, 1, 4, 2, 2, 2])

calculate_water([2, 1, 1, 4, 1, 0, 2])


















