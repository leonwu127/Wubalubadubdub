WEIGHT  = 1

# Returns a positive integer that will be multipled by weight and and the current score
# Return None if you do not want the snake to go in this direction

def run(data, direction):
    head = [x for x in data["snakes"] if x["id"] == data["our-snake-id"]][0]["coords"][0]

    if direction == "north":
        head[1] -= 1

    if direction == "south":
        head[1] += 1

    if direction == "west":
        head[0] -= 1

    if direction == "east":
        head[0] += 1

    print "\n head " + direction
    print head
    print "\n"

    if head[1] >= data["height"] or head[1] < 0:
        return None

    if head[0] >= data["width"] or head[0] < 0:
        return None

    ## Dont hit your own body
    print "dont hit your body"
    for x in [x for x in data["snakes"] if x["id"] == data["our-snake-id"]][0]["coords"][1:]:
        print x[0]
        print head[0]
        print x[1]
        print head[1]
        
        if x[0] == head[0] and x[1] == head[1]:
            return None
    return 1
