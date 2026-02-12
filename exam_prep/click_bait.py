from collections import deque

suggested_links_scores = deque([int(x) for x in input().split()])
featured_articles_scores = [int(y) for y in input().split()]
target_engagement_value = int(input())
final_feed = []


while suggested_links_scores and featured_articles_scores:
    current_suggested_score = suggested_links_scores.popleft()
    current_featured_score = featured_articles_scores.pop()
    if current_suggested_score > current_featured_score:
        remainder = current_suggested_score % current_featured_score
        final_feed.append(-remainder)
        if remainder > 0:
            suggested_links_scores.append(remainder *2)

    elif current_suggested_score < current_featured_score:
            remainder = current_featured_score % current_suggested_score
            final_feed.append(remainder)
            if remainder > 0:
                featured_articles_scores.append(remainder * 2)
    else:
        final_feed.append(0)


print(f"Final Feed: {', '.join(map(str, final_feed))}")
if sum(final_feed) >= target_engagement_value:
    print(f"Goal achieved! Engagement Value: {sum(final_feed)}")
else:
    print(f"Goal not achieved! Short by: {abs(sum(final_feed) - target_engagement_value)}")

