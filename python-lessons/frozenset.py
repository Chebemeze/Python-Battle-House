permissions = {frozenset(["admin", "editor"]): "Full Access"}
permissions = frozenset({"a", "b", "a"})
print(permissions)
alt = frozenset(["admin"])
if permissions == alt:
    print(permissions)
#print(permissions)

new_dict = {}
# def group_by_tag_combination(articles):
#     if articles is None:
#         return {}
#     for index, article in enumerate(articles):
#         for key, value in article.items():
#             if title not in new_dict


# group_by_tag_combination([{"title": "A", "tags": ["python", "web"]}, {"title": "B", "tags": ["web", "python"]}])

