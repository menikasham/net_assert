def vote(votes):
    countes = 0
    for item in votes:
        count = votes.count(item)
        if count > countes:
            countes = item
    return countes

