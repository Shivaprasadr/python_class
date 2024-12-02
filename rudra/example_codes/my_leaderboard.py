import redis

class Leaderboard:
    def __init__(self, name):
        # Connect to the cloud Redis instance
        self.redis_conn = redis.StrictRedis(
            host='redis-17783.c269.eu-west-1-3.ec2.redns.redis-cloud.com',
            port=17783,
            password='pwd',
            decode_responses=True
        )
        self.name = name  # Leaderboard name

    def rank_member(self, member, score):
        # Add member with score to the leaderboard
        self.redis_conn.zadd(self.name, {member: score})

    def rank_for(self, member):
        # Get the rank of a specific member
        # Redis ranks are 0-based; adding 1 for 1-based rank
        rank = self.redis_conn.zrevrank(self.name, member)
        return rank + 1 if rank is not None else None

# Create or attach to a leaderboard named 'highscores'
highscore_lb = Leaderboard('highscores')

# Add members and their scores
highscore_lb.rank_member('player1', 150)
highscore_lb.rank_member('player2', 0)
highscore_lb.rank_member('player3', 180)
highscore_lb.rank_member('player4', 3180)
highscore_lb.rank_member('player5', 1)
highscore_lb.rank_member('player6', '')

# Query a specific member's rank
print(highscore_lb.rank_for('player2'))  # Output: ***


highscore_cricket = Leaderboard('highscores_cricket')
# Add members and their scores
highscore_cricket.rank_member('mahamoes', 3000)
highscore_cricket.rank_member('jones', 0)
highscore_cricket.rank_member('shiva', 180)
highscore_cricket.rank_member('rudra', 3180)
highscore_cricket.rank_member('trump', 1)
highscore_cricket.rank_member('jack', 3)
highscore_cricket.rank_member('jack4', 3)
print(highscore_cricket.rank_for('rudra'))  # Output: **