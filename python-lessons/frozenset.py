def group_by_tag_combination(articles):
    same_tags = {}
    for article in articles:
        title = article["title"]
        tag = frozenset(article["tags"])
        same_tags[tag]= same_tags.get(tag, [])
        same_tags[tag].append(title)
    return same_tags
